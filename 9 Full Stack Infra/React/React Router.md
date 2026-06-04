---
tags: [react, intermediate, routing]
---

# React Router

> Declarative routing for React SPAs.

## v6 setup
```jsx
import { BrowserRouter, Routes, Route, Link, useParams } from 'react-router-dom';

<BrowserRouter>
  <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/users/:id" element={<User />} />
    <Route path="*" element={<NotFound />} />
  </Routes>
</BrowserRouter>
```

## Navigation
- `<Link to="/x">` declarative
- `useNavigate()` programmatic
- `useParams()` route params
- `useSearchParams()` query strings

## Nested routes
Parent route renders `<Outlet />` for children.

## Common mistakes
- Forgetting BrowserRouter wrapper
- Hash routing in production without reason
- Not handling 404 (`path="*"`)

## Related
- [[Protected Routes]] · [[Code Splitting]]

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

## Best Learning Resources

### Official Documentation
- https://react.dev/ — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. Jack Herrington, Theo, Web Dev Simplified

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
