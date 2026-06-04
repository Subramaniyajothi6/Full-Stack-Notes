---
tags: [express, intermediate, pattern]
---

# Router Modules

> Split routes across files using `express.Router`.

```js
// users.routes.js
import { Router } from 'express';
const r = Router();
r.get('/', list);
r.post('/', create);
export default r;

// app.js
import users from './routes/users.routes.js';
app.use('/users', users);
```

## Mount-time middleware
```js
app.use('/admin', requireAdmin, adminRouter);
```

## Common mistakes
- Forgetting `export default`
- Defining routes inline in `app.js` until it explodes
- Cyclic imports between routers and controllers

## Related
- [[Routing]] · [[Middleware]]

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
