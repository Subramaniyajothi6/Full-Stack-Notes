---
tags: [testing, intermediate, ui]
---

# Visual Regression

> Snapshot rendered UI to images; fail tests when pixels diverge unexpectedly. Catches CSS / layout bugs unit tests can't.

## Tools
- **Playwright** — built-in `toHaveScreenshot` matcher
- **Storybook + Chromatic** — per-story visual diff (hosted)
- **Percy** — hosted visual review
- **BackstopJS** — open-source CLI
- **Reg-suit** — open-source, S3-backed

## Playwright example
```ts
test('home looks right', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveScreenshot('home.png', { fullPage: true });
});
```
First run creates baseline. Subsequent runs diff. Failed pixels = test fail; review and update.

## Storybook + Chromatic
```yaml
# .github/workflows/chromatic.yml
- uses: chromaui/action@v1
  with: { projectToken: ${{ secrets.CHROMATIC_PROJECT_TOKEN }} }
```
Diffs every Storybook story on every PR; UI changes are reviewable like code.

## Stabilization tricks
- **Fixed viewport size** — `viewport: { width: 1280, height: 720 }`
- **Disable animations** — global CSS `transition: none`
- **Freeze time** — date mocks, hide timestamps
- **Hide variable content** — `mask: [page.locator('.dynamic')]`
- **Wait for fonts/images** — Playwright `waitForLoadState('networkidle')`

## Real World Usage
- Design-system component libraries
- Marketing pages where design pixel-fidelity matters
- Cross-browser layout checks
- Refactor confidence (Tailwind class migration)

## Common Mistakes
- No baseline review process → snapshots stale silently
- Flaky tests from animations/fonts/timestamps
- Diffing huge full-page screenshots that mask small breakages
- Ignoring CI vs local rendering differences (font availability)
- Updating snapshots blindly when failing → loses the safety net

## Prerequisites
- [[Playwright]] · [[E2E Testing]] · [[CI CD]]

## What To Learn Next
- [[Load Testing]] · [[Mutation Testing]]

## Best Learning Resources

### Official Documentation
- [Playwright Visual Comparisons](https://playwright.dev/docs/test-snapshots)
- [Chromatic docs](https://www.chromatic.com/docs/)
- [Percy docs](https://docs.percy.io/)

### Best YouTube Resource
- [Storybook YouTube](https://www.youtube.com/@chromatic-uiengineers)
- [Playwright YouTube — visual testing](https://www.youtube.com/c/Playwrightdev)

### Best Free Course
- [Storybook tutorials — Visual Testing](https://storybook.js.org/tutorials/visual-testing-handbook/)

### Best Advanced Resource
- [Argos CI](https://argos-ci.com/) — modern visual review platform

### Best Practice Project
Add visual regression to your design-system Storybook with Chromatic. Make a CSS change in one component; verify only its stories flag (others stay green).

### Recommended Order to Learn
1. Single-page screenshot baseline
2. Stabilization (fonts, animations, time)
3. Per-component Storybook + Chromatic
4. CI integration
5. Cross-browser comparisons
6. Approval workflow

## Interview Questions
**Q. Why visual regression on top of unit tests?**
A. Unit tests verify logic. Visual tests verify rendering — CSS, layout, fonts, images.

**Q. How to handle dynamic content?**
A. Mask, mock dates, freeze counters; or render only the static part.

## Related
- [[Playwright]] · [[E2E Testing]] · [[CI CD]] · [[Load Testing]]
