---
tags: [system-design, intermediate, scale]
---

# Horizontal vs Vertical Scaling

| Vertical                     | Horizontal                             |
| ---------------------------- | -------------------------------------- |
| Bigger machine               | More machines                           |
| Easy, no code change         | Needs stateless services + LB          |
| Limited by hardware          | Near-linear scale                       |
| Single point of failure      | HA via redundancy                       |

## Practical advice
Make services stateless first; horizontal scale follows naturally. Use [[Load Balancing]] in front.

## Related
- [[Load Balancing]] · [[Replication in System Design]]

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
- https://aws.amazon.com/architecture/ — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. ByteByteGo, Hussein Nasser

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
