# JavaScript Prototypes

## Definition

A prototype is an object from which other objects inherit properties and methods.

In JavaScript, every object has an internal prototype link, forming a chain called the prototype chain.

---

## Syntax

There is no single "syntax" for prototypes. Different methods are used depending on the situation:

~~~javascript
// 1. Access prototype (not recommended in production)
object.__proto__

// 2. Safe way to get prototype
Object.getPrototypeOf(object)

// 3. Safe way to set prototype
Object.setPrototypeOf(object, prototype)

// 4. Best way to create object with prototype
Object.create(prototype)
~~~

---

## Basic Example

~~~javascript
const obj = {
  greet() {
    console.log("Hello")
  }
}

const user = {}

user.__proto__ = obj
user.greet()
~~~

### Output

~~~javascript
Hello
~~~

---

## Additional Examples

### Using Constructor Function

~~~javascript
function Person(name) {
  this.name = name
}

Person.prototype.greet = function () {
  console.log("Hello " + this.name)
}

const p = new Person("John")
p.greet()
~~~

### Output

~~~javascript
Hello John
~~~

---

### Prototype Chain

~~~javascript
const animal = {
  eats: true
}

const dog = {
  barks: true
}

dog.__proto__ = animal

console.log(dog.eats)
~~~

### Output

~~~javascript
true
~~~

---

### Prototype Chain Termination

~~~javascript
console.log(Object.getPrototypeOf(Object.prototype))
~~~

### Output

~~~javascript
null
~~~

---

### Class and Prototype

~~~javascript
class Person {
  greet() {
    console.log("Hello")
  }
}

const p = new Person()

console.log(Object.getPrototypeOf(p) === Person.prototype)
~~~

### Output

~~~javascript
true
~~~

---

## When to use

- When sharing methods between multiple objects  
- When understanding how inheritance works internally  
- When optimizing memory (methods are not duplicated per object)  

## When NOT to use

- Avoid manually modifying `__proto__` in production  
- Prefer `class` and `extends` for readability  
- Avoid overcomplicating simple objects  
- Avoid using `Object.setPrototypeOf()` frequently due to performance cost 

## Behavior

- Every object has an internal prototype link  
- If a property is not found on the object, JavaScript searches the prototype chain until it finds the property or reaches `null`
- Methods defined on prototype are shared across instances (not duplicated per object)  
- `class` is syntactic sugar over prototypes → [[Classes]]  
- Inheritance is implemented using prototype chaining → [[Inheritance]]  
- Prototype lookup happens at runtime (dynamic lookup)

---

## Hoisting (only if applicable)

- Prototypes themselves are not hoisted  
- Constructor functions are hoisted like normal functions  

---

## Edge Cases

### Infinite Prototype Chain

~~~javascript
const obj = {}
obj.__proto__ = obj
~~~

### Output

~~~javascript
TypeError
~~~

### Why it is an edge case

An object cannot be its own prototype.

---

### Overriding Prototype Property

~~~javascript
const animal = {
  sound: "generic"
}

const dog = {
  sound: "bark"
}

dog.__proto__ = animal

console.log(dog.sound)
~~~

### Output

~~~javascript
bark
~~~

### Why it is an edge case

Own property overrides prototype property.

---

## Common Mistakes

### ❌ Wrong Code

~~~javascript
const animal = {
  greet() {
    console.log("Hello")
  }
}

const dog = {}

dog.__proto__ = animal
~~~

### Why it is a mistake

Directly modifying `__proto__` is not recommended because it mutates the object's prototype at runtime, which can lead to performance issues and unpredictable behavior.

---

### ✅ Fix

~~~javascript
const animal = {
  greet() {
    console.log("Hello")
  }
}

const dog = Object.create(animal)
dog.greet()
~~~

### Why the fix works

`Object.create()` creates a new object with the specified prototype.

Even though `dog` does not have the `greet` method directly, it is accessed through the prototype chain.

---

### ❌ Wrong Code

~~~javascript
function Person(name) {
  this.name = name
}

const p = Person("John")
console.log(p.name)
~~~

### Output

~~~javascript
undefined
~~~

### Why it is a mistake

Constructor function is called without `new`, so no object is created and `this` does not refer to a new instance.

---

### ✅ Fix

~~~javascript
function Person(name) {
  this.name = name
}
const p = new Person("John")
console.log(p.name)
~~~

### Output

~~~javascript
John
~~~

### Why the fix works

`new` creates an object and links it to the prototype.

---

### ❌ Wrong Code

~~~javascript
function Person(name) {
  this.name = name
}

Person.prototype = {
  greet() {
    console.log("Hello")
  }
}

const p = new Person("John")
console.log(p.constructor)
~~~

### Output

~~~javascript
[Function: Object]
~~~

### Why it is a mistake

Overwriting `prototype` removes the default `constructor` reference and it falls back to `Object`.

---

### ✅ Fix

~~~javascript
function Person(name) {
  this.name = name
}

Person.prototype = {
  constructor: Person,
  greet() {
    console.log("Hello")
  }
}

const p = new Person("John")
console.log(p.constructor)
~~~

### Why the fix works

Restoring `constructor` maintains correct prototype linkage.

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
