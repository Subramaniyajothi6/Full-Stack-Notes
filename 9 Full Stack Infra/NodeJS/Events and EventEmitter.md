---
tags: [nodejs, intermediate, concept]
---

# Events and EventEmitter

> Pub/sub primitive used everywhere in Node.

## Basics
```js
import { EventEmitter } from 'events';
const bus = new EventEmitter();

bus.on('msg', payload => console.log(payload));
bus.emit('msg', { hi: 1 });
```

## API surface
- `on`, `once`, `off`
- `emit`, `listenerCount`
- `setMaxListeners`

## Common mistakes
- Memory leak warning ("possible EventEmitter memory leak") — too many listeners not removed
- Throwing inside an `error` listener — process exits if uncaught
- Synchronous emit assumed async

## Related
- [[Streams]] · [[HTTP Module]]

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
