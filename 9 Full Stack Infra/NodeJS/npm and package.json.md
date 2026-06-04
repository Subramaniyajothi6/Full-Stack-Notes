---
tags: [nodejs, beginner, tooling]
---

# npm and package.json

> npm is the default package manager. `package.json` is the manifest.

## Key fields
```json
{
  "name": "my-app",
  "version": "1.0.0",
  "type": "module",
  "main": "index.js",
  "scripts": { "start": "node index.js", "test": "vitest" },
  "dependencies": {},
  "devDependencies": {},
  "engines": { "node": ">=20" }
}
```

## Commands
- `npm install` — read package.json, write `node_modules` + lockfile
- `npm install pkg --save-dev`
- `npm run script-name`
- `npm ci` — clean, lockfile-strict install (CI)
- `npm audit` — vulnerability check

## Common mistakes
- Committing `node_modules`
- Not committing lockfile
- Mixing yarn/pnpm/npm in one repo
- Loose semver ranges in production (`^` jumps minor versions)

## Related
- [[Semantic Versioning]] · [[Modules]]

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
