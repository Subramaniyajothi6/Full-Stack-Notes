---
tags: [mongodb, intermediate, syntax]
---

# Update Operators

## Field
`$set` `$unset` `$rename` `$inc` `$mul` `$min` `$max` `$currentDate`

## Array
`$push` `$pull` `$addToSet` `$pop`
With modifiers: `$each`, `$slice`, `$position`, `$sort`

## Examples
```js
db.users.updateOne({ _id }, { $inc: { loginCount: 1 } });
db.posts.updateOne({ _id }, { $addToSet: { tags: 'mern' } });
db.posts.updateOne({ _id }, { $push: { comments: { $each: [c], $slice: -100 } } });
```

## upsert
```js
db.cfg.updateOne({ key: 'theme' }, { $set: { value: 'dark' } }, { upsert: true });
```

## Common mistakes
- Replacing the document by passing a plain object instead of update operators
- `$push` of duplicates instead of `$addToSet`

## Related
- [[CRUD Operations]] · [[Mongoose Schema and Models]]

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
