---
tags: [mongodb, intermediate, syntax]
---

# Query Operators

## Comparison
`$eq` `$ne` `$gt` `$gte` `$lt` `$lte` `$in` `$nin`

## Logical
`$and` `$or` `$not` `$nor`

## Element
`$exists` `$type`

## Array
`$all` — all elements present
`$elemMatch` — at least one element matches all conditions
`$size` — array length

## Regex
```js
{ name: /^A/i }
```

## Examples
```js
db.products.find({ price: { $gte: 10, $lte: 100 }, tags: { $in: ['sale'] } });
db.orders.find({ items: { $elemMatch: { sku: 'X', qty: { $gt: 1 } } } });
```

## Related
- [[CRUD Operations]] · [[Indexes]]

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
