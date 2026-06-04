---
tags: [mongodb, advanced, performance]
---

# Explain and Query Plans

```js
db.users.find({ email }).explain('executionStats');
```

## Key fields
- `winningPlan.stage` — `IXSCAN` good, `COLLSCAN` bad (unless tiny)
- `executionStats.totalDocsExamined` — should be near `nReturned`
- `executionStats.executionTimeMillis`

## Index hint
```js
db.users.find({...}).hint({ email: 1 });
```

## Related
- [[Indexes]] · [[Compound Indexes]]

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
