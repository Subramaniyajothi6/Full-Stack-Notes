---
tags: [git, beginner, tooling]
---

# Git Basics

> Distributed version control. Snapshots of your repo over time; branches are cheap, merging is normal.

## Mental model
- **Working tree** — files on disk
- **Index / staging** — what's queued for the next commit
- **HEAD** — your current commit
- **Refs** — branches and tags pointing at commits
- **Remote** — another copy of the repo (origin)

## Daily commands
```bash
git status
git add path                      # stage
git add -p                        # stage hunks interactively
git commit -m "msg"
git commit --amend                 # rewrite last commit (only before push)
git log --oneline --graph --decorate --all
git diff [--staged]
git switch branch                  # checkout newer alternative
git switch -c new-branch           # create + switch
git restore --staged file          # unstage
git restore file                   # discard local changes (careful)
```

## Sync
```bash
git fetch                          # update remote refs
git pull --rebase                  # fetch + replay your commits on top
git push
git push -u origin branch          # set upstream
```

## History rewriting (safely on YOUR branches)
```bash
git rebase -i HEAD~5               # squash, reword, reorder
git reset --hard HEAD~1            # nuke last commit (dangerous)
git reflog                         # find lost commits
```

## Stash
```bash
git stash push -m "wip"
git stash pop
git stash list
```

## Real World Usage
- Feature branches off main
- Squash-merge PRs into main
- `git bisect` to find which commit introduced a bug
- `git blame` for archeology
- `git cherry-pick` to pull a single commit across branches

## Common Mistakes
- `git push --force` to a shared branch (use `--force-with-lease`)
- Committing secrets (gitleaks pre-commit hook helps)
- Huge binary files in repo (use Git LFS)
- `git pull` (merge) when team uses rebase workflow
- Long-lived branches → painful merges
- Naming branches `temp/x` then forgetting them

## Prerequisites
- [[CLI]]

## What To Learn Next
- [[Branching Strategies]] · [[GitHub Workflows]]

## Best Learning Resources

### Official Documentation
- [Git docs](https://git-scm.com/doc)
- [Pro Git book (free)](https://git-scm.com/book/en/v2)

### Best YouTube Resource
- [The Net Ninja — Git & GitHub](https://www.youtube.com/c/TheNetNinja)
- [Fireship — Git in 100 seconds + tips](https://www.youtube.com/c/Fireship)

### Best Free Course
- [Learn Git Branching (interactive)](https://learngitbranching.js.org/)
- [Atlassian Git tutorials](https://www.atlassian.com/git/tutorials)

### Best Advanced Resource
- [Pro Git book — chapters on internals](https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain)
- [Julia Evans Git zines](https://wizardzines.com/zines/git/)

### Best Practice Project
Take any 10 of your old commits and practice: amend, rebase-squash, cherry-pick, reset, reflog recover. Without a remote, so mistakes are isolated.

### Recommended Order to Learn
1. add / commit / status / log / diff
2. Branches + switch
3. Remotes + push / pull
4. Rebase vs merge
5. Stash + cherry-pick
6. Interactive rebase
7. Bisect + blame + reflog

## Interview Questions
**Q. Rebase vs merge?**
A. Rebase replays your commits on top of base → linear history. Merge keeps both histories with a merge commit. Teams pick one; rebase = clean, merge = explicit.

**Q. `--force-with-lease` vs `--force`?**
A. `--force-with-lease` aborts if someone else pushed since you last fetched — prevents stomping on others.

**Q. How do you recover a deleted branch?**
A. `git reflog` shows recent HEAD movements; `git branch <name> <sha>` resurrects.

## Related
- [[CLI]] · [[Branching Strategies]] · [[GitHub Workflows]]
