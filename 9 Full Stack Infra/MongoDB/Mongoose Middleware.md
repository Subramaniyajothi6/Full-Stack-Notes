---
tags: [mongoose, mongodb, intermediate, pattern]
---

# Mongoose Middleware

> Hooks before/after operations.

## Pre-save hook
```js
schema.pre('save', async function (next) {
  if (this.isModified('password')) this.password = await bcrypt.hash(this.password, 12);
  next();
});
```

## Other hooks
`pre/post('init', 'validate', 'save', 'remove', 'updateOne', 'findOneAndUpdate', 'aggregate')`.

## Common mistakes
- `function` vs arrow — arrow loses `this`
- Forgetting `next()` (or `await`) → hangs
- Modifying docs in `findOneAndUpdate` hooks — `this` is the query, not the doc

## Related
- [[Mongoose Schema and Models]]

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

## Best Learning Resources

### Official Documentation
- https://www.mongodb.com/docs/ — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. Hussein Nasser, MongoDB official

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
