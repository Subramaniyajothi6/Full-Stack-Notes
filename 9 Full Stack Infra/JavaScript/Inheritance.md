# JavaScript Inheritance

## Definition

Inheritance allows one class (child) to acquire properties and methods from another class (parent).

It enables code reuse and helps create a hierarchical relationship between classes.

---

## Syntax

~~~javascript
class Parent {
  constructor() {}
}

class Child extends Parent {
  constructor() {
    super()
  }
}
~~~

---

## Basic Example

~~~javascript
class Animal {
  constructor(name) {
    this.name = name
  }

  speak() {
    console.log(this.name + " makes a sound")
  }
}

class Dog extends Animal {}

const d = new Dog("Tom")
d.speak()
~~~

### Output

~~~javascript
Tom makes a sound
~~~

---

## Additional Examples

### Method Overriding

~~~javascript
class Animal {
  speak() {
    console.log("Animal sound")
  }
}

class Dog extends Animal {
  speak() {
    console.log("Dog barks")
  }
}

const d = new Dog()
d.speak()
~~~

### Output

~~~javascript
Dog barks
~~~

---

### Using `super` in Methods

~~~javascript
class Animal {
  speak() {
    console.log("Animal sound")
  }
}

class Dog extends Animal {
  speak() {
    super.speak()
    console.log("Dog barks")
  }
}

const d = new Dog()
d.speak()
~~~

### Output

~~~javascript
Animal sound
Dog barks
~~~

---

### Using `super` in Constructor

~~~javascript
class Animal {
  constructor(name) {
    this.name = name
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name)
    this.breed = breed
  }
}

const d = new Dog("Tom", "Labrador")
console.log(d)
~~~

### Output

~~~javascript
Dog { name: "Tom", breed: "Labrador" }
~~~

---

## When to use

- When multiple classes share common properties or methods  
- When building hierarchical relationships  
- When extending functionality of existing classes  

---

## When NOT to use

- When composition is more suitable (has-a relationship)  
- When it creates unnecessary complexity  
- When classes are unrelated  

---

## Behavior

- Child class uses `extends` to inherit from parent  
- `super()` must be called before using `this` in constructor  
- Child class can override parent methods  
- `this` refers to the child instance → [[this keyword]]  
- Inheritance works on top of prototypes → [[Prototypes]]

---

## Hoisting (only if applicable)

- Classes are hoisted but not initialized  
- They exist in the Temporal Dead Zone (TDZ)  
- Cannot be used before declaration  

~~~javascript
const d = new Dog() // ❌ Error

class Animal {}
class Dog extends Animal {}
~~~

---

## Edge Cases

### Using `this` before `super`

~~~javascript
class Animal {
  constructor(name) {
    this.name = name
  }
}

class Dog extends Animal {
  constructor(name) {
    this.name = name
  }
}

const d = new Dog("Tom")
~~~

### Output

~~~javascript
ReferenceError: Must call super constructor before using 'this'
~~~

### Why it is an edge case

In derived classes, `super()` must be called before accessing `this`.

---

### Fix

~~~javascript
class Dog extends Animal {
  constructor(name) {
    super(name)
  }
}
~~~

### Output

~~~javascript
Dog { name: "Tom" }
~~~

### Why the fix works

`super()` initializes the parent class before using `this`.

---

## Common Mistakes

### ❌ Wrong Code

~~~javascript
class Animal {
  speak() {
    console.log("Animal sound")
  }
}

class Dog extends Animal {}

const d = new Dog()
d.speak = function () {
  console.log("Dog barks")
}
d.speak()
~~~

### Why it is a mistake

Overriding method on instance instead of class breaks inheritance design.

---

### ✅ Fix

~~~javascript

class Animal {
  speak() {
    console.log("Animal sound")
  }
}

class Dog extends Animal {
  speak() {
    console.log("Dog barks")
  }
}

const d = new Dog()
d.speak()

~~~

### Why the fix works

Method overriding should be done in class, not per instance.


---

### ❌ Wrong Code

~~~javascript
class Animal {
  constructor(name) {
    this.name = name
  }
}

class Dog extends Animal {
  constructor(name) {
    super()
  }
}

const d = new Dog("Tom")
console.log(d.name)
~~~

### Output

~~~javascript
undefined
~~~

### Why it is a mistake

Argument is not passed to `super()`.

---

### ✅ Fix

~~~javascript
class Dog extends Animal {
  constructor(name) {
    super(name)
  }
}
~~~

### Output

~~~javascript
Tom
~~~

### Why the fix works

Passing arguments ensures parent properties are initialized correctly.

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
