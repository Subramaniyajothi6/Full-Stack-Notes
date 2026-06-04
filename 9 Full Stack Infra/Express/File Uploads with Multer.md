---
tags: [express, intermediate, syntax]
---

# File Uploads with Multer

## Install
```bash
npm i multer
```

## Memory or disk
```js
import multer from 'multer';
const upload = multer({
  storage: multer.diskStorage({
    destination: 'uploads/',
    filename: (req, file, cb) => cb(null, Date.now() + '-' + file.originalname)
  }),
  limits: { fileSize: 5 * 1024 * 1024 }, // 5 MB
  fileFilter: (req, file, cb) => cb(null, file.mimetype.startsWith('image/'))
});

app.post('/avatar', upload.single('file'), (req, res) => {
  res.json({ path: req.file.path });
});
```

## Production
- Stream uploads to S3 / Cloudinary instead of local disk
- Validate type + size + content
- Sanitize filenames (path traversal)

## Related
- [[Body Parsing]] · [[Validation]]

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

## Common Mistakes
- TODO: pitfalls and edge cases

## Best Learning Resources

### Official Documentation
- https://expressjs.com/ — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. Web Dev Simplified, Traversy Media

### Best Free Course
- TODO

### Best Advanced Resource
- TODO

### Best Practice Project
- TODO: 1-paragraph project idea

### Recommended Order to Learn
1. TODO
2. TODO
3. TODO

## Interview Questions
**Q. TODO** — A. ...

**Q. TODO** — A. ...
