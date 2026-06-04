---
tags: [nodejs, advanced, concurrency]
---

# Child Process

> Spawn separate OS processes. Useful for shelling out or long-running CPU jobs.

## APIs
- `spawn` — stream stdout/stderr (long-running)
- `exec` — buffer output (short commands)
- `fork` — spawn another Node process with IPC channel
- `execFile` — like exec but no shell (safer)

## Example
```js
import { spawn } from 'child_process';
const ls = spawn('ls', ['-la']);
ls.stdout.on('data', d => console.log(d.toString()));
```

## Common mistakes
- `exec` with user input → command injection. Use `execFile` or sanitize.
- Ignoring exit codes
- Letting buffers explode (`exec` default 200kb)

## Related
- [[Cluster and Worker Threads]] · [[Streams]]

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
