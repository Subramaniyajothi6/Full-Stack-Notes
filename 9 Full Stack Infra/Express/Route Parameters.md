---
tags: [express, beginner, syntax]
---

# Route Parameters

## Single param
```js
app.get('/users/:id', (req, res) => req.params.id);
```

## Multiple
`/users/:userId/posts/:postId`

## Coerce + validate
```js
const id = Number(req.params.id);
if (Number.isNaN(id)) return res.status(400).json({ error: 'bad id' });
```

## param middleware
```js
app.param('id', (req, res, next, id) => { req.userId = Number(id); next(); });
```

## Common mistakes
- Trusting params without validation
- Using params for sensitive data (URL appears in logs)

## Related
- [[Routing]] · [[Validation]]

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
