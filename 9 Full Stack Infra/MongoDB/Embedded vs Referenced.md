---
tags: [mongodb, advanced, design]
---

# Embedded vs Referenced

| Choice     | When                                                 |
| ---------- | ---------------------------------------------------- |
| Embedded   | Read together, child has no independent lifecycle    |
| Referenced | Many-to-many, child is large or queried independently|

## Examples
- Order line items → embedded
- User profile → embedded user "settings"
- Comments on a viral post → referenced (unbounded array bad)
- Authors and posts → referenced (M:N)

## Related
- [[Schema Design Patterns]] · [[Mongoose Population]]

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
