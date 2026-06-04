# JavaScript `this` keyword

## Definition

The `this` keyword refers to the object that is currently executing the function.

Its value depends on how the function is called, not where it is defined.

---

## Syntax

~~~javascript
this
~~~

---

## Basic Example

~~~javascript
const user = {
  name: "John",
  greet() {
    console.log(this.name)
  }
}

user.greet()
~~~

### Output

~~~javascript
John
~~~

---

## Additional Examples

### Global Context

~~~javascript
console.log(this)
~~~

### Output (browser)

~~~javascript
window
~~~

---

### Inside Regular Function

~~~javascript
function show() {
  console.log(this)
}

show()
~~~

### Output

~~~javascript
window (non-strict)
undefined (strict mode)
~~~

---

### Arrow Function Behavior

~~~javascript
const obj = {
  value: 20,
  getValue: () => {
    console.log(this.value)
  }
}

obj.getValue()
~~~

### Output

~~~javascript
undefined
~~~

---

### Using call, apply, bind

~~~javascript
function greet() {
  console.log(this.name)
}

const user = { name: "John" }

greet.call(user)
greet.apply(user)
const fn = greet.bind(user)
fn()
~~~

### Output

~~~javascript
John
John
John
~~~

---

## When to use

- Access object properties inside methods  
- Maintain context in OOP  
- Control execution context using `call`, `apply`, `bind`  

---

## When NOT to use

- Inside arrow functions when object context is required  
- When it causes ambiguity (prefer explicit references if needed)  

---

## Behavior

- Determined at runtime (dynamic binding)  
- Depends on how the function is called (call site)  
- Arrow functions do NOT have their own `this`  
- In strict mode, `this` inside functions is `undefined`  
- In methods, `this` refers to the calling object  

---

## Hoisting (only if applicable)

- `this` is not hoisted  
- It is assigned during execution  

---

## Edge Cases

### Losing `this` in Callback

~~~javascript
const obj = {
  name: "John",
  greet() {
    setTimeout(function () {
      console.log(this.name)
    }, 1000)
  }
}

obj.greet()
~~~

### Output

~~~javascript
undefined
~~~

### Why it is an edge case

Callback function loses object context.

---

### Fix (Arrow Function)

~~~javascript
setTimeout(() => {
  console.log(this.name)
}, 1000)
~~~

### Output

~~~javascript
John
~~~

### Why the fix works

Arrow function inherits `this` from parent scope.

---

### Fix (bind)

~~~javascript
setTimeout(function () {
  console.log(this.name)
}.bind(this), 1000)
~~~

### Output

~~~javascript
John
~~~

### Why the fix works

`bind` explicitly sets `this` to the correct object.

---

## Common Mistakes

### ❌ Wrong Code

~~~javascript
const obj = {
  value: 10,
  getValue: () => {
    console.log(this.value)
  }
}

obj.getValue()
~~~

### Why it is a mistake

Arrow function does not bind its own `this`. It uses the outer scope.

### ✅ Fix

~~~javascript
const obj = {
  value: 10,
  getValue() {
    console.log(this.value)
  }
}

obj.getValue()
~~~

### Why the fix works

Regular method binds `this` to the object.

---

### ❌ Wrong Code

~~~javascript
function test() {
  console.log(this)
}

test()
~~~

### Why it is a mistake

In non-strict mode, `this` defaults to the global object unexpectedly.

### ✅ Fix

~~~javascript
"use strict"

function test() {
  console.log(this)
}

test()
~~~

### Why the fix works

Strict mode prevents global binding and keeps `this` as `undefined`.

---

### ❌ Wrong Code

~~~javascript
const obj = {
  name: "John",
  greet() {
    console.log(this.name)
  }
}

const fn = obj.greet
fn()
~~~

### Why it is a mistake

Function is detached from the object. So `this` is lost.

### ✅ Fix

~~~javascript
const fn = obj.greet.bind(obj)
fn()
~~~

### Why the fix works

`bind(obj)` permanently sets `this` to `obj`.

---

### ❌ Wrong Code

~~~javascript
const obj = {
  name: "John",
  greet() {
    const fn = this.greet
    fn()
  }
}

obj.greet()
~~~

### Why it is a mistake

Method reference is extracted and called as a normal function.

### ✅ Fix

~~~javascript
const obj = {
  name: "John",
  greet() {
    const fn = this.greet.bind(this)
    fn()
  }
}
~~~

### Why the fix works

Binding preserves the correct `this` context.

---

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

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
