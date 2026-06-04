---
tags: [git, intermediate, tooling]
---

# GitHub Workflows

> PRs, reviews, Actions, branch protection — the day-to-day collaboration layer on top of Git.

## Pull Request anatomy
- **Source branch → target branch** (typically `feature/x → main`)
- Description with context, screenshots, test plan
- Auto-linked issues (`Closes #123`)
- Reviewers + CODEOWNERS auto-assign
- Status checks (CI must pass)
- Conversation resolution required before merge
- Merge style (squash / rebase / merge commit)

## Branch protection rules
- Require PR + review before merge
- Require status checks (CI)
- Dismiss stale reviews on push
- Require linear history
- Restrict who can push directly
- Require signed commits (high-trust repos)

## GitHub Actions essentials
```yaml
name: CI
on: [pull_request, push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20', cache: 'npm' }
      - run: npm ci
      - run: npm test
```

## CODEOWNERS
```
# .github/CODEOWNERS
/apps/api/  @backend-team
*.tf        @infra-team
docs/       @writing-team
```

## Useful patterns
- **Conventional commits** + automatic changelog (e.g. semantic-release)
- **PR templates** in `.github/PULL_REQUEST_TEMPLATE.md`
- **Issue templates** to nudge clear bug reports
- **Required PR labels** before merge
- **Dependabot** for security + version updates
- **GitHub Projects** for kanban / roadmap

## Real World Usage
- Small team: branch protection + CI required + squash merge
- Open-source: PR template + CODEOWNERS + good first issue labels
- Enterprise: required reviews from CODEOWNERS + signed commits
- Monorepo: per-package CODEOWNERS, path-filtered CI jobs

## Common Mistakes
- No branch protection on `main` (anyone can push, force-push)
- CI not required → merging red PRs
- 1000-line PRs that no one reviews seriously
- Reviewers not auto-assigned → bottlenecks
- Secrets in plain workflow YAML
- Workflows that auto-deploy from forks (security risk)

## Prerequisites
- [[Git Basics]] · [[Branching Strategies]] · [[CI CD]]

## What To Learn Next
- [[Full-Stack CI CD]] · [[Secrets Management]]

## Best Learning Resources

### Official Documentation
- [GitHub Actions docs](https://docs.github.com/en/actions)
- [Branch protection rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule)
- [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositories-settings-and-features/customizing-your-repository/about-code-owners)

### Best YouTube Resource
- [GitHub YouTube](https://www.youtube.com/github)
- [TechWorld with Nana — GitHub Actions](https://www.youtube.com/c/TechWorldwithNana)

### Best Free Course
- [GitHub Skills (interactive)](https://skills.github.com/)
- [Awesome Actions list](https://github.com/sdras/awesome-actions)

### Best Advanced Resource
- [Octokit + GitHub Apps for automation](https://docs.github.com/en/apps)
- [Reusable workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows)

### Best Practice Project
Set up a repo with: required PR review, required CI, CODEOWNERS, Dependabot, PR template, conventional-commit-driven release. Run a fake "real" change through the pipeline; document each step.

### Recommended Order to Learn
1. PR + review basics
2. Branch protection rules
3. CI workflow (lint/test/build)
4. CODEOWNERS + auto-assign
5. Reusable workflows + composite actions
6. Dependabot + secret scanning
7. OIDC to cloud (replace long-lived secrets)

## Interview Questions
**Q. Why branch protection?**
A. Stops accidents — force-pushes, untested code, unreviewed merges. Cheap insurance.

**Q. CODEOWNERS use cases?**
A. Auto-route PRs to the right team; enforce that owners must approve changes in their areas.

**Q. Why OIDC for cloud deploys?**
A. Replaces long-lived AWS keys in GitHub Secrets with short-lived STS tokens — much safer.

## Related
- [[Git Basics]] · [[Branching Strategies]] · [[CI CD]] · [[Full-Stack CI CD]] · [[Secrets Management]]
