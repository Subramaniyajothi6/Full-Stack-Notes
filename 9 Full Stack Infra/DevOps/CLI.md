---
tags: [infra, devenv, beginner]
---

# CLI

> Command-line interfaces — the most efficient way to interact with computers, especially servers.

## Why it matters
Servers, CI/CD, Docker, Kubernetes, deployments — everything runs on commands. CLI fluency is non-negotiable for backend work.

## Core ideas
- **Shell** — bash, zsh, fish, PowerShell — interpret commands
- **Pipes & redirection** — `|`, `>`, `<`, `2>&1` — compose tools
- **Filters** — `grep`, `awk`, `sed`, `cut`, `sort`, `uniq`, `wc`
- **Process control** — `&`, `jobs`, `fg`, `bg`, `kill`, `nohup`
- **Globbing & expansion** — `*.txt`, `{a,b}`, `~`, `$VAR`

## Quick reference
```bash
ls -lah                # detailed listing
find . -name "*.js"    # locate files
grep -rn "TODO" src    # search recursively, line numbers
ps aux | grep node     # find process
curl -i https://x.com  # HTTP request
ssh user@host          # remote login
scp file user@host:/p  # copy over SSH
tail -f log.txt        # follow log
xargs -I{} echo {}     # invoke per line
```

## Real World Usage
- SSH into prod box, tail logs, check `top`/`htop`
- Build pipelines: `npm ci && npm test && docker build`
- Quick data wrangling without Excel: `cut`, `awk`, `jq`
- Scripting deploys before learning Terraform

## Common Mistakes
- Quoting variables: `rm -rf $DIR/` — if `DIR` is empty, ruins the system. Use `"${DIR:?}"`.
- `cd && command` — `cd` failure should abort. Use `cd ... || exit`.
- Editing files while program reads them in same shell pipeline
- Shipping scripts without `set -euo pipefail`

## Prerequisites
- Basic computing literacy

## What To Learn Next
- [[Linux Basics]] · [[Shell Commands]] · [[Docker]]

## Best Learning Resources

### Official Documentation
- [Bash Reference Manual](https://www.gnu.org/software/bash/manual/) — definitive
- [tldr pages](https://tldr.sh/) — example-first command help

### Best YouTube Resource
- [The Primeagen — Terminal/Bash](https://www.youtube.com/c/ThePrimeagen) — practical, fast
- [TechWorld with Nana — Linux/CLI](https://www.youtube.com/c/TechWorldwithNana) — DevOps angle

### Best Free Course
- [MIT Missing Semester — Shell tools](https://missing.csail.mit.edu/) — exactly the things schools skip
- [LinuxJourney](https://linuxjourney.com/) — interactive

### Best Advanced Resource
- [The Art of Command Line](https://github.com/jlevy/the-art-of-command-line) — concise reference of pro tips
- [explainshell.com](https://explainshell.com/) — paste any command, get every flag explained

### Best Practice Project
Write a bash script that takes a folder, finds all images, generates thumbnails (ImageMagick), and outputs an HTML index. Add error handling, logging, and a `--dry-run` flag.

### Recommended Order to Learn
1. Navigation + file ops
2. Pipes + redirection
3. grep/awk/sed
4. Process control + signals
5. Shell scripting (variables, loops, functions)
6. SSH, scp, rsync

## Interview Questions
**Q. What does `2>&1 | tee log.txt` do?**
A. Redirects stderr to stdout, then tees combined stream into a file and the terminal.

**Q. Difference between `>` and `>>`?**
A. `>` overwrites; `>>` appends.

**Q. How to find which process owns a port?**
A. `lsof -i :3000` or `ss -tulpn | grep 3000`.

**Q. Why use `set -euo pipefail` in scripts?**
A. Exit on errors, undefined vars, and pipeline failures — fails loudly instead of silently.

## Related
- [[Linux Basics]] · [[Shell Commands]] · [[CI CD]]
