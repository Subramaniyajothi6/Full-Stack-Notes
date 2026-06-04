---
tags: [react, intermediate, state-management]
---

# Redux Toolkit

> The official, opinionated way to write Redux. Far less boilerplate.

## Slice example
```js
import { createSlice } from '@reduxjs/toolkit';

const counter = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    inc: s => { s.value++ },          // Immer lets you "mutate"
    add: (s, a) => { s.value += a.payload }
  }
});
export const { inc, add } = counter.actions;
export default counter.reducer;
```

## Store
```js
import { configureStore } from '@reduxjs/toolkit';
const store = configureStore({ reducer: { counter: counter.reducer } });
```

## Hooks
```js
const value = useSelector(s => s.counter.value);
const dispatch = useDispatch();
```

## RTK Query
Built-in data fetching + caching layer; replaces hand-written thunks.

## Common mistakes
- Real mutation outside Immer-wrapped reducers
- Putting non-serializable data in store
- Recomputing selectors instead of using `createSelector`

## Related
- [[Redux Basics]] · [[Context API]]

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
