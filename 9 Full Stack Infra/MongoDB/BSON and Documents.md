---
tags: [mongodb, beginner, concept]
---

# BSON and Documents

> BSON = Binary JSON. Adds types JSON lacks.

## Extra types
- `ObjectId`
- `Date`
- `Decimal128`
- Binary, regex

## Document
A row equivalent — up to 16 MB.
```json
{
  "_id": ObjectId("..."),
  "title": "Hello",
  "tags": ["mern","blog"],
  "author": { "name": "X" },
  "createdAt": ISODate("...")
}
```

## Common mistakes
- Documents larger than 16 MB → split or use GridFS
- Storing date as string instead of `Date`

## Related
- [[Collections and Databases]] · [[CRUD Operations]]

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
