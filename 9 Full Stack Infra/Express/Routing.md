---
tags: [express, beginner, concept]
---

# Routing

## Methods
```js
app.get('/users', list);
app.post('/users', create);
app.put('/users/:id', replace);
app.patch('/users/:id', update);
app.delete('/users/:id', remove);
```

## Path patterns
- `/users/:id` — param
- `/users/:id?` — optional
- `/files/*` — wildcard
- Regex: `app.get(/.*fly$/, ...)`

## app.use vs app.METHOD
`use` matches any HTTP method and any path prefix.

## Order matters
First match wins.

## Related
- [[Route Parameters]] · [[Router Modules]] · [[Middleware]]

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
