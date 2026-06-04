---
tags: [react, intermediate, pattern]
---

# Component Composition

> Build features by combining components. Prefer composition over inheritance.

## children prop
```jsx
function Card({ children }) {
  return <div className="card">{children}</div>;
}
<Card><h2>Hi</h2></Card>
```

## Slot pattern
```jsx
function Page({ header, sidebar, content }) { ... }
<Page header={<H/>} sidebar={<S/>} content={<C/>} />
```

## Compound components
```jsx
<Tabs>
  <Tabs.List>
    <Tabs.Tab>One</Tabs.Tab>
  </Tabs.List>
  <Tabs.Panels>
    <Tabs.Panel>Content</Tabs.Panel>
  </Tabs.Panels>
</Tabs>
```

## Common mistakes
- Reaching for HOCs/inheritance when children would do
- Tightly coupling parent and child via prop names

## Related
- [[Higher Order Components]] · [[Render Props]] · [[Components]]

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
