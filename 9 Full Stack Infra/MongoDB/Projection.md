---
tags: [mongodb, intermediate, syntax]
---

# Projection

> Choose which fields to return.

```js
db.users.find({ active: true }, { name: 1, email: 1, _id: 0 });
```

## Inclusion vs exclusion
Cannot mix (except `_id`).

## Slice arrays
```js
{ comments: { $slice: 5 } }
```

## Why care
- Saves bandwidth + memory
- Avoids leaking sensitive fields (passwordHash)

## Related
- [[Query Operators]] · [[Mongoose Schema and Models]]

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
