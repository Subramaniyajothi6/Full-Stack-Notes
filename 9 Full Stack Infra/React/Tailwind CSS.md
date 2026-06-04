---
tags: [react, frontend, intermediate, syntax]
---

# Tailwind CSS

> Utility-first CSS framework. Compose styles by stringing class names; the compiler purges unused ones.

## Why it took over
- Constraint system (spacing, colors, fonts come from a small scale) → consistency
- No naming things (`.header__title--large` doesn't exist)
- Production CSS is small (only used classes ship)
- Pairs beautifully with React's component model

## Setup (with Vite + React)
```bash
npm i -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```
```css
/* index.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

## Patterns
```tsx
// component
<button className="rounded-md bg-blue-600 px-4 py-2 text-white hover:bg-blue-700 focus-visible:ring-2 ring-blue-300">
  Save
</button>

// merging conditional classes
import { clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';
const cn = (...c: any[]) => twMerge(clsx(c));

<div className={cn('p-4', isError && 'bg-red-50 text-red-900', className)} />
```

## Variants
- States: `hover:`, `focus:`, `disabled:`, `aria-[expanded=true]:`, `data-[state=open]:`
- Responsive: `sm:` `md:` `lg:` `xl:` `2xl:`
- Dark mode: `dark:`
- Group/peer: `group-hover:`, `peer-checked:`

## Design system via theme
```js
// tailwind.config.js
module.exports = {
  content: ['./src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: { brand: { 50: '...', 500: '#3b82f6', 900: '...' } },
      fontFamily: { display: ['Cal Sans', 'sans-serif'] },
    },
  },
  plugins: [require('@tailwindcss/forms')],
};
```

## Real World Usage
- React component libraries ([[shadcn UI]], Tremor)
- Marketing sites
- Internal dashboards
- Email templates (with caveats; many email clients don't support modern CSS)
- Replacing CSS-in-JS for performance

## Common Mistakes
- Long, ad-hoc class strings without extracting components
- Skipping `tailwind-merge` → duplicate classes win randomly
- Putting design tokens inline instead of in `theme.extend`
- Forgetting `content` paths → utilities purged
- Fighting Tailwind for one bespoke layout when raw CSS is faster

## Prerequisites
- [[Components]] · CSS basics

## What To Learn Next
- [[shadcn UI]] · [[Radix UI]] · [[Framer Motion]]

## Best Learning Resources

### Official Documentation
- [Tailwind CSS docs](https://tailwindcss.com/docs)
- [Tailwind UI components](https://tailwindui.com/)

### Best YouTube Resource
- [Sam Selikoff — Tailwind patterns](https://www.youtube.com/c/SamSelikoff)
- [Theo — Tailwind takes](https://www.youtube.com/@t3dotgg)

### Best Free Course
- [Tailwind Components (free section)](https://tailwindcss.com/plus)
- [Refactoring UI (free chapters; Tailwind authors)](https://www.refactoringui.com/)

### Best Advanced Resource
- [Adam Wathan's blog (Tailwind creator)](https://adamwathan.me/)
- [Tailwind UI patterns](https://tailwindui.com/components)

### Best Practice Project
Rebuild a marketing landing page with Tailwind. Define a brand-scaled `colors`, custom `fontFamily`, dark mode toggle. Extract reusable component variants with [[shadcn UI]].

### Recommended Order to Learn
1. Utility classes + spacing scale
2. Responsive + state variants
3. `clsx` + `tailwind-merge` for conditional classes
4. Theme customization
5. Plugins (forms, typography, container queries)
6. Building a design system with shadcn

## Interview Questions
**Q. Why utility-first instead of semantic classes?**
A. Consistency from a constrained scale, instant context-switching, no naming overhead, smaller final CSS. Trades verbosity in JSX for less indirection.

**Q. Does the bundle grow with usage?**
A. No — the compiler only emits CSS for classes you actually use (`content` config drives the scan).

## Related
- [[shadcn UI]] · [[Radix UI]] · [[Framer Motion]] · [[Components]]
