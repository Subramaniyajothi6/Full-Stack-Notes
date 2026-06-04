---
tags: [express, intermediate, pattern]
---

# Validation

> Validate every input that crosses a trust boundary. Reject early.

## Libraries
- **Zod** — TS-native, infer types
- **Joi** — mature
- **express-validator** — chain API

## Zod example
```js
import { z } from 'zod';
const Body = z.object({ email: z.string().email(), age: z.number().int().min(0) });

app.post('/users', (req, res) => {
  const parse = Body.safeParse(req.body);
  if (!parse.success) return res.status(400).json(parse.error.flatten());
  // parse.data is typed
});
```

## Common mistakes
- Trusting `req.params` and `req.query`
- Validating only on the happy path
- Returning DB validation errors verbatim (leaks schema)

## Related
- [[Body Parsing]] · [[Error Handling Middleware]]

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
