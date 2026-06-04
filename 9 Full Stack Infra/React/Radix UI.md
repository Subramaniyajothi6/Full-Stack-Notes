---
tags: [infra, frontend, intermediate]
---

# Radix UI

> Unstyled, accessible primitives for React. The behavior layer behind [[shadcn UI]], Vercel UI, and many design systems.

## Why it matters
Building accessible Dialog, Popover, Select, and Combobox correctly is genuinely hard (focus traps, keyboard nav, ARIA). Radix gives you headless primitives that handle this, leaving styling to you.

## Core ideas
- **Headless** — zero styles, full behavior + a11y
- **Compound components** — `<Dialog.Root><Dialog.Trigger /><Dialog.Content /></Dialog.Root>`
- Per-package install: `@radix-ui/react-dialog` etc.
- Pairs naturally with Tailwind, vanilla CSS, or styled-components

## Example
```tsx
import * as Dialog from '@radix-ui/react-dialog';

<Dialog.Root>
  <Dialog.Trigger>Open</Dialog.Trigger>
  <Dialog.Portal>
    <Dialog.Overlay className="fixed inset-0 bg-black/50" />
    <Dialog.Content className="fixed inset-0 m-auto w-96 p-4 bg-white">
      <Dialog.Title>Hello</Dialog.Title>
      <Dialog.Close>x</Dialog.Close>
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

## Real World Usage
- Building design systems
- Replacing Material-UI/Chakra when you want full styling control
- Backbone of [[shadcn UI]] components

## Common Mistakes
- Forgetting `Dialog.Portal` → modal stuck inside a transformed parent
- Not setting `aria-label` / `Dialog.Title` for screen readers
- Animating `Dialog.Content` without unmount handling — use `forceMount` + AnimatePresence
- Mixing controlled and uncontrolled `open` props

## Prerequisites
- [[Components|Components]] · basic HTML/ARIA

## What To Learn Next
- [[shadcn UI]] · [[Framer Motion]]

## Best Learning Resources

### Official Documentation
- [Radix UI docs](https://www.radix-ui.com/) — primitives + colors + themes
- [Primitives reference](https://www.radix-ui.com/primitives)

### Best YouTube Resource
- [Sam Selikoff — Build UI](https://www.youtube.com/c/SamSelikoff) — many Radix examples
- [Theo — Radix vs alternatives](https://www.youtube.com/@t3dotgg)

### Best Free Course
- [Build UI — Radix recipes](https://buildui.com/recipes)

### Best Advanced Resource
- [Radix source on GitHub](https://github.com/radix-ui/primitives) — see how a11y is implemented
- [Adam Argyle on a11y patterns](https://www.youtube.com/@adamargyle)

### Best Practice Project
Build a command palette (Cmd+K) using `@radix-ui/react-dialog` + a search input. Add keyboard nav between results, ARIA roles, and animation via Framer Motion.

### Recommended Order to Learn
1. Dialog + Popover
2. Dropdown Menu + Context Menu
3. Tabs + Accordion
4. Select + Combobox patterns
5. Tooltip + Toast
6. Custom theming + Radix Colors

## Interview Questions
**Q. Why use Radix over a styled UI library?**
A. Full styling control, smaller bundles, audited a11y. Tradeoff: more design work upfront.

**Q. Why does Dialog.Portal exist?**
A. Renders the modal at the document root so transforms or `overflow:hidden` ancestors can't clip or misposition it.

**Q. How do you animate Radix Dialog enter/exit?**
A. `forceMount` + `<AnimatePresence>` (or CSS data-state attributes via `[data-state]` selectors).

## Related
- [[shadcn UI]] · [[Framer Motion]]
