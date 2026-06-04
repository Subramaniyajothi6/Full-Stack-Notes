---
tags: [mongoose, mongodb, intermediate, syntax]
---

# Mongoose Validation

```js
const schema = new mongoose.Schema({
  age: { type: Number, min: 0, max: 130 },
  email: { type: String, match: /^\S+@\S+$/ },
  status: { type: String, enum: ['active','banned'] },
  bio: { type: String, validate: v => v.length <= 500 }
});
```

## Where it fires
- `save()`, `create()`, `validate()`
- `findOneAndUpdate({ runValidators: true })` — opt-in
- Bulk ops bypass by default

## Related
- [[Validation|Express Validation]]

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
