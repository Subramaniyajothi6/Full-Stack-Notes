---
tags: [infra, testing, intermediate]
---

# E2E Testing

> End-to-end: drive the real app through a browser, asserting user-visible behavior.

## Why it matters
Catches integration issues across frontend, backend, network, and infra. The closest automated test to "did the user actually have a good experience?"

## Tools
- **Playwright** — modern, multi-browser, built-in tracing — see [[Playwright]]
- **Cypress** — popular but iframe-based, single-tab limits
- **Puppeteer** — Chrome-only, scripting-focused — see [[Puppeteer]]
- **WebdriverIO / Selenium** — older, broader

## Example (Playwright)
```ts
import { test, expect } from '@playwright/test';

test('sign up + post', async ({ page }) => {
  await page.goto('/signup');
  await page.fill('[name=email]', 'a@b.c');
  await page.fill('[name=password]', 'pw1234');
  await page.click('button[type=submit]');
  await expect(page).toHaveURL('/dashboard');

  await page.click('text=New post');
  await page.fill('textarea', 'Hello');
  await page.click('text=Publish');
  await expect(page.locator('article')).toContainText('Hello');
});
```

## Real World Usage
- Smoke suite running on every PR (top 5 user journeys)
- Pre-release "happy path" coverage
- Visual regression (Playwright + screenshots)
- Cross-browser checks (Playwright projects)

## Common Mistakes
- Too many E2E tests → slow, flaky, expensive (test pyramid)
- Brittle locators (`.css-x123abc`) — use `getByRole`/`data-testid`
- No video/trace artifacts → debugging blind
- Running against shared staging during CI runs (flaky data)
- Hitting external APIs without mocking — flakes when they're down

## Prerequisites
- [[Unit Testing]] · [[Integration Testing]] · [[Browser DevTools]]

## What To Learn Next
- [[Playwright]] · [[Puppeteer]] · [[CI CD]]

## Best Learning Resources

### Official Documentation
- [Playwright Docs](https://playwright.dev/) — best-in-class
- [Cypress Docs](https://docs.cypress.io/)
- [Puppeteer Docs](https://pptr.dev/)

### Best YouTube Resource
- [Playwright (official)](https://www.youtube.com/c/Playwrightdev)
- [Stefan Judis](https://www.youtube.com/c/StefanJudis) — practical Playwright
- [Joel Quenneville (testing patterns)](https://www.youtube.com/results?search_query=playwright+joel+quenneville)

### Best Free Course
- [Playwright getting started + workshops](https://playwright.dev/docs/intro) — free official
- [Test automation university (free)](https://testautomationu.applitools.com/)

### Best Advanced Resource
- [Playwright Engineering blog](https://playwright.dev/blog) — internals + tips
- [Test Pyramid — Martin Fowler](https://martinfowler.com/articles/practical-test-pyramid.html)

### Best Practice Project
Add a 5-test Playwright suite for a real app's critical paths (signup, login, create, edit, delete). Wire it to CI to run on PR with traces uploaded. Add a nightly cross-browser job (chromium + firefox + webkit).

### Recommended Order to Learn
1. Locators (`getByRole`, `getByText`)
2. Waiting + auto-retries
3. Network mocking
4. Auth state reuse
5. Traces + videos
6. Parallel + sharding
7. Visual regression

## Interview Questions
**Q. Why fewer E2E tests than unit?**
A. Slow, expensive, flakier. Test pyramid: lots of unit, some integration, few E2E.

**Q. How to avoid flakiness?**
A. Stable selectors (`getByRole`), built-in auto-wait, isolate test data, mock external deps, retry strategies for known-flaky cases (sparingly).

**Q. Playwright vs Cypress?**
A. Playwright: multi-browser, multi-tab, multi-context, better parallelism. Cypress: single-browser-tab, batteries-included DX.

## Related
- [[Playwright]] · [[Puppeteer]] · [[Unit Testing]] · [[Integration Testing]]
