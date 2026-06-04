---
tags: [express, beginner, syntax]
---

# Template Engines

> SSR templating for non-API apps. For SPAs, skip this.

## Setup (EJS)
```js
app.set('view engine', 'ejs');
app.set('views', './views');
app.get('/', (req, res) => res.render('home', { title: 'Hi' }));
```

## Engines
- EJS — simple
- Pug — indentation-based
- Handlebars — logic-light

## When to use
Server-rendered marketing pages, admin tools, simple CRUD.

## Related
- [[Static Files]] · [[Server Components|Server Components]]

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
- https://expressjs.com/ — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. Web Dev Simplified, Traversy Media

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
