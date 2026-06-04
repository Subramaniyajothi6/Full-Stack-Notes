---
tags: [git, intermediate, pattern]
---

# Branching Strategies

> How your team turns commits into releases. Different shapes for different products.

## Trunk-based development (modern default)
- `main` is always shippable
- Short-lived branches (hours to a couple days)
- Feature flags gate incomplete work
- Continuous integration; deploys often
- Best for SaaS / web

## GitHub Flow
- Same as trunk-based but slightly more ceremony
- `main` is deployable; feature branches → PR → merge → deploy
- Lightweight

## GitFlow (heavier; older)
- `main` for released code only
- `develop` for upcoming work
- `feature/*`, `release/*`, `hotfix/*` branches
- Heavier ceremony; suits scheduled releases
- Often overkill for SaaS

## Release branches
- `release/2024-Q4` cut from `main` at feature freeze
- Bug fixes cherry-picked back
- Good for shipped products with multiple supported versions (SDKs, libraries)

## Decision factors
| Need                            | Recommend         |
|---------------------------------|-------------------|
| Continuous deploys              | Trunk-based       |
| Scheduled monthly releases      | GitHub Flow       |
| Multiple supported versions     | GitFlow + release |
| Open-source project             | GitHub Flow       |
| Library / SDK with semver       | GitFlow-lite      |

## Merge styles
- **Squash and merge** — single commit per PR; clean main history; lose individual commit messages
- **Rebase and merge** — preserve commit-by-commit history, linear
- **Merge commit** — preserves branch shape; noisy

Most teams pick squash for app repos.

## Real World Usage
- SaaS: trunk-based + feature flags
- Open-source: GitHub Flow + label-based release notes
- Libraries: GitFlow-lite with release branches
- Game / desktop apps: long-lived release branches

## Common Mistakes
- Long-lived branches → merge hell
- Mixing strategies across a team
- "Feature flag everything" — flags accumulate; remove them
- Cherry-picking instead of merging properly between long-lived branches
- Force-pushing to shared branches

## Prerequisites
- [[Git Basics]]

## What To Learn Next
- [[GitHub Workflows]] · [[Full-Stack CI CD]]

## Best Learning Resources

### Official Documentation
- [GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow)
- [Atlassian — Branching strategies](https://www.atlassian.com/git/tutorials/comparing-workflows)

### Best YouTube Resource
- [Continuous Delivery — Dave Farley](https://www.youtube.com/c/ContinuousDelivery) — trunk-based proponent

### Best Free Course
- [Trunk-Based Development site](https://trunkbaseddevelopment.com/)
- [Atlassian Git workflows](https://www.atlassian.com/git/tutorials/comparing-workflows)

### Best Advanced Resource
- [Accelerate (Forsgren, Humble, Kim)](https://itrevolution.com/product/accelerate/) — DORA metrics + trunk-based evidence

### Best Practice Project
Audit your team's branching style. Map it onto one of the named patterns. Cap branch age via PR-stale automation. Try squash merging for one sprint; review history readability after.

### Recommended Order to Learn
1. Solo: GitHub Flow
2. Team: trunk-based + short branches
3. Feature flags to enable incomplete work on main
4. Branch protection rules
5. Release cadence + tagging strategy

## Interview Questions
**Q. Trunk-based vs GitFlow?**
A. Trunk-based: small branches, continuous deploy, feature flags. GitFlow: long branches, scheduled releases. Modern web teams strongly favor trunk-based.

**Q. Squash vs rebase merge?**
A. Squash: one commit per PR, clean linear main, lose intermediate detail. Rebase: keep every commit linearized. Pick based on whether you value "what was the unit of change" or "what were the steps."

## Related
- [[Git Basics]] · [[GitHub Workflows]] · [[Full-Stack CI CD]]
