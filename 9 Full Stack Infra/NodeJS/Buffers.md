---
tags: [nodejs, intermediate, concept]
---

# Buffers

> Fixed-size raw bytes. Used wherever Node deals with binary data (files, network).

## Create
```js
Buffer.from('hello', 'utf8')   // from string
Buffer.from([0x01, 0x02])      // from array
Buffer.alloc(10)               // zero-filled
Buffer.allocUnsafe(10)         // uninitialized — fast but caution
```

## Common conversions
```js
buf.toString('utf8')
buf.toString('hex')
buf.toString('base64')
```

## Common mistakes
- Treating Buffer as string — concatenate with care
- `Buffer.allocUnsafe` left unfilled (may leak memory contents)

## Related
- [[Streams]] · [[File System]]

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

## Best Learning Resources

### Official Documentation
- https://nodejs.org/en/docs — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. Hussein Nasser, TechWorld with Nana, Traversy Media

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
