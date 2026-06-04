---
tags: [mongodb, intermediate, concept]
---

# Aggregation Pipeline

> Transform documents through ordered stages.

## Anatomy
```js
db.orders.aggregate([
  { $match: { status: 'paid' } },
  { $group: { _id: '$customer', total: { $sum: '$amount' } } },
  { $sort: { total: -1 } },
  { $limit: 10 }
]);
```

## Why pipeline
- Server-side compute
- Use indexes when stages allow
- Can be very efficient if `$match` is early and indexed

## Related
- [[Aggregation Stages]] · [[Lookup and Joins]]

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
