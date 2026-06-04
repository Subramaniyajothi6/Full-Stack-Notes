# Spread Operator (Objects)

The spread operator (`...`) is used to **copy or merge objects**.

---

## Basic Syntax

```javascript
const obj = { name: "John", age: 25 }

const newObj = { ...obj }
```

---

## Copying Objects

```javascript
const obj = { name: "John" }

const copy = { ...obj }

console.log(copy) // { name: "John" }
```

### Important

```javascript
const a = { name: "John" }
const b = a

b.name = "Sam"

console.log(a.name) // "Sam"
```

This copies **reference**, not the object.

---

### Correct Way (using spread)

```javascript
const a = { name: "John" }
const b = { ...a }

b.name = "Sam"

console.log(a.name) // "John"
```

Now it's a **new object (shallow copy)**.

---

## Merging Objects

```javascript
const obj1 = { name: "John" }
const obj2 = { age: 25 }

const merged = { ...obj1, ...obj2 }

console.log(merged)
// { name: "John", age: 25 }
```

---

## Overwriting Properties

```javascript
const obj1 = { name: "John", age: 20 }
const obj2 = { age: 25 }

const merged = { ...obj1, ...obj2 }

console.log(merged)
// { name: "John", age: 25 }
```

### Rule

- Later values overwrite earlier ones

---

## Shallow Copy (Important)

Spread operator creates a **shallow copy**, not deep copy.

```javascript
const obj = {
  name: "John",
  address: {
    city: "Salem"
  }
}

const copy = { ...obj }

copy.address.city = "Chennai"

console.log(obj.address.city) // "Chennai"
```

### Why?

Nested objects are still **shared by reference**.

---

## Spread vs Reference

```javascript
const a = { name: "John" }

const ref = a
const copy = { ...a }

ref.name = "Sam"

console.log(a.name)   // "Sam"
console.log(copy.name) // "John"
```

---

## Real-world Usage

### Updating object (React style)

```javascript
const user = { name: "John", age: 25 }

const updatedUser = { ...user, age: 26 }
```

---

### Adding new property

```javascript
const user = { name: "John" }

const newUser = { ...user, city: "Salem" }
```

---

## Mental Model

```
Spread → take all properties → put into new object
```

---

## Important Points

- Used to copy objects  
- Used to merge objects  
- Creates shallow copy  
- Later properties overwrite earlier ones  

---

## Interview Summary

- Used for copying and merging objects  
- Does NOT create deep copy  
- Common in React state updates

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
