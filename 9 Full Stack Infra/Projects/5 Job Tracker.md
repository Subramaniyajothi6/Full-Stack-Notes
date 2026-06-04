---
tags: [project, intermediate, mern]
---

# 5. Job Tracker

> You already have the folder — turn it into a polished MERN app.

## Goal
Track applications, statuses, contacts, follow-ups; analytics dashboard.

## Concepts practiced
- Complex filters & sort
- Charts ([[Components|recharts/Chart.js]])
- Date handling (`date-fns`)
- CSV export

## Schema sketch
```
Application: {
  user, company, role, status: enum,
  appliedAt, contacts: [{ name, email, role }],
  events: [{ at, type, note }],   // applied, screened, interviewed, rejected
  salaryRange, location, link
}
```

## Milestones
1. Auth (reuse project 3)
2. Application CRUD with status timeline
3. Filter + group + sort
4. Dashboard: applications/week, status funnel, time-to-response
5. Reminders for follow-up
6. CSV export, search

## Next
- [[6 Real-time Chat]]

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
