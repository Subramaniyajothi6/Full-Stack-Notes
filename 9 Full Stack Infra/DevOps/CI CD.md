---
tags: [infra, devops, intermediate]
---

# CI CD

> Continuous Integration (run tests on every change) + Continuous Deployment (auto-ship to environments).

## Why it matters
Catches bugs early, makes releases boring (in a good way), enables safe rapid iteration.

## Core ideas
- **Pipeline** — a sequence of stages (lint → test → build → deploy)
- **Trigger** — push, PR, schedule, manual
- **Runner** — VM/container that executes steps
- **Artifact** — output (binary, image) passed between jobs
- **Cache** — speeds up dep install / build
- **Secrets** — injected at runtime via env vars (never in repo)
- **Environments** — staging vs prod with approval gates

## Tools
- **GitHub Actions** — most popular, generous free tier
- **GitLab CI** — built into GitLab
- **CircleCI**, **Buildkite**, **Jenkins**
- **Vercel/Netlify** — Git-based deploys for frontend
- **Argo CD / Flux** — GitOps for K8s

## GitHub Actions example
```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20', cache: 'npm' }
      - run: npm ci
      - run: npm run lint
      - run: npm test -- --coverage
      - uses: codecov/codecov-action@v4
```

## Real World Usage
- Test + build on every PR
- Auto-deploy `main` to staging
- Manual promotion to prod with approval
- Nightly E2E runs
- Container image build + push to registry

## Common Mistakes
- Long pipelines (>10 min) — slow feedback
- No caching — pays full install cost every run
- Secrets in code or in plain env in YAML
- "Test" jobs that don't fail the build
- Deploying without rollback strategy
- Running same workflow with different env vars instead of separate jobs

## Prerequisites
- [[CLI]] · [[Docker]] · Git basics

## What To Learn Next
- [[Terraform]] · [[AWS]] · [[Sandboxing]]

## Best Learning Resources

### Official Documentation
- [GitHub Actions docs](https://docs.github.com/en/actions) — most depth
- [GitLab CI/CD docs](https://docs.gitlab.com/ee/ci/)

### Best YouTube Resource
- [TechWorld with Nana — CI/CD Crash Course](https://www.youtube.com/c/TechWorldwithNana)
- [Anton Putra — DevOps + GH Actions](https://www.youtube.com/c/AntonPutra)

### Best Free Course
- [GitHub Actions Hero (gamified)](https://lab.github.com/githubtraining/github-actions:-hello-world)
- [DevOps Roadmap (roadmap.sh)](https://roadmap.sh/devops)

### Best Advanced Resource
- [Continuous Delivery — Dave Farley YouTube](https://www.youtube.com/c/ContinuousDelivery) — pioneer
- [GitOps with Argo CD docs](https://argo-cd.readthedocs.io/)

### Best Practice Project
Add a complete pipeline to your MERN repo: lint → test (Vitest) → E2E (Playwright headless) → docker build → push to GHCR → deploy preview to Fly/Vercel on PR, deploy to prod on `main`. Add a manual approval gate for prod.

### Recommended Order to Learn
1. Pipeline as code basics
2. Caching + matrix builds
3. Secrets management
4. Build artifacts + image registries
5. Environments + approvals
6. GitOps + IaC integration

## Interview Questions
**Q. CI vs CD vs CDeployment?**
A. CI integrates code and runs tests. CD = Continuous Delivery (always-deployable, manual ship) or Continuous Deployment (auto-ship on green).

**Q. How do you keep secrets out of CI logs?**
A. Use the platform's secret store; never `echo` secrets; mark outputs as masked; rotate often.

**Q. What's the role of immutable artifacts?**
A. Build once; promote the same artifact through environments. Avoids "works in staging, fails in prod" from rebuilds.

**Q. Why GitOps?**
A. Git is the source of truth for infrastructure. Deploys are PRs; rollback is `git revert`.

## Related
- [[Docker]] · [[Terraform]] · [[AWS]]
