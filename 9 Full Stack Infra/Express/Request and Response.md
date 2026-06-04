---
tags: [express, beginner, concept]
---

# Request and Response

## req
- `req.params` — route params
- `req.query` — query string
- `req.body` — parsed body (after `express.json`)
- `req.headers`, `req.cookies`, `req.ip`

## res
- `res.status(201).json({...})`
- `res.send(text)`
- `res.redirect('/login')`
- `res.cookie('token', t, opts)`
- `res.set('X-Custom', 'v')`

## Streaming
`res` is a Writable stream — `pipe` files or remote responses through.

## Common mistakes
- Calling `res.send` twice (`Cannot set headers after sent`)
- Forgetting `return` after `res.json` then continuing the handler

## Related
- [[Routing]] · [[Body Parsing]]

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

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
