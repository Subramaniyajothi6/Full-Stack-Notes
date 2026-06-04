# JavaScript Object Methods

Object methods are built-in functions used to work with object properties.

---

# 1. Property Methods

## Object.keys()

### Definition
Returns an array of an object's **own enumerable property keys**.

### Syntax
```javascript
Object.keys(obj)
```

### Example
```javascript
const obj = { name: "John", age: 25 }

Object.keys(obj)
// ["name", "age"]
```

---

## Object.values()

### Definition
Returns an array of an object's **own enumerable property values**.

### Syntax
```javascript
Object.values(obj)
```

### Example
```javascript
Object.values(obj)
// ["John", 25]
```

---

## Object.entries()

### Definition
Returns an array of **[key, value] pairs**.

### Syntax
```javascript
Object.entries(obj)
```

### Example
```javascript
Object.entries(obj)
/*
[
  ["name", "John"],
  ["age", 25]
]
*/
```

---

# 2. Iteration Methods

## for...in

### Definition
Loops through all **enumerable properties (including inherited ones)**.

### Syntax
```javascript
for (let key in obj) {
  // logic
}
```

### Example
```javascript
for (let key in obj) {
  console.log(key, obj[key])
}
```

---

## Safe Iteration

```javascript
for (let key in obj) {
  if (obj.hasOwnProperty(key)) {
    console.log(key, obj[key])
  }
}
```

---

# ⚠️ Edge Cases

### Includes inherited properties
```javascript
const parent = { a: 1 }
const child = Object.create(parent)
child.b = 2

for (let key in child) {
  console.log(key) // b, a
}
```

---

### Object.keys() ignores prototype
```javascript
Object.keys(child) // ["b"]
```

---

### Key order behavior
```javascript
const obj = { 2: "b", 1: "a", name: "John" }

Object.keys(obj)
// ["1", "2", "name"]
```

---

# ❌ Common Mistakes

### Wrong property access

```javascript
const obj = { name: "John", age: 25 }

for (let key in obj) {
  console.log(obj.key) // ❌ undefined
}
```

### Why it is wrong
- `key` is a variable, not a literal property name  
- `obj.key` looks for property `"key"` instead of actual keys like `"name"`

### Fix
```javascript
for (let key in obj) {
  console.log(obj[key]) // ✅ John, 25
}
```

### When to use [key] format
- When property name is **dynamic (stored in a variable)**

---

### Forgetting hasOwnProperty

```javascript
const parent = { a: 1 }
const obj = Object.create(parent)
obj.b = 2

for (let key in obj) {
  console.log(key) // ❌ b, a
}
```

### Why it is wrong
- `for...in` also iterates over **inherited properties (prototype)**  

### Fix
```javascript
for (let key in obj) {
  if (obj.hasOwnProperty(key)) {
    console.log(key) // ✅ b
  }
}
```

### When to use hasOwnProperty() form
- When you want **only object's own properties**

---

### Expecting values from Object.keys()

```javascript
const obj = { name: "John", age: 25 }

Object.keys(obj) // ❌ ["name", "age"]
```

### Why it is wrong
- `Object.keys()` returns only **keys**, not values  

### Fix
```javascript
Object.values(obj) // ✅ ["John", 25]
```

### When to use .values() form
- When you need **values instead of keys**

---

# 💡 Recommended Usage

```javascript
const obj = { name: "John", age: 25 }

Object.entries(obj).forEach(([key, value]) => {
  console.log(key, value)
})
// name John
// age 25
```

### Why this is better
- Gives both key and value together  
- Avoids separate access like `obj[key]`  

### When to use entries
- When working with **both key and value**

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
