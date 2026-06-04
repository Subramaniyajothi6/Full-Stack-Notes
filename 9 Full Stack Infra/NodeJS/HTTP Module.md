---
tags: [nodejs, intermediate, concept]
---

# HTTP Module

> Built-in `http` module — what Express is built on.

## Bare server
```js
import http from 'http';
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello');
});
server.listen(3000);
```

## req/res
- `req` is a Readable stream
- `res` is a Writable stream
- Headers must be set before `res.write`

## Common mistakes
- Not handling `req.on('error')`
- Forgetting `res.end()`
- Buffering huge requests in memory

## Related
- [[Streams]] · [[What is Express|What is Express]]

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
