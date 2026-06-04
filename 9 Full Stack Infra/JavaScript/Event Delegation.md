# Event Delegation

## Definition

Event Delegation is a technique in JavaScript where a single event listener is attached to a parent element to handle events for its child elements.

It works using event propagation (bubbling), where events triggered on child elements bubble up to the parent.

## Syntax

~~~javascript
parent.addEventListener("event", (e) => {
  if (e.target.matches("selector")) {
    // logic
  }
})
~~~

## Basic Example

~~~html
<ul id="list">
  <li>Item 1</li>
  <li>Item 2</li>
</ul>
~~~

~~~javascript
const list = document.getElementById("list")

list.addEventListener("click", (e) => {
  if (e.target.tagName === "LI") {
    console.log(e.target.textContent)
  }
})
~~~

### Output

~~~javascript
Item 1 / Item 2 (depending on click)
~~~

## Additional Examples

### 1. Handling Dynamic Elements

#### Definition
Handles events for elements added after page load.

#### Syntax

~~~javascript
parent.addEventListener("event", handler)
~~~

#### Example

~~~html
<ul id="list"></ul>
~~~

~~~javascript
const list = document.getElementById("list")

list.addEventListener("click", (e) => {
  if (e.target.tagName === "LI") {
    console.log(e.target.textContent)
  }
})

// dynamically adding element
const li = document.createElement("li")
li.textContent = "New Item"
list.appendChild(li)
~~~

#### Output

~~~javascript
New Item (when clicked)
~~~

#### Use Case
Used when elements are created dynamically.

---

### 2. Using matches()

#### Definition
Checks if the clicked element matches a CSS selector.

#### Syntax

~~~javascript
e.target.matches("selector")
~~~

#### Example

~~~html
<div id="container">
  <button class="btn">Click</button>
</div>
~~~

~~~javascript
const container = document.getElementById("container")

container.addEventListener("click", (e) => {
  if (e.target.matches(".btn")) {
    console.log("Button clicked")
  }
})
~~~

#### Output

~~~javascript
Button clicked
~~~

#### Use Case
Cleaner way to filter target elements.

---

### 3. Handling Multiple Child Types

#### Definition
Handles different child elements using conditions.

#### Example

~~~javascript
container.addEventListener("click", (e) => {
  if (e.target.matches(".btn")) {
    console.log("Button")
  } else if (e.target.matches(".link")) {
    console.log("Link")
  }
})
~~~

#### Output

~~~javascript
Button / Link
~~~

#### Use Case
Used when multiple child elements require different actions.

---

## When to use

- When handling many child elements efficiently
- When elements are dynamically added
- To reduce multiple event listeners

## When NOT to use

- When only a single element needs an event
- When event does not bubble

## Behavior

- Uses event bubbling
- Event starts from target and moves up to parent
- `e.target` gives actual clicked element
- Improves performance by reducing listeners

→ For detailed explanation: [[Event Handling]]

## Hoisting (only if applicable)

Not applicable.

## Edge Cases

### ❌ Wrong Code

~~~javascript
list.addEventListener("click", (e) => {
  console.log(e.currentTarget.textContent)
})
~~~

### Output

~~~javascript
(All list content)
~~~

### Why it is an edge case

`currentTarget` refers to the parent, not the clicked element.

### ✅ Fix

~~~javascript
list.addEventListener("click", (e) => {
  console.log(e.target.textContent)
})
~~~

### Output

~~~javascript
Clicked item text
~~~

### Why the fix works

`target` refers to the actual clicked element.

---

### ❌ Wrong Code

~~~javascript
list.addEventListener("click", (e) => {
  if (e.target.tagName === "ul") {
    console.log("Clicked")
  }
})
~~~

### Output

~~~javascript
(No output)
~~~

### Why it is an edge case

Event target is usually the child element, not the parent.

### ✅ Fix

~~~javascript
list.addEventListener("click", (e) => {
  if (e.target.tagName === "LI") {
    console.log("Clicked")
  }
})
~~~

### Output

~~~javascript
Clicked
~~~

### Why the fix works

Checks the correct target element.

---

## Common Mistakes

### ❌ Wrong Code

~~~javascript
const items = document.querySelectorAll("li")

items.forEach(item => {
  item.addEventListener("click", () => {
    console.log("Clicked")
  })
})
~~~

### Output

~~~javascript
Works, but inefficient
~~~

### Why it is a mistake

Adds multiple listeners instead of one parent listener.

### ✅ Fix

~~~javascript
const list = document.getElementById("list")

list.addEventListener("click", (e) => {
  if (e.target.tagName === "LI") {
    console.log("Clicked")
  }
})
~~~

### Output

~~~javascript
Clicked
~~~

### Why the fix works

Uses a single listener for all child elements.

---

### ❌ Wrong Code

~~~javascript
list.addEventListener("click", (e) => {
  console.log(e.target)
})
~~~

### Output

~~~javascript
May log unwanted elements
~~~

### Why it is a mistake

Does not filter the target element.

### ✅ Fix

~~~javascript
list.addEventListener("click", (e) => {
  if (e.target.matches("li")) {
    console.log(e.target)
  }
})
~~~

### Output

~~~javascript
Only li elements logged
~~~

### Why the fix works

Ensures only intended elements are handled.

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
