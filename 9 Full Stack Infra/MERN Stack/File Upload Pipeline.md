---
tags: [mern, integration, intermediate]
---

# File Upload Pipeline

> A production upload flow: browser → presigned URL → S3 → event → worker processes → metadata in DB → CDN serves.

## The flow
```
[Browser]
   │ 1. POST /api/uploads/init  { name, mimeType, size }
   ▼
[API]
   │ generates presigned PUT URL, creates pending Upload row
   │ returns { uploadId, url, fields }
   ▼
[Browser]
   │ 2. PUT directly to S3 using presigned URL (no API hop)
   ▼
[S3]
   │ ObjectCreated event
   ▼
[Lambda / Queue worker]
   │ 3. Validate (mime, size, virus scan)
   │ 4. Process (resize images, transcode video, extract metadata)
   │ 5. Update Upload row: status=ready, derived URLs
   ▼
[CDN] serves the final asset
```

## Server: presigned URL
```ts
import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3';
import { getSignedUrl } from '@aws-sdk/s3-request-presigner';
import { z } from 'zod';

const Init = z.object({
  name: z.string().max(200),
  mimeType: z.string().regex(/^(image|video)\//),
  size: z.number().max(50 * 1024 * 1024),
});

app.post('/api/uploads/init', requireAuth, async (req, res) => {
  const body = Init.parse(req.body);
  const upload = await Upload.create({
    userId: req.user.sub, status: 'pending', mimeType: body.mimeType,
  });
  const key = `uploads/${req.user.sub}/${upload.id}/${body.name}`;
  const url = await getSignedUrl(s3, new PutObjectCommand({
    Bucket: 'myapp-uploads', Key: key,
    ContentType: body.mimeType, ContentLength: body.size,
  }), { expiresIn: 60 });
  res.json({ uploadId: upload.id, url, key });
});
```

## Client: upload directly
```tsx
async function upload(file: File) {
  const init = await fetch('/api/uploads/init', {
    method: 'POST',
    body: JSON.stringify({ name: file.name, mimeType: file.type, size: file.size }),
  }).then(r => r.json());

  await fetch(init.url, {
    method: 'PUT',
    headers: { 'Content-Type': file.type },
    body: file,
  });

  // Poll for processing or use websocket
  return init.uploadId;
}
```

## Processing worker
- **Images** — `sharp` for resize + format conversion (WebP/AVIF)
- **Video** — [[FFmpeg]] for HLS variants + thumbnails
- **PDF** — `pdf-lib` / Ghostscript for thumbnail
- **Validation** — `file-type` to verify mime by magic bytes (not just trust the extension)
- **Antivirus** — ClamAV for user-shared files

## Real World Usage
- Profile avatars
- Product images for e-commerce
- Video uploads (YouTube-style HLS pipeline)
- PDF document workflows
- AI training data ingestion
- Voice memo storage

## Common Mistakes
- **Proxying uploads through the API** — wastes server bandwidth + memory; use presigned URLs
- Trusting `Content-Type` from client (verify by magic bytes server-side)
- No size limit on presigned URL (`ContentLength`) → unbounded uploads
- Storing originals on the API container disk (lost on redeploy)
- No virus scanning for user-shared files
- Letting users dictate the S3 key path → path traversal / overwrite attacks
- Slow processing blocks the upload UX → use a job queue + status polling/websocket
- Public bucket when content should be private — generate signed CDN URLs for reads

## Prerequisites
- [[AWS S3]] · [[Object Storage]] · [[Background Jobs]] · [[CDN]]

## What To Learn Next
- [[Email Infrastructure]] · [[Stripe Integration]]

## Best Learning Resources

### Official Documentation
- [AWS S3 Presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/PresignedUrlUploadObject.html)
- [Sharp (image processing)](https://sharp.pixelplumbing.com/)
- [Cloudflare R2 (S3-compatible alt)](https://developers.cloudflare.com/r2/)
- [Mux video docs](https://docs.mux.com/) — managed video pipeline

### Best YouTube Resource
- [Theo — file upload UX](https://www.youtube.com/@t3dotgg)
- [Hussein Nasser — S3 multipart upload](https://www.youtube.com/@hnasr)

### Best Free Course
- [Mux Video 101 series](https://www.mux.com/blog/) — best modern primer on video upload pipeline
- [AWS Skill Builder — S3 storage](https://explore.skillbuilder.aws/)

### Best Advanced Resource
- [Mux engineering blog — video stack at scale](https://www.mux.com/blog/)
- [Cloudinary engineering blog — image processing](https://cloudinary.com/blog)

### Best Practice Project
Add image uploads to a MERN app: presigned PUT → S3 → Lambda triggers Sharp resize → 3 sizes (thumb / medium / large) → CDN. Show progress in the UI; handle network failures with resume/retry.

### Recommended Order to Learn
1. Direct upload via presigned URL
2. Validate metadata server-side (mime, size)
3. Magic-byte verification post-upload
4. Async processing pipeline
5. Multiple variants (resize / transcode)
6. CDN with cache headers
7. Resumable uploads for large files (multipart)

## Interview Questions
**Q. Why upload via presigned URL instead of through your API?**
A. Server doesn't proxy bytes; saves CPU/memory/bandwidth and scales infinitely with S3.

**Q. How do you stop a user from uploading 100GB?**
A. `ContentLength` in the presigned URL caps the size; S3 rejects oversize requests.

**Q. How do you verify file type beyond the `Content-Type` header?**
A. Read the first bytes (magic numbers) server-side. Use `file-type` package.

## Related
- [[AWS S3]] · [[Object Storage]] · [[Background Jobs]] · [[CDN]] · [[FFmpeg]]
