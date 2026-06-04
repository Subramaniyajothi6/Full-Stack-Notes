---
tags: [mongoose, mongodb, beginner, syntax]
---

# Mongoose Schema and Models

```js
import mongoose from 'mongoose';
const userSchema = new mongoose.Schema({
  email: { type: String, required: true, unique: true, lowercase: true },
  name:  { type: String, trim: true },
  role:  { type: String, enum: ['user','admin'], default: 'user' },
}, { timestamps: true });

userSchema.methods.fullLabel = function () { return `${this.name} <${this.email}>`; };
userSchema.statics.findByEmail = function (email) { return this.findOne({ email }); };

export const User = mongoose.model('User', userSchema);
```

## Common mistakes
- Adding fields not in schema (set `strict: true` — default)
- Forgetting `unique: true` doesn't validate before insert (use `pre('save')`)
- Putting business logic in models too aggressively

## Related
- [[Mongoose Validation]] · [[Mongoose Middleware]]

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
