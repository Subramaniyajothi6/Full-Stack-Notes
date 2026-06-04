---
tags: [infra, testing, intermediate]
---

# Puppeteer

> Headless Chrome control library by Google. Used for scraping, PDF generation, screenshots, and browser automation.

## Why it matters
Pre-Playwright workhorse. Still ideal for non-test scraping/automation tasks where multi-browser support isn't needed.

## Core ideas
- `launch({ headless: 'new' })` returns Browser
- `browser.newPage()` for tab
- DOM queries: `page.$`, `page.$$`, `page.evaluate(() => ...)`
- Network interception (`page.setRequestInterception`)
- PDF / screenshot APIs

## Example
```ts
import puppeteer from 'puppeteer';

const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.goto('https://example.com');
await page.pdf({ path: 'page.pdf', format: 'A4' });
await page.screenshot({ path: 'page.png', fullPage: true });
await browser.close();
```

## Real World Usage
- Server-side PDF rendering
- Headless SEO previews / OG image generation
- Web scraping (respect robots + ToS)
- Generating thumbnails of webpages
- Crawling for monitoring (uptime, broken links)

## Common Mistakes
- Forgetting to close pages/browsers → memory leak
- Using as test runner — Playwright is purpose-built for that
- Crawling at high rate → IP bans, rule violations
- Heavy CPU per page; not budgeting concurrency

## Prerequisites
- [[Async Await|Async/Await]] · [[Browser Internals]]

## What To Learn Next
- [[Playwright]] · [[E2E Testing]]

## Best Learning Resources

### Official Documentation
- [Puppeteer Docs](https://pptr.dev/) — clear API reference
- [Google Chrome DevTools team examples](https://github.com/puppeteer/puppeteer/tree/main/examples)

### Best YouTube Resource
- [Web Dev Simplified — Puppeteer](https://www.youtube.com/c/WebDevSimplified)
- [Fireship — scraping with Puppeteer](https://www.youtube.com/c/Fireship)

### Best Free Course
- [Puppeteer guide on pptr.dev](https://pptr.dev/guides/) — sufficient

### Best Advanced Resource
- [Puppeteer source on GitHub](https://github.com/puppeteer/puppeteer)
- [Browserless docs](https://docs.browserless.io/) — production-grade headless infra

### Best Practice Project
Build a "screenshot + PDF" microservice: queue jobs (Redis), launch Puppeteer worker pool, generate, upload to S3 via presigned URL. Add concurrency limit + memory monitor.

### Recommended Order to Learn
1. Launch + page basics
2. DOM queries + evaluate
3. Network interception
4. PDF + screenshot
5. Worker pool + concurrency
6. Anti-bot countermeasures (when allowed)

## Interview Questions
**Q. Puppeteer vs Playwright?**
A. Playwright = test framework, multi-browser, modern. Puppeteer = automation library, Chrome-only, simpler.

**Q. Why does headless server-side rendering use a lot of memory?**
A. Each page spins up a renderer process; pool to share + recycle.

## Related
- [[Playwright]] · [[E2E Testing]] · [[Browser Internals]]
