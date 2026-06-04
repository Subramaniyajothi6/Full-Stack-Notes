---
tags: [project, intermediate, mern]
---

# 3. Authentication System

> Foundational auth flow you'll reuse in every other project.

## Concepts practiced
- bcrypt password hashing
- [[JWT Authentication|JWT access + refresh]]
- [[Cookies and Sessions|httpOnly cookies]]
- [[Protected Routes|Protected Routes]]
- [[Helmet and Security|Helmet]] + [[Rate Limiting|rate limiting]]

## Milestones
1. Signup/login (bcrypt, validation)
2. JWT issue → cookie
3. Auth middleware (`req.user`)
4. Refresh token rotation
5. Logout (clear cookies, revoke refresh)
6. React: login page → protected dashboard
7. Forgot/reset password (email token)

## Common mistakes
- Storing JWT in localStorage
- No refresh strategy → 1h tokens or worse
- Same secret for access + refresh
- No CSRF protection on cookie auth

## Next
- [[4 Blog Platform]]

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
