---
tags: [nodejs, intermediate, tooling]
---

# Logging in Node

## Why structured logging
Plain `console.log` is hard to query. Use JSON logs with levels.

## Libraries
- **Pino** — fast, JSON
- **Winston** — flexible, transports
- **Bunyan** — JSON

## Best practices
- Add a **request id** correlated across logs
- Levels: trace/debug/info/warn/error/fatal
- Send to stdout — let the platform aggregate (Loki, Datadog)
- Never log secrets

## Related
- [[Error Handling in Node]] · [[Logging with Morgan|Logging with Morgan]]

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
