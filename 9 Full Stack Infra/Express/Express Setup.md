---
tags: [express, beginner, syntax]
---

# Express Setup

## Install
```bash
npm i express
```

## Minimal app
```js
import express from 'express';
const app = express();

app.get('/', (req, res) => res.send('Hello'));

app.listen(3000, () => console.log('http://localhost:3000'));
```

## Recommended structure
```
src/
  index.js
  app.js          // express() + middleware + routes
  routes/
    users.routes.js
  controllers/
    users.controller.js
  models/
  middleware/
  config/
```

## Related
- [[Routing]] · [[Middleware]]

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
