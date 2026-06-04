# JavaScript Object Reference Behavior

Objects in JavaScript are stored and copied by **reference**, not by value.

---

## 1. What it means

```javascript
const obj1 = { name: "John" }
const obj2 = obj1
```

- `obj1` and `obj2` point to the **same memory location**

---

## 2. Proof

```javascript
obj2.name = "Doe"

console.log(obj1.name) // "Doe"
```

Changing one affects the other.

---

## 3. Visual

```
obj1 ─┐
      ├──> { name: "John" }
obj2 ─┘
```

---

## 4. Comparison

```javascript
const obj1 = { name: "John" }
const obj2 = { name: "John" }

console.log(obj1 === obj2) // false
```

Why?

- Different memory references

---

## 5. Primitive vs Object

```javascript
let a = 10
let b = a

b = 20

console.log(a) // 10
```

- Primitives → copied by **value**
- Objects → copied by **reference**

---

## 6. Copying Objects (Important)

### ❌ Wrong way (reference copy)

```javascript
const obj1 = { name: "John" }
const obj2 = obj1
```

---

### ✅ Shallow Copy (Spread)

```javascript
const obj1 = { name: "John" }
const obj2 = { ...obj1 }
```

Now:

```javascript
obj2.name = "Doe"

console.log(obj1.name) // "John"
```

---

### ⚠️ Shallow Copy Problem

```javascript
const obj1 = {
  user: { name: "John" }
}

const obj2 = { ...obj1 }

obj2.user.name = "Doe"

console.log(obj1.user.name) // "Doe"
```

Nested objects are still shared.

---

### ✅ Deep Copy (basic way)

```javascript
const obj2 = JSON.parse(JSON.stringify(obj1))
```

⚠️ Limitations:
- loses functions
- loses undefined
- loses special types (Date, Map, etc.)

---

## 7. Real World Problem

```javascript
function updateUser(user) {
  user.name = "Updated"
}

const user = { name: "John" }

updateUser(user)

console.log(user.name) // "Updated"
```

Function modifies original object.

---

## 8. Safe Practice

```javascript
function updateUser(user) {
  return { ...user, name: "Updated" }
}
```

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
