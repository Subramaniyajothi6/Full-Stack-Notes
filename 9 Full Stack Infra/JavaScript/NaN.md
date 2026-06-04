# JavaScript NaN (Not a Number)

`NaN` stands for **Not a Number**.

It represents a value that is **not a valid number**, usually the result of an invalid mathematical operation.

---

# What is NaN?

`NaN` is a special value in JavaScript of type **number**.

```javascript
typeof NaN
```

Output

```
"number"
```

Yes, it’s confusing. JavaScript made that choice and never looked back.

---

# How NaN Occurs

## Invalid Number Conversion

```javascript
Number("hello") // NaN
```

---

## Invalid Math Operations

```javascript
"abc" - 2   // NaN
0 / 0       // NaN
Math.sqrt(-1) // NaN
```

---

# Key Property of NaN

## NaN is NOT equal to anything (even itself)

```javascript
NaN === NaN // false
NaN == NaN  // false
```

This is one of the most important interview points.

---

# Checking for NaN

## isNaN()

```javascript
isNaN("hello") // true
```

⚠️ Problem:

- It performs **type coercion**
- `"hello"` → NaN → true

See:  
[[Type Conversions]]

---

## Number.isNaN()

```javascript
Number.isNaN("hello") // false
Number.isNaN(NaN)     // true
```

✅ Recommended method

- Does **not perform type coercion**
- More reliable

---

# Difference: isNaN vs Number.isNaN

|Method|Type Coercion|Reliable|
|---|---|---|
|isNaN()|Yes|No|
|Number.isNaN()|No|Yes|

---

# NaN in Comparisons

```javascript
NaN > 5   // false
NaN < 5   // false
NaN == 5  // false
```

Any comparison with `NaN` returns **false**.

---

# NaN Propagation

If `NaN` appears in a calculation, it **spreads**.

```javascript
let result = NaN + 10

console.log(result)
```

Output

```
NaN
```

Once NaN enters, it contaminates everything.

---

# Common Interview Traps

## typeof NaN

```javascript
typeof NaN
```

Output

```
"number"
```

---

## NaN comparison

```javascript
NaN === NaN // false
```

---

## isNaN behavior

```javascript
isNaN("123")   // false
isNaN("hello") // true
```

Because of **type coercion**.

---

# Mental Model

When JavaScript fails to convert something into a number:

```
Invalid Number → NaN
```

And once you get NaN:

```
NaN + anything → NaN
```

---

# Interview Summary

Important points:

- `NaN` means **invalid number**
- `typeof NaN` → `"number"`
- `NaN !== NaN`
- Use `Number.isNaN()` instead of `isNaN()`
- NaN spreads in calculations
- Often caused by **invalid type conversion**

---

# Related Concepts
JavaScript Operators

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
