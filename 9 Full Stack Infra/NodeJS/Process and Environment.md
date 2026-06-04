---
tags: [nodejs, beginner, concept]
---

# Process and Environment

> The `process` global gives access to the running Node process.

## Common uses
```js
process.env.NODE_ENV     // env vars
process.argv             // CLI args
process.cwd()            // working dir
process.exit(1)          // exit with code
process.on('SIGINT', ...) // signal handlers
process.on('uncaughtException', ...)
```

## Env config
- Use `dotenv` to load `.env` in dev
- Never commit secrets

## Common mistakes
- Calling `process.exit()` mid-request — drops in-flight work
- Reading `process.env` deep in code — centralize in a config module
- Not handling `SIGTERM` for graceful shutdown

## Related
- [[Error Handling in Node]] · [[Helmet and Security|Helmet and Security]]

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

## Best Learning Resources

### Official Documentation
- https://nodejs.org/en/docs — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. Hussein Nasser, TechWorld with Nana, Traversy Media

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
