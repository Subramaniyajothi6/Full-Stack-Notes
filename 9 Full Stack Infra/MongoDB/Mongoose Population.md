---
tags: [mongoose, mongodb, intermediate, pattern]
---

# Mongoose Population

> Replace `ObjectId` refs with the referenced document.

## Schema
```js
const post = new Schema({
  author: { type: Schema.Types.ObjectId, ref: 'User' }
});
```

## Query
```js
const posts = await Post.find().populate('author', 'name email');
```

## Deep populate
```js
.populate({ path: 'comments', populate: { path: 'author' } });
```

## Costs
- Each populate is an extra query — N+1 risk
- Consider embedding or `$lookup` aggregation for hot paths

## Related
- [[Embedded vs Referenced]] · [[Lookup and Joins]]

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
