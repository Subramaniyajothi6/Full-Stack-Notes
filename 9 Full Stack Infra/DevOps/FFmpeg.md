---
tags: [infra, performance, intermediate]
---

# FFmpeg

> The Swiss army knife of audio/video. Open-source library + CLI for decode/encode/transcode/filter media.

## Why it matters
Anything involving video — uploads, thumbnails, transcoding, streaming, recording — touches FFmpeg. It's behind YouTube, VLC, OBS, almost every video product.

## Core concepts
- **Container** — `.mp4`, `.mkv`, `.webm`, `.mov` — wraps streams
- **Codec** — H.264, H.265, AV1 (video); AAC, Opus, MP3 (audio)
- **Stream** — video, audio, subtitle inside container
- **Filtergraph** — chain of operations: scale, crop, overlay, fps
- **HLS / DASH** — adaptive streaming via segmented playlists
- **FFmpeg.wasm** — port that runs in browsers via [[WASM]]

## Cheat sheet
```bash
ffmpeg -i in.mov -c:v libx264 -crf 23 -c:a aac out.mp4   # transcode
ffmpeg -i in.mp4 -ss 00:00:30 -t 5 out.gif               # 5-sec gif
ffmpeg -i in.mp4 -vf "scale=720:-1" out.mp4              # resize
ffmpeg -i in.mp4 -vn out.mp3                             # extract audio
ffmpeg -i in.mp4 -hls_time 4 -hls_list_size 0 out.m3u8   # HLS
ffmpeg -i in.mp4 -ss 5 -frames:v 1 thumb.jpg             # thumbnail
ffprobe -v quiet -print_format json -show_streams in.mp4 # inspect
```

## Real World Usage
- Video upload pipeline: probe → transcode to multiple bitrates → HLS
- Thumbnail generation
- Live streaming (RTMP → HLS)
- Audio normalization
- Browser-side conversion via FFmpeg.wasm

## Common Mistakes
- Not capping CPU — transcoding can exhaust workers
- Trusting input — check duration / dimensions / codecs first (security)
- Re-encoding when stream copy works (`-c copy`)
- HLS without proper keyframe interval — bad seeking
- Forgetting `-y` in scripts → prompts hang CI

## Prerequisites
- [[CLI]] · basic media literacy

## What To Learn Next
- [[WASM]] · [[Object Storage]] · [[CDN|CDN]]

## Best Learning Resources

### Official Documentation
- [FFmpeg docs](https://ffmpeg.org/documentation.html) — comprehensive but dense
- [FFmpeg.wasm docs](https://ffmpegwasm.netlify.app/)

### Best YouTube Resource
- [Computerphile — How JPEG/MP4 work](https://www.youtube.com/c/Computerphile)
- [Mux engineers — video tech talks](https://www.youtube.com/c/MuxHQ)

### Best Free Course
- [Mux Video 101 series](https://www.mux.com/blog/) — best modern primer on video stack
- [Streaming tech blog series — Bitmovin](https://bitmovin.com/blog/)

### Best Advanced Resource
- [Mux blog](https://www.mux.com/blog/) — engineering depth on encoding/streaming
- [Bitmovin blog](https://bitmovin.com/blog/) — codecs, ABR, low-latency

### Best Practice Project
Build a video upload pipeline: presigned S3 upload → SQS → worker that runs `ffmpeg` to make 1080p/720p/480p HLS variants → upload back to S3 → CloudFront → HTML video player. Add a thumbnail at 5 seconds.

### Recommended Order to Learn
1. Containers vs codecs
2. Basic transcode + scale + crop
3. Filtergraphs
4. HLS / DASH adaptive streaming
5. Hardware acceleration (NVENC, VAAPI)
6. FFmpeg.wasm browser-side

## Interview Questions
**Q. Container vs codec?**
A. Container is the file format wrapping streams (`.mp4`). Codec is the compression algorithm for a stream (H.264, AAC).

**Q. Why HLS over plain MP4 for streaming?**
A. Adaptive bitrate — playlist of segments at multiple qualities; client switches based on network.

**Q. When to use `-c copy`?**
A. When you only need to remux (change container) without re-encoding — fast and lossless.

## Related
- [[WASM]] · [[Object Storage]] · [[AWS S3]]
