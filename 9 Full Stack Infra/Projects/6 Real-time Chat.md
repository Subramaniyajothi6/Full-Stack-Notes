---
tags: [project, advanced, mern]
---

# 6. Real-time Chat

> Introduces WebSockets and presence.

## Stack additions
- **Socket.IO** — see [[WebSockets|WebSockets]]
- **Redis adapter** — to scale across instances

## Concepts practiced
- Rooms (channels, DMs)
- Presence (online/offline)
- Typing indicators
- Read receipts
- Message persistence + history (cursor pagination)

## Milestones
1. Auth + sessions
2. Socket connection authenticated via token
3. Channels + DMs
4. Presence with Redis
5. Message history paginated
6. Typing indicator
7. Notifications (browser push)

## Common mistakes
- Not authenticating sockets
- Storing socket → user mapping in memory (breaks on multiple instances)
- Sending entire history on connect → kills first paint

## Next
- [[7 E-commerce Storefront]]

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

## Best Learning Resources

### Official Documentation
-  — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. 

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
