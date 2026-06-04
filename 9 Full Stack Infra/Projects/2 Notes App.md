---
tags: [project, beginner, mern]
---

# 2. Notes App

> Adds search, pagination, and richer Mongoose features.

## Goal
Markdown notes with full-text search and tags.

## Concepts practiced
- [[Indexes|Text indexes]]
- [[Pagination and Filtering|Pagination & filtering]]
- [[React Router|React Router]] (per-note view)
- Markdown rendering (`react-markdown`)

## Milestones
1. CRUD `/notes` with `title`, `body`, `tags`
2. `?q=...` text search using `$text` index
3. Pagination (cursor or offset)
4. Tag filter
5. Per-note view + edit page

## Common mistakes
- Searching without text index → slow
- Loading entire body in list view (use projection)

## Next
- [[3 Authentication System]]

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
