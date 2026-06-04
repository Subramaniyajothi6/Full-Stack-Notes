# JavaScript Static Methods

## Definition

Static methods are methods that belong to the class itself, not to instances of the class.

They are called directly on the class, not on objects created from the class.

---

## Syntax

~~~javascript
class ClassName {
  static methodName() {
    // logic
  }
}
~~~

---

## Basic Example

~~~javascript
class MathUtils {
  static add(a, b) {
    return a + b
  }
}

console.log(MathUtils.add(2, 3))
~~~

### Output

~~~javascript
5
~~~

---

## Additional Examples

### Static vs Instance Method

~~~javascript
class User {
  constructor(name) {
    this.name = name
  }

  greet() {
    console.log("Hello " + this.name)
  }

  static info() {
    console.log("This is a User class")
  }
}

const u = new User("John")

u.greet()        // instance method
User.info()      // static method
~~~

### Output

~~~javascript
Hello John
This is a User class
~~~

---

### Utility Method

~~~javascript
class Calculator {
  static square(n) {
    return n * n
  }
}

console.log(Calculator.square(4))
~~~

### Output

~~~javascript
16
~~~

---

### Static Method Calling Another Static Method

~~~javascript
class MathUtils {
  static add(a, b) {
    return a + b
  }

  static double(n) {
    return this.add(n, n)
  }
}

console.log(MathUtils.double(5))
~~~

### Output

~~~javascript
10
~~~

---

## When to use

- When functionality does not depend on instance data  
- When creating utility/helper methods  
- When grouping related functions inside a class  

---

## When NOT to use

- When the method needs access to instance properties (`this.name`, etc.)  
- When behavior depends on object-specific data  

---

## Behavior

- Static methods belong to the class, not the instance  
- Cannot be accessed using object instances  
- Accessed using `ClassName.method()`  
- Inside static methods, `this` refers to the class itself  
- Static methods are not available on the prototype of instances  

---

## Hoisting (only if applicable)

- Static methods follow class hoisting rules  
- Class is hoisted but not initialized (TDZ applies)  

~~~javascript
MathUtils.add(2, 3) // ❌ Error

class MathUtils {
  static add(a, b) {
    return a + b
  }
}
~~~

---

## Edge Cases

### Calling Static Method from Instance

~~~javascript
class Test {
  static greet() {
    console.log("Hello")
  }
}

const t = new Test()
t.greet()
~~~

### Output

~~~javascript
TypeError
~~~

### Why it is an edge case

Static methods are not available on instances.

---

### Accessing Instance Data Inside Static Method

~~~javascript
class User {
  constructor(name) {
    this.name = name
  }

  static greet() {
    console.log("Hello " + this.name)
  }
}

User.greet()
~~~

### Output

~~~javascript
Hello undefined
~~~

### Why it is an edge case

`this` refers to the class, not an instance. Since no instance is created, `this.name` is `undefined`.

---

## Common Mistakes

### ❌ Wrong Code

~~~javascript
class Test {
  static greet() {
    console.log("Hello")
  }
}

const t = new Test()
t.greet()
~~~

### Output

~~~javascript
TypeError
~~~

### Why it is a mistake

Static methods are not available on instances.

---

### ✅ Fix

~~~javascript
class Test {
  static greet() {
    console.log("Hello")
  }
}

Test.greet()
~~~

### Output

~~~javascript
Hello
~~~

### Why the fix works

Static methods belong to the class and do not require creating an instance.

---

### ❌ Wrong Code

~~~javascript
class MathUtils {
  add(a, b) {
    return a + b
  }
}

console.log(MathUtils.add(2, 3))
~~~

### Output

~~~javascript
TypeError
~~~

### Why it is a mistake

The method is defined as an instance method but is being called on the class.

Instance methods require creating an object using `new`, while static methods can be called directly on the class.

we are neither:  
- creating an instance using `new`  
- nor defining the method as `static`  
  
so calling it on the class results in a TypeError.

### ✅ Fix

~~~javascript
class MathUtils {
  static add(a, b) {
    return a + b
  }
}

console.log(MathUtils.add(2, 3))
~~~

### Output

~~~javascript
5
~~~

### Why the fix works

Adding `static` allows the method to be called on the class.

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
