---
tags: [mongodb, intermediate, performance]
---

# Indexes

> The single biggest perf lever in MongoDB.

## Create
```js
db.users.createIndex({ email: 1 }, { unique: true });
db.posts.createIndex({ author: 1, createdAt: -1 });
db.products.createIndex({ name: 'text', description: 'text' });
```

## Types
- Single field
- Compound — see [[Compound Indexes]]
- Text
- Geo (`2dsphere`)
- Hashed (sharding)
- TTL — auto-expire docs

## Costs
- Slow writes (every index updated)
- Disk space

## Common mistakes
- No index on common filter
- Too many indexes
- Wrong field order in compound (see [[Compound Indexes]])

## Related
- [[Compound Indexes]] · [[Explain and Query Plans]]

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
