---
tags: [project, intermediate, mern]
---

# 4. Blog Platform

> CMS-style with roles, comments, drafts.

## Concepts practiced
- Role-based access (author, admin)
- [[Schema Design Patterns|Embedded vs referenced]] for comments
- Slug generation, SEO
- Image uploads ([[File Uploads with Multer|Multer]] → S3/Cloudinary)
- Markdown editor

## Milestones
1. Auth from project 3
2. Posts CRUD, draft/publish
3. Slug + permalink
4. Comments — embed initially, switch to referenced when one post explodes
5. Image upload pipeline
6. Admin dashboard (user list, ban, feature posts)

## Common mistakes
- Trusting `role` from frontend
- No XSS sanitization on rendered HTML

## Next
- [[5 Job Tracker]]

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
