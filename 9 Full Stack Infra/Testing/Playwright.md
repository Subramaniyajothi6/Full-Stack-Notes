---
tags: [infra, testing, intermediate]
---

# Playwright

> Microsoft's modern E2E framework. One API across Chromium, Firefox, WebKit. Fast, reliable, batteries-included.

## Why it matters
Best-in-class for cross-browser E2E. Auto-waits, traces, codegen, parallel sharding, and a polished VS Code extension.

## Core features
- Multiple browser engines + projects (configure per browser)
- Auto-wait on locators (no `sleep`)
- Tracing → playwright trace viewer for replays
- `codegen` to record interactions
- `--ui` watch mode
- Network mocking + auth state reuse
- Component testing for React/Svelte/Vue

## Setup
```bash
npm init playwright@latest
```

## Example
```ts
import { test, expect } from '@playwright/test';

test('home loads', async ({ page }) => {
  await page.goto('/');
  await expect(page.getByRole('heading', { name: /welcome/i })).toBeVisible();
});

test.use({ viewport: { width: 375, height: 667 } });
```

## Real World Usage
- Smoke suite gating PRs
- Cross-browser regression
- Visual regression with `toHaveScreenshot`
- Auth flow tests with `storageState` reuse
- Mobile emulation

## Common Mistakes
- CSS selectors with hashed classnames → brittle
- Asserting too much per test → slow + flaky
- Running against shared environments → race conditions
- Not uploading traces in CI → blind debugging
- Forgetting `npm run dev` style web server setup in `playwright.config`

## Prerequisites
- [[E2E Testing]] · [[CI CD]]

## What To Learn Next
- [[Puppeteer]] · [[TestSprite]]

## Best Learning Resources

### Official Documentation
- [Playwright Docs](https://playwright.dev/) — comprehensive, current
- [Playwright VS Code extension](https://playwright.dev/docs/getting-started-vscode)

### Best YouTube Resource
- [Playwright (official channel)](https://www.youtube.com/c/Playwrightdev)
- [Stefan Judis — Playwright tips](https://www.youtube.com/c/StefanJudis)

### Best Free Course
- [Playwright Learn](https://playwright.dev/docs/intro) — official walkthrough

### Best Advanced Resource
- [Microsoft Playwright Roadmap blog](https://playwright.dev/blog) — releases + patterns
- [Test Automation University — Playwright](https://testautomationu.applitools.com/playwright/)

### Best Practice Project
Add a 10-test suite covering key user journeys. Configure 3 projects (chromium, firefox, webkit). Add visual regression on the home + dashboard. Run on PR with sharding (4 workers) and trace upload artifacts.

### Recommended Order to Learn
1. Locators + auto-wait
2. Fixtures (authenticated user)
3. Network mocking
4. Tracing + debugging
5. Visual regression
6. Component testing mode

## Interview Questions
**Q. Why does Playwright auto-wait?**
A. Locators are evaluated lazily and retried until actionable — eliminates most `wait` boilerplate that plagues older tools.

**Q. Page vs Browser context?**
A. Browser is one engine instance; Context = isolated profile (cookies, storage); Page = tab. Use one context per test for isolation.

**Q. How do you reuse login?**
A. `storageState` — save cookies/local storage once and reuse across tests via `test.use({ storageState })`.

## Related
- [[E2E Testing]] · [[Puppeteer]] · [[CI CD]]
