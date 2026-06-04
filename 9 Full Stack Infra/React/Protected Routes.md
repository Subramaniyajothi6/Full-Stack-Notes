---
tags: [react, intermediate, routing]
---

# Protected Routes

> Block unauthenticated users from certain routes.

## Pattern
```jsx
function RequireAuth({ children }) {
  const { user } = useAuth();
  return user ? children : <Navigate to="/login" replace />;
}

<Route path="/dashboard" element={<RequireAuth><Dashboard /></RequireAuth>} />
```

## Loaders (v6.4+)
Use `loader` to fetch + redirect on auth failure server-side style.

## Common mistakes
- Storing JWT in localStorage without thinking about XSS — see [[JWT Authentication|JWT Authentication]]
- Flicker before redirect — gate render until auth resolved

## Related
- [[React Router]] · [[JWT Authentication|JWT Authentication]]

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
