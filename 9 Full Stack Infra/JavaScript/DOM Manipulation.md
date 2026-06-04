# DOM Manipulation

## Definition

DOM Manipulation refers to modifying the structure, content, or style of HTML elements using JavaScript.

It allows dynamic updates to the webpage without reloading.

## Syntax

Common operations:

~~~javascript
element.textContent = "text"
element.innerHTML = "<b>text</b>"
element.style.property = "value"
element.setAttribute("attr", "value")
element.classList.add("class")
element.classList.remove("class")
~~~

## Basic Example

~~~html
<p id="demo">Hello</p>
~~~

~~~javascript
const el = document.getElementById("demo")
el.textContent = "Updated"
~~~

### Output

~~~javascript
Updated
~~~

## Additional Examples

### 1. Changing Text Content

#### Definition
Updates the text inside an element.

#### Syntax

~~~javascript
element.textContent = "new text"
~~~

#### Example

~~~html
<p id="text">Hi</p>
~~~

~~~javascript
const el = document.getElementById("text")
el.textContent = "Hello World"
~~~

#### Output

~~~javascript
Hello World
~~~

#### Use Case
Used to safely update text without interpreting HTML.

---

### 2. Using innerHTML

#### Definition
Updates content including HTML tags.

#### Syntax

~~~javascript
element.innerHTML = "HTML string"
~~~

#### Example

~~~html
<div id="box"></div>
~~~

~~~javascript
const el = document.getElementById("box")
el.innerHTML = "<b>Bold Text</b>"
~~~

#### Output

~~~javascript
Bold Text (rendered as bold)
~~~

#### Use Case
Used when inserting HTML structure dynamically.

---

### 3. Changing Styles

#### Definition
Modifies CSS styles of an element.

#### Syntax

~~~javascript
element.style.property = "value"
~~~

#### Example

~~~html
<p id="para">Text</p>
~~~

~~~javascript
const el = document.getElementById("para")
el.style.color = "red"
~~~

#### Output

~~~javascript
(Text becomes red)
~~~

#### Use Case
Used for dynamic styling based on conditions.

---

### 4. Working with Classes

#### Definition
Adds, removes, or toggles CSS classes.

#### Syntax

~~~javascript
element.classList.add("class")
element.classList.remove("class")
element.classList.toggle("class")
~~~

#### Example

~~~html
<p id="item">Text</p>
~~~

~~~javascript
const el = document.getElementById("item")
el.classList.add("active")
~~~

#### Output

~~~javascript
<p class="active">Text</p>
~~~

#### Use Case
Used for applying styles or states (e.g., active, hidden).

---

### 5. setAttribute & getAttribute

#### Definition
Sets or retrieves attributes of an element.

#### Syntax

~~~javascript
element.setAttribute("name", "value")
element.getAttribute("name")
~~~

#### Example

~~~html
<img id="img">
~~~

~~~javascript
const el = document.getElementById("img")
el.setAttribute("src", "image.png")
console.log(el.getAttribute("src"))
~~~

#### Output

~~~javascript
image.png
~~~

#### Use Case
Used to dynamically control attributes like src, href.

---

### 6. Creating & Appending Elements

#### Definition
Creates new elements and adds them to the DOM.

#### Syntax

~~~javascript
document.createElement("tag")
parent.appendChild(child)
~~~

#### Example

~~~html
<ul id="list"></ul>
~~~

~~~javascript
const li = document.createElement("li")
li.textContent = "Item"

const list = document.getElementById("list")
list.appendChild(li)
~~~

#### Output

~~~javascript
<li>Item</li> added inside <ul>
~~~

#### Use Case
Used when dynamically generating UI elements.

---

## When to use

- Updating UI dynamically
- Changing styles based on user interaction
- Adding/removing elements
- Building interactive applications

## When NOT to use

- When static HTML is sufficient
- When logic does not affect UI
- When overusing causes performance issues

## Behavior

- Changes reflect immediately in the browser
- `textContent` is safe (no HTML parsing)
- `innerHTML` parses HTML (can overwrite children)
- `classList` is efficient for class handling

→ For detailed explanation: [[Event Handling]]

## Hoisting (only if applicable)

Not applicable.

## Edge Cases

### ❌ Wrong Code

~~~javascript
const el = document.getElementById("box")
el.innerHTML += "<p>New</p>"
~~~

### Output

~~~javascript
(Re-renders content)
~~~

### Why it is an edge case

Using `innerHTML +=` re-parses entire content, which can remove event listeners.

### ✅ Fix

~~~javascript
const p = document.createElement("p")
p.textContent = "New"

document.getElementById("box").appendChild(p)
~~~

### Output

~~~javascript
(New element added safely)
~~~

### Why the fix works

Avoids re-rendering existing DOM.

---

### ❌ Wrong Code

~~~javascript
el.style.background-color = "red"
~~~

### Output

~~~javascript
SyntaxError
~~~

### Why it is an edge case

CSS properties with hyphens must be camelCase in JavaScript.

### ✅ Fix

~~~javascript
el.style.backgroundColor = "red"
~~~

### Output

~~~javascript
(Background becomes red)
~~~

### Why the fix works

Uses correct JavaScript property naming.

---

## Common Mistakes

### ❌ Wrong Code

~~~javascript
const el = document.getElementById("demo")
el.innerHTML = el.innerHTML + "<p>Test</p>"
~~~

### Output

~~~javascript
(Content replaced and re-rendered)
~~~

### Why it is a mistake

Inefficient and may remove existing event listeners.

### ✅ Fix

~~~javascript
const p = document.createElement("p")
p.textContent = "Test"
el.appendChild(p)
~~~

### Output

~~~javascript
(Appends without re-rendering existing nodes)
~~~

### Why the fix works

Uses DOM methods instead of string manipulation.

---

### ❌ Wrong Code

~~~javascript
el.className = "active"
~~~

### Output

~~~javascript
(Existing classes removed)
~~~

### Why it is a mistake

Overrides all existing classes.

### ✅ Fix

~~~javascript
el.classList.add("active")
~~~

### Output

~~~javascript
(Class added without removing others)
~~~

### Why the fix works

Preserves existing class list.

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
