# Event Handling

## Definition

Event Handling in JavaScript allows you to execute code in response to user actions such as clicks, key presses, mouse movements, or form submissions.

An event is an action that occurs in the browser, and an event handler is a function that runs when that event occurs.

## Syntax

~~~javascript
element.addEventListener("event", callback)
~~~

Inline (not recommended):

~~~html
<button onclick="handleClick()">Click</button>
~~~

## Basic Example

~~~html
<button id="btn">Click Me</button>
~~~

~~~javascript
const btn = document.getElementById("btn")

btn.addEventListener("click", () => {
  console.log("Button clicked")
})
~~~

### Output

~~~javascript
Button clicked
~~~

## Additional Examples

### 1. Click Event

#### Definition
Executes a function when an element is clicked.

#### Syntax

~~~javascript
element.addEventListener("click", callback)
~~~

#### Example

~~~javascript
btn.addEventListener("click", () => {
  console.log("Clicked")
})
~~~

#### Output

~~~javascript
Clicked
~~~

#### Use Case
Used for buttons, links, and user interactions.

---

### 2. Input Event

#### Definition
Triggers when the value of an input field changes.

#### Syntax

~~~javascript
element.addEventListener("input", callback)
~~~

#### Example

~~~html
<input id="name">
~~~

~~~javascript
const input = document.getElementById("name")

input.addEventListener("input", (e) => {
  console.log(e.target.value)
})
~~~

#### Output

~~~javascript
(User typed value)
~~~

#### Use Case
Used for live search, validation, etc.

---

### 3. Event Object

#### Definition
An object automatically passed to the event handler containing details about the event.

#### Syntax

~~~javascript
element.addEventListener("event", (event) => {})
~~~

#### Example

~~~javascript
btn.addEventListener("click", (e) => {
  console.log(e.type)
})
~~~

#### Output

~~~javascript
click
~~~

#### Use Case
Used to get event details like type, target, coordinates, etc.

---

### 4. Multiple Events on Same Element

#### Definition
Attach multiple event listeners to a single element.

#### Example

~~~javascript
btn.addEventListener("click", () => console.log("Click"))
btn.addEventListener("mouseover", () => console.log("Hover"))
~~~

#### Output

~~~javascript
Click  
Hover
~~~

#### Use Case
Used for handling different interactions on the same element.

---

### 5. Removing Event Listener

#### Definition
Removes an attached event listener.

#### Syntax

~~~javascript
element.removeEventListener("event", callback)
~~~

#### Example

~~~javascript
function handleClick() {
  console.log("Clicked")
}

btn.addEventListener("click", handleClick)
btn.removeEventListener("click", handleClick)
~~~

#### Output

~~~javascript
(No output after removal)
~~~

#### Use Case
Used to prevent repeated or unnecessary event handling.

---

## When to use

- Handling user interactions
- Building interactive UI
- Triggering actions based on events

## When NOT to use

- When no user interaction is needed
- When logic is purely data-based
%% there should be difference where normal event and passing a event in the callback as argument in callback function  %%
## Behavior

- Events propagate through the DOM (bubbling by default)
- Event listeners can be added multiple times
- Callback executes when event occurs

→ For detailed explanation: [[Event Delegation]]

## Hoisting (only if applicable)

Not applicable.

## Edge Cases

### ❌ Wrong Code

~~~javascript
btn.addEventListener("click", handleClick())
~~~

### Output

~~~javascript
Function executes immediately
~~~

### Why it is an edge case

The function is called instead of being passed as a reference.

### ✅ Fix

~~~javascript
btn.addEventListener("click", handleClick)
~~~

### Output

~~~javascript
Executes on click
~~~

### Why the fix works

Passes function reference instead of calling it.

---

### ❌ Wrong Code

~~~javascript
btn.addEventListener("click", () => {
  console.log("Clicked")
})

btn.removeEventListener("click", () => {
  console.log("Clicked")
})
~~~

### Output

~~~javascript
Listener not removed
~~~

### Why it is an edge case

Even though the functions look identical, they are different references in memory.

### ✅ Fix

~~~javascript
function handleClick() {
  console.log("Clicked")
}

btn.addEventListener("click", handleClick)
btn.removeEventListener("click", handleClick)
~~~

### Output

~~~javascript
Listener removed successfully
~~~

### Why the fix works

Uses the same function reference for both adding and removing.

---

## Common Mistakes

### ❌ Wrong Code

~~~javascript
const btn = document.getElementById("btn")

btn.onclick = () => console.log("One")
btn.onclick = () => console.log("Two")
~~~

### Output

~~~javascript
Two
~~~

### Why it is a mistake

`onclick` is a property, not a method. Assigning a new function overrides the previous one.

### ✅ Fix

~~~javascript
const btn = document.getElementById("btn")

btn.addEventListener("click", () => console.log("One"))
btn.addEventListener("click", () => console.log("Two"))
~~~

### Output

~~~javascript
One  
Two
~~~

### Why the fix works

Allows multiple event listeners instead of overwriting.

---

### ❌ Wrong Code

~~~javascript
document.getElementById("btn").addEventListener("click", () => {
  console.log("Clicked")
})
~~~

### Output

~~~javascript
TypeError if element not found
~~~

### Why it is a mistake

Element may not exist when the script runs.

### ✅ Fix

~~~javascript
document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("btn")
  btn.addEventListener("click", () => {
    console.log("Clicked")
  })
})
~~~

### Output

~~~javascript
Clicked
~~~

### Why the fix works

Ensures DOM is fully loaded before accessing elements.

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
