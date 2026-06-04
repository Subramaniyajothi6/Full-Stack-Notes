---
tags: [infra, frontend, intermediate]
---

# shadcn UI

> Not a library — a CLI that copies styled, accessible component source files (built on [[Radix UI]] + Tailwind) into your repo. You own the code.

## Why it matters
Solves the "lock-in vs reinvention" problem. You get production-ready components but can edit them freely, adapt to your design system, and audit accessibility.

## Core ideas
- `npx shadcn@latest add button dialog dropdown-menu` — copies `.tsx` files into `components/ui/`
- Built on [[Radix UI]] primitives for behavior + a11y
- Styled with Tailwind, themable via CSS variables
- Includes blocks (full sections) and themes
- "v0.dev" + CLI generate AI-designed components from prompts

## Example
```bash
npx shadcn@latest init
npx shadcn@latest add button dialog form input
```

```tsx
import { Button } from '@/components/ui/button';
<Button variant="destructive">Delete</Button>
```

## Real World Usage
- Dashboards, SaaS internal tools
- Marketing sites combined with [[Framer Motion]]
- Accessibility-conscious shipping without rolling your own primitives

## Common Mistakes
- Treating it like a npm package — updates require running CLI again
- Heavy customization without keeping a changelog of edits
- Skipping the `cn()` utility for class merging
- Pulling many components and never reviewing them

## Prerequisites
- [[Components|Components]] · Tailwind CSS basics

## What To Learn Next
- [[Radix UI]] · [[Framer Motion]]

## Best Learning Resources

### Official Documentation
- [shadcn/ui docs](https://ui.shadcn.com/) — components, themes, blocks
- [GitHub repo](https://github.com/shadcn-ui/ui)

### Best YouTube Resource
- [Theo (t3.gg) — shadcn coverage](https://www.youtube.com/@t3dotgg)
- [Web Dev Cody — shadcn UI walkthroughs](https://www.youtube.com/@WebDevCody)

### Best Free Course
- [Theme + tooling tutorial on the docs site](https://ui.shadcn.com/docs/installation)

### Best Advanced Resource
- [Building a Design System with shadcn](https://ui.shadcn.com/docs/theming) — theming + tokens
- [v0.dev](https://v0.dev/) — generate shadcn components via prompt

### Best Practice Project
Build a polished SaaS dashboard: sidebar, command palette (Cmd+K), data table with sort/filter, dialog forms, theme toggle (dark/light). Customize Button + Input variants to match a brand.

### Recommended Order to Learn
1. Init + add a few components
2. Theming + CSS variables
3. Form + Zod + react-hook-form integration
4. Data Table component
5. Customizing component source

## Interview Questions
**Q. Why is shadcn not on npm?**
A. By design — you copy source so you control upgrades, accessibility tweaks, and styling.

**Q. What's the relationship to Radix UI?**
A. shadcn wraps Radix primitives with default Tailwind styles.

**Q. How do you upgrade shadcn components?**
A. Re-run the CLI; manually re-merge customizations. Some teams keep a "shadcn unmodified" branch for diffs.

## Related
- [[Radix UI]] · [[Framer Motion]]
