---
tags: [mern, deployment, intermediate]
---

# Full-Stack CI CD

> One pipeline that lints, tests, builds, and deploys a MERN app on every PR and every merge to main.

## Stages
```
PR opened
   ├── lint (eslint, prettier, biome)
   ├── typecheck (tsc --noEmit)
   ├── unit + integration tests (vitest)
   ├── e2e (playwright on a built app)
   ├── build (web + api images)
   ├── deploy preview env (Vercel preview / Fly app per PR)
   └── status check on PR

merged to main
   ├── all of the above
   ├── build + push images (api, web)
   ├── deploy staging
   ├── smoke test
   └── manual approval → deploy prod (blue-green / canary)
```

## GitHub Actions example (PR + main)
```yaml
name: CI
on:
  pull_request:
  push: { branches: [main] }

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20', cache: 'npm' }
      - run: npm ci
      - run: npm run lint
      - run: npm run typecheck
      - run: npm test -- --coverage
      - run: npx playwright install --with-deps
      - run: npm run e2e
      - uses: actions/upload-artifact@v4
        if: failure()
        with: { name: playwright-traces, path: test-results/ }

  build-and-push:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
        with: { registry: ghcr.io, username: ${{ github.actor }}, password: ${{ secrets.GITHUB_TOKEN }} }
      - uses: docker/build-push-action@v5
        with:
          context: ./apps/api
          push: true
          tags: ghcr.io/${{ github.repository }}/api:${{ github.sha }}

  deploy-prod:
    needs: build-and-push
    runs-on: ubuntu-latest
    environment: production    # requires manual approval
    steps:
      - run: ./scripts/deploy.sh ${{ github.sha }}
```

## Rollback strategy
- Tag every artifact with `git sha` (immutable)
- `./scripts/deploy.sh <sha>` works for any past sha
- Rollback = re-run with previous sha
- DB migrations: forward-only; never backwards-compatible breaks

## DB migrations in CI
```yaml
- run: npm run db:migrate         # part of deploy job
  env: { DATABASE_URL: ${{ secrets.STAGING_DATABASE_URL }} }
```
Use additive migrations (add column with default → backfill → start using → drop old later). Avoid breaking changes in a single deploy.

## Real World Usage
- PR previews so reviewers can click around
- Auto-deploy staging on every merge
- Manual approval gate to prod (compliance + sanity)
- Nightly E2E smoke
- Image scanning (Trivy) blocks deploys with CVEs

## Common Mistakes
- Slow pipelines (>15 min) — feedback loop dies → cache deps, parallelize, shard E2E
- Tests that pass locally but fail in CI (env dependency you didn't notice)
- Secrets echoed in logs (mask them; prefer OIDC over static keys)
- Building twice (build in test, build in deploy) instead of promoting one artifact
- "Skip CI" abuse → broken main
- DB migrations that aren't forward-only → rollback corrupts data

## Prerequisites
- [[CI CD]] · [[Docker]] · [[Testing MOC]] · [[Environment Management]] · [[Deployment Architecture]]

## What To Learn Next
- [[Logging Across Services]] · [[Realtime with Socket.IO]]

## Best Learning Resources

### Official Documentation
- [GitHub Actions docs](https://docs.github.com/en/actions)
- [Playwright in CI](https://playwright.dev/docs/ci)
- [Argo CD docs](https://argo-cd.readthedocs.io/) — GitOps to K8s

### Best YouTube Resource
- [TechWorld with Nana — CI/CD](https://www.youtube.com/c/TechWorldwithNana)
- [Anton Putra — Pipelines + Cloud](https://www.youtube.com/c/AntonPutra)

### Best Free Course
- [GitHub Learning Lab — Actions](https://lab.github.com/)
- [Continuous Delivery — Dave Farley YouTube](https://www.youtube.com/c/ContinuousDelivery)

### Best Advanced Resource
- [Continuous Delivery (book) — Humble & Farley](https://www.amazon.com/Continuous-Delivery-Deployment-Automation-Addison-Wesley/dp/0321601912)
- [Google SRE Workbook — release engineering](https://sre.google/workbook/)

### Best Practice Project
Add a complete pipeline to one of your project repos: lint → typecheck → unit → integration → E2E (Playwright) → build images → push to GHCR → deploy preview on PR → deploy prod on merge with approval. Document expected pipeline duration and tune to <10 min.

### Recommended Order to Learn
1. CI runs tests on PR
2. Caching + matrix builds for speed
3. Artifact build + registry push
4. Preview deploys per PR
5. Approval gates + environments
6. Blue-green / canary deploys
7. GitOps (Argo CD)

## Interview Questions
**Q. Why one artifact promoted across stages?**
A. Eliminates "works in staging, breaks in prod" caused by rebuild differences.

**Q. How do you keep CI under 10 minutes?**
A. Dependency cache, parallel jobs, shard E2E, fail-fast, only run full E2E on main.

**Q. What's a canary deploy?**
A. Route a small % of traffic to the new version, monitor metrics, then ramp up or roll back.

## Related
- [[CI CD]] · [[Docker]] · [[Dockerized MERN]] · [[Deployment Architecture]] · [[Environment Management]] · [[Testing MOC]]
