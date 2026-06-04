---
tags: [moc, testing]
---

# Testing MOC

> Test pyramid from fast units → component integration → end-to-end browser flows.

## Layers
- [[Unit Testing]] — smallest pieces in isolation
- [[Integration Testing]] — modules together (route + DB + middleware)
- [[E2E Testing]] — real browser, real user flows
- [[Visual Regression]] — pixel diffs to catch CSS/layout bugs
- [[Load Testing]] — find capacity limits
- [[Contract Testing]] — producer/consumer agreement
- [[Mutation Testing]] — quality of your tests

## Tools
- [[Vitest]] — Vite-powered runner; replaces Jest in modern stacks
- [[React Testing Library]] — render React, query like a user
- [[MSW]] — network mock at the request layer
- [[Playwright]] — multi-browser E2E; auto-wait, traces, codegen
- [[Puppeteer]] — Chrome automation, scraping, PDF/screenshot
- [[TestSprite]] — AI-driven test generation + maintenance

## Suggested order
1. [[Unit Testing]] (with [[Vitest]])
2. [[React Testing Library]] + [[MSW]]
3. [[Integration Testing]] (supertest + testcontainers)
4. [[E2E Testing]] (with [[Playwright]])
5. [[Visual Regression]]
6. [[Contract Testing]] (when multi-team / public API)
7. [[Load Testing]] (pre-launch + regression)
8. [[Mutation Testing]] (critical domain logic)

## Roadmap to fill in
- [ ] Storybook + Chromatic in detail
- [ ] Cypress (legacy choice; covered briefly here)
- [ ] Test data management + factories
- [ ] Snapshot testing best practices
- [ ] Property-based testing (fast-check)
- [ ] Test impact analysis / selective runs
- [ ] Flake hunting + retries

## Related stacks
- [[CI CD]] — wire tests into pipelines
- [[React MOC]] · [[NodeJS MOC]] · [[Express MOC]]
- [[DevOps MOC]] — observability complements testing

## Related
- [[Full Stack Infra MOC]] · [[MERN MOC]]
