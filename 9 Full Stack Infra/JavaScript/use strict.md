# JavaScript use strict

`"use strict"` enables **Strict Mode** in JavaScript.

Strict Mode is a **restricted version of JavaScript** that helps catch common mistakes and prevents unsafe behavior.

It makes the code **more secure, predictable, and easier to debug**.

---

# Why Strict Mode exists

Early JavaScript allowed many **unsafe or confusing behaviors**, such as:

- creating variables accidentally
- silent errors
- incorrect `this` binding
- duplicate parameters

Strict Mode was introduced in **ES5** to prevent these problems.

---

# How to enable Strict Mode

## 1. Global strict mode

```javascript
"use strict"

let x = 10
```

Strict mode applies to the **entire script**.

---

## 2. Function-level strict mode

```javascript
function test() {
  "use strict"

  let x = 10
}
```

Strict mode applies **only inside that function**.

---

# Common Errors Prevented by Strict Mode

## 1. Prevents accidental global variables

Without strict mode:

```javascript
x = 10
console.log(x)
```

JavaScript automatically creates a **global variable**.

With strict mode:

```javascript
"use strict"

x = 10
```

Error:

```
ReferenceError: x is not defined
```

---

## 2. Prevents deleting variables

```javascript
"use strict"

let x = 10
delete x
```

Error:

```
SyntaxError
```

---

## 3. Prevents duplicate parameters

Without strict mode:

```javascript
function add(a, a) {
  return a
}
```

Allowed but confusing.

With strict mode:

```
SyntaxError
```

---

## 4. `this` behavior in functions

Without strict mode:

```javascript
function test() {
  console.log(this)
}

test()
```

Output:

```
window
```

With strict mode:

```javascript
"use strict"

function test() {
  console.log(this)
}

test()
```

Output:

```
undefined
```

---

# Strict Mode Restrictions

Strict mode disallows:

- undeclared variables
- deleting variables or functions
- duplicate function parameters
- some unsafe syntax

---

# Important Note

ES6 modules and modern JavaScript tools **automatically use strict mode**.

Example:

```javascript
export const value = 10
```

Modules run in **strict mode by default**, so `"use strict"` is usually unnecessary in modern projects.

---

# When to use it

Strict mode is useful because it:

- prevents silent errors
- improves debugging
- enforces cleaner JavaScript
- avoids accidental global variables

Most modern JavaScript environments already enforce strict mode.

---

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
- https://developer.mozilla.org/en-US/docs/Web/JavaScript — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. Web Dev Simplified, Fireship, The Net Ninja

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
