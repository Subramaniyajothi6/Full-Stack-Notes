---
tags: [infra, devenv, beginner]
---

# Browser DevTools

> Built-in toolkit for inspecting, debugging, and profiling web apps.

## Why it matters
You'll spend more time in DevTools than in your editor. Mastery turns hour-long bugs into 5-minute fixes.

## Core panels
- **Elements** — DOM tree, computed styles, accessibility tree, force pseudo-states
- **Console** — `$0`–`$4` last selected nodes, `$$('css')` querySelectorAll, `console.table`, `monitor()`
- **Network** — waterfall, throttling, copy as fetch/curl, HAR export
- **Performance** — flamegraphs, long tasks, layout shifts
- **Memory** — heap snapshots, allocation timeline
- **Application** — storage, service workers, manifest
- **Sources** — breakpoints (line, conditional, logpoints, DOM, XHR)

## Power features
- `Cmd+Shift+P` (Ctrl+Shift+P) — command palette
- "Show coverage" — find unused JS/CSS
- Local overrides — edit prod assets, persist locally
- Workspaces — map sources to local repo
- Lighthouse — perf/accessibility audits

## Real World Usage
- Debugging slow requests via Network waterfall
- Tracking memory leaks with 3-snapshot pattern (record → action → record → action → record)
- Reproducing prod-only bugs by editing live with overrides
- Auditing accessibility with the a11y tab

## Common Mistakes
- Using `console.log` when `console.table`/`console.dir` is clearer
- Profiling with extensions enabled (use Incognito or guest profile)
- Forgetting "Disable cache" while devtools open (it only applies then)
- Not preserving log/network across navigation

## Prerequisites
- [[Browser Internals]]

## What To Learn Next
- [[Performance Optimization|React Performance]] · [[CLI]]

## Best Learning Resources

### Official Documentation
- [Chrome DevTools docs](https://developer.chrome.com/docs/devtools) — official, frequently updated
- [Firefox DevTools docs](https://firefox-source-docs.mozilla.org/devtools-user/)

### Best YouTube Resource
- [Umar Hansa — DevTools Tips](https://www.youtube.com/c/UmarHansa) — micro-tips from a former DevTools engineer
- [Web Dev Simplified — DevTools](https://www.youtube.com/c/WebDevSimplified) — beginner-friendly walk-throughs

### Best Free Course
- [DevTools tips on web.dev](https://web.dev/explore/devtools) — short, practical articles

### Best Advanced Resource
- [Chrome DevTools — Performance reference](https://developer.chrome.com/docs/devtools/performance/reference) — every flamegraph row explained

### Best Practice Project
Take a slow demo site (or your own), run a Lighthouse audit, and document each improvement: image format, JS bundle splitting, layout-shift fixes. Share before/after metrics.

### Recommended Order to Learn
1. Elements + Console basics
2. Network panel + throttling
3. Sources + breakpoints
4. Performance + flamegraph reading
5. Memory snapshots
6. Lighthouse + Coverage

## Interview Questions
**Q. How do you find a memory leak?**
A. Three-snapshot pattern in Memory panel. Look for "Detached" DOM and growing closures.

**Q. How do you simulate a slow network?**
A. Network panel → throttling presets (Slow 3G) or custom profile.

**Q. What's the difference between recording in Performance vs Lighthouse?**
A. Performance is a manual flamegraph for one interaction. Lighthouse runs an automated multi-metric audit.

## Related
- [[Browser Internals]] · [[React Testing|React Testing]]
