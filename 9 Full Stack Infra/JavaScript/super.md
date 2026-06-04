# JavaScript super Keyword

## Definition

The `super` keyword is used to access properties and methods of a parent (base) class.

It is mainly used in child classes that extend a parent class.

---

## Syntax

~~~javascript
class Parent {
  constructor() {}
  method() {}
}

class Child extends Parent {
  constructor() {
    super()
  }

  method() {
    super.method()
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

class Dog extends Animal {
  constructor(name) {
    super(name)
  }

  speak() {
    super.speak()
    console.log(this.name + " barks")
  }
}

const d = new Dog("Tom")
d.speak()
~~~

### Output

~~~javascript
Tom makes a sound
Tom barks
~~~

---

## Additional Examples

### Using super() in Constructor

~~~javascript
class Person {
  constructor(name) {
    this.name = name
  }
}

class Student extends Person {
  constructor(name, course) {
    super(name)
    this.course = course
  }
}

const s = new Student("John", "CS")
console.log(s.name, s.course)
~~~

### Output

~~~javascript
John CS
~~~

---

### Calling Parent Method

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

## When to use

- When extending a class using `extends`  
- When calling parent constructor  
- When reusing parent methods inside child class  

---

## When NOT to use

- When there is no inheritance (`extends`)  
- In regular functions or non-class context  

---

## Behavior

- `super()` calls the parent class constructor  
- Must be called before using `this` in child constructor  
- `super.method()` calls a method from the parent class  
- Works only inside classes that use `extends`  
- `super` refers to the prototype of the parent class  

---

## Hoisting (only if applicable)

- `super` follows class rules  
- Cannot be used before `super()` is called in constructor  

---

## Edge Cases

### Using `this` before `super()`

~~~javascript
class Parent {
  constructor() {
    this.name = "Parent"
  }
}

class Child extends Parent {
  constructor() {
    this.age = 10
    super()
  }
}

const c = new Child()
~~~

### Output

~~~javascript
ReferenceError
~~~

### Why it is an edge case

`this` cannot be used before calling `super()` in a child constructor.

---

### Using super without extends

~~~javascript
class A {}

class B {
  constructor() {
    super()
  }
}
~~~

### Output

~~~javascript
SyntaxError
~~~

### Why it is an edge case

`super` can only be used in classes that extend another class.

---

## Common Mistakes

### ❌ Wrong Code

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
ReferenceError
~~~

### Why it is a mistake

`super()` is not called before using `this`.

---

### ✅ Fix

~~~javascript
class Animal {
  constructor(name) {
    this.name = name
  }
}

class Dog extends Animal {
  constructor(name) {
    super(name)
  }
}

const d = new Dog("Tom")
console.log(d.name)
~~~

### Output

~~~javascript
Tom
~~~

### Why the fix works

`super()` initializes the parent class before using `this`.

---

### ❌ Wrong Code

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

### Why it is a mistake

Parent method is completely overridden and not reused.

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

### Why the fix works

`super.method()` allows reuse of parent behavior instead of replacing it completely.

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
