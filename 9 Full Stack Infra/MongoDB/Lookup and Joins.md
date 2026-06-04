---
tags: [mongodb, advanced, syntax]
---

# Lookup and Joins

```js
db.orders.aggregate([
  { $lookup: {
      from: 'users',
      localField: 'userId',
      foreignField: '_id',
      as: 'user'
  }},
  { $unwind: '$user' }
]);
```

## When (not) to use
- Use sparingly — Mongo isn't optimized for big joins
- Often better to **embed** when read together (see [[Embedded vs Referenced]])

## Pipeline lookup
```js
$lookup: { from, let: { uid: '$userId' }, pipeline: [...], as: 'user' }
```

## Related
- [[Schema Design Patterns]] · [[Embedded vs Referenced]]

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
