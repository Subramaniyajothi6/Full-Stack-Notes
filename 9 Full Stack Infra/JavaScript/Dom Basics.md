# DOM Basics

## Definition

The Document Object Model (DOM) is a programming interface for web documents. It represents the HTML structure as a tree of objects, where each node corresponds to a part of the document.

JavaScript can use the DOM to:
- Access elements
- Modify content
- Change styles
- Respond to user actions

## Syntax

Accessing elements:

~~~javascript
document.getElementById("id")
document.getElementsByClassName("class")
document.getElementsByTagName("tag")
document.querySelector("selector")
document.querySelectorAll("selector")
~~~

## Basic Example

~~~html
<h1 id="title">Hello</h1>
~~~

~~~javascript
const element = document.getElementById("title")
console.log(element.textContent)
~~~

### Output

~~~javascript
Hello
~~~

## Additional Examples

### 1. Access Element by ID

#### Definition
Selects a single element using its unique ID.

#### Syntax

~~~javascript
document.getElementById("id")
~~~

#### Example

~~~html
<p id="text">Hi</p>
~~~

~~~javascript
const el = document.getElementById("text")
console.log(el.textContent)
~~~

#### Output

~~~javascript
Hi
~~~

#### Use Case
Used when you need a specific unique element.

---

### 2. Access Elements by Class Name

#### Definition
Selects multiple elements that share the same class.

#### Syntax

~~~javascript
document.getElementsByClassName("className")
~~~

#### Example

~~~html
<p class="item">A</p>
<p class="item">B</p>
~~~

~~~javascript
const items = document.getElementsByClassName("item")
console.log(items.length)
~~~

#### Output

~~~javascript
2
~~~

#### Use Case
Useful when handling multiple elements with the same styling or behavior.

---

### 3. querySelector

#### Definition
Selects the first element that matches a CSS selector.

#### Syntax

~~~javascript
document.querySelector("selector")
~~~

#### Example

~~~html
<div class="box">Test</div>
<div class="box">Sample</div>
~~~

~~~javascript
const el = document.querySelector(".box")
console.log(el.textContent)
~~~

#### Output

~~~javascript
Test
~~~

#### Use Case
Preferred modern method for flexible selection.

---

### 4. querySelectorAll

#### Definition
Selects all elements matching a CSS selector.

#### Syntax

~~~javascript
document.querySelectorAll("selector")
~~~

#### Example

~~~html
<li>1</li>
<li>2</li>
<li>3</li>
~~~

~~~javascript
const list = document.querySelectorAll("li")
console.log(list.length)
~~~

#### Output

~~~javascript
3
~~~

#### Use Case
Used when working with multiple elements.

---

### 5. DOM Tree Structure

#### Definition
The DOM represents HTML as a hierarchical tree of nodes.

#### Example

~~~html
<html>
  <body>
    <h1>Hello</h1>
  </body>
</html>
~~~

#### Output

~~~text
Document
 └── html
      └── body
           └── h1
~~~

#### Use Case
Understanding parent-child relationships helps in traversal and manipulation.

---

### 6. Common Element Properties

#### Definition
Once an element is selected, you can access or modify its properties.

#### Syntax

~~~javascript
element.property
~~~

#### Example

~~~html
<p id="demo">Hello</p>
~~~

~~~javascript
const el = document.getElementById("demo")

console.log(el.textContent)
el.textContent = "Updated"
~~~

#### Output

~~~javascript
Hello
~~~

#### Use Case
Used to read or update content dynamically.

---

## When to use

- When accessing or reading elements from a webpage
- When preparing to manipulate content or styles
- When handling user interactions (with events)

## When NOT to use

- When working outside the browser (e.g., Node.js)
- When direct data manipulation is enough without UI interaction

## Behavior

- DOM is created after HTML is parsed
- JavaScript can dynamically update the DOM
- `getElementsByClassName` returns a live collection
- `querySelectorAll` returns a static NodeList

→ For detailed explanation: [[DOM Manipulation]]

## Hoisting (only if applicable)

Not applicable.

## Edge Cases

### ❌ Wrong Code

~~~javascript
const el = document.getElementById("missing")
console.log(el.textContent)
~~~

### Output

~~~javascript
TypeError: Cannot read properties of null
~~~

### Why it is an edge case

If the element does not exist, it returns `null`.

### ✅ Fix

~~~javascript
const el = document.getElementById("missing")

if (el) {
  console.log(el.textContent)
}
~~~

### Output

~~~javascript
(no error)
~~~

### Why the fix works

Checks for `null` before accessing properties.

---

### ❌ Wrong Code

~~~javascript
const items = document.getElementsByClassName("item")
items.forEach(el => console.log(el))
~~~

### Output

~~~javascript
TypeError: items.forEach is not a function
~~~

### Why it is an edge case

HTMLCollection does not support array methods.

### ✅ Fix

~~~javascript
const items = document.getElementsByClassName("item")
Array.from(items).forEach(el => console.log(el))
~~~

### Output

~~~javascript
<p class="item">A</p>
<p class="item">B</p>
~~~

### Why the fix works

Converts collection into an array.

---

## Common Mistakes

### ❌ Wrong Code

~~~javascript
document.querySelectorAll(".item").style.color = "red"
~~~

### Output

~~~javascript
TypeError
~~~

### Why it is a mistake

Returns multiple elements, not a single one.

### ✅ Fix

~~~javascript
document.querySelectorAll(".item").forEach(el => {
  el.style.color = "red"
})
~~~

### Output

~~~javascript
(All elements turn red)
~~~

### Why the fix works

Applies style to each element individually.

---

### ❌ Wrong Code

~~~javascript
const el = document.getElementById("title")
console.log(el.value)
~~~

### Output

~~~javascript
undefined
~~~

### Why it is a mistake

`value` is not valid for non-input elements like `<h1>`.

### ✅ Fix

~~~javascript
const el = document.getElementById("title")
console.log(el.textContent)
~~~

### Output

~~~javascript
Hello
~~~

### Why the fix works

Uses the correct property for text-based elements.

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
