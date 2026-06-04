---
tags: [mongodb, beginner, syntax]
---

# CRUD Operations

## Insert
```js
db.users.insertOne({ name: 'A' });
db.users.insertMany([{...}, {...}]);
```

## Find
```js
db.users.find({ age: { $gte: 18 } });
db.users.findOne({ _id });
```

## Update
```js
db.users.updateOne({ _id }, { $set: { age: 30 } });
db.users.updateMany({ active: false }, { $set: { archived: true } });
```

## Delete
```js
db.users.deleteOne({ _id });
db.users.deleteMany({ archived: true });
```

## Common mistakes
- Using `update` (full replace) when `$set` is intended
- No index on the filter → collection scan
- Forgetting `_id` is unique

## Related
- [[Query Operators]] · [[Update Operators]] · [[Indexes]]

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
