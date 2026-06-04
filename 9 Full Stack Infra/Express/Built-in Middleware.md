---
tags: [express, beginner, syntax]
---

# Built-in Middleware

| Middleware             | Use                              |
| ---------------------- | -------------------------------- |
| `express.json()`       | Parse `application/json` body    |
| `express.urlencoded()` | Parse form bodies                |
| `express.static(dir)`  | Serve static files               |
| `express.raw()`        | Raw Buffer body                  |
| `express.text()`       | Plain text body                  |

## Tips
- Set body size limits: `express.json({ limit: '1mb' })`
- Don't enable parsers you won't use

## Related
- [[Middleware]] · [[Body Parsing]] · [[Static Files]]

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
