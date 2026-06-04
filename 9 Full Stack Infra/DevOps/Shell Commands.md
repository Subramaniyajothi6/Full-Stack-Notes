---
tags: [infra, devenv, beginner]
---

# Shell Commands

> The 30 commands that cover 95% of daily Linux/Unix work.

## Why it matters
Productivity multiplier. Every senior engineer composes pipelines reflexively.

## Categories

### Files
| Cmd     | Use                                |
| ------- | ---------------------------------- |
| `ls`    | list files                         |
| `cd`    | change dir                          |
| `pwd`   | current dir                         |
| `mkdir -p` | create nested                   |
| `cp -r` | copy recursively                   |
| `mv`    | move/rename                        |
| `rm -rf`| recursive delete (DANGEROUS)       |
| `ln -s` | symlink                            |
| `find`  | search filesystem                  |
| `tree`  | dir tree                           |

### Text
| Cmd      | Use                                 |
| -------- | ----------------------------------- |
| `cat`    | print file                          |
| `head -n`| first N lines                       |
| `tail -f`| follow log                          |
| `less`   | pager                               |
| `grep -rn` | search content                    |
| `awk`    | column-oriented text                |
| `sed`    | stream edit (`sed -i s/a/b/g`)      |
| `cut -d` | split by delimiter                  |
| `sort -u`| sort unique                         |
| `uniq -c`| count duplicates                    |
| `wc -l`  | line count                          |
| `jq`     | JSON                                |
| `xargs`  | feed args from stdin                |

### Network
| Cmd          | Use                            |
| ------------ | ------------------------------ |
| `curl -i`    | HTTP w/ headers                |
| `wget`       | download                       |
| `ssh`/`scp`  | remote shell / copy            |
| `dig`/`nslookup` | DNS                        |
| `ss -tulpn`  | listening ports                |
| `ping`       | ICMP                           |
| `traceroute` | path                           |

### System
| Cmd            | Use                          |
| -------------- | ---------------------------- |
| `top`/`htop`   | process view                 |
| `ps aux`       | snapshot                     |
| `kill -9 PID`  | force kill                   |
| `df -h`        | disk free                    |
| `du -sh *`     | folder sizes                 |
| `free -h`      | memory                       |
| `uptime`       | load avg                     |
| `journalctl -u` | systemd logs                |
| `systemctl`    | service control              |

## Power patterns
```bash
# Top 10 biggest files
find . -type f -printf '%s %p\n' | sort -rn | head

# Replace string in many files
grep -rl "OLD" . | xargs sed -i 's/OLD/NEW/g'

# Watch a JSON API
watch -n 1 'curl -s http://localhost/health | jq .'

# Disk usage by extension
find . -type f | sed 's/.*\.//' | sort | uniq -c | sort -rn
```

## Real World Usage
- Server log triage with `grep | awk | sort | uniq -c`
- CI scripts piping test output through `jq` for summary
- Quick one-liners instead of writing scripts

## Common Mistakes
- Forgetting quotes around variables → globbing/word-splitting bugs
- `rm` without `--` when filenames begin with `-`
- Using `cat file | grep` instead of `grep ... file`
- Not chaining with `&&` (continue on success) vs `;` (always)

## Prerequisites
- [[CLI]]

## What To Learn Next
- [[Linux Basics]] · [[CI CD]] · [[Docker]]

## Best Learning Resources

### Official Documentation
- [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/) — every flag, canonical
- [tldr.sh](https://tldr.sh/) — fast example-first

### Best YouTube Resource
- [DistroTube](https://www.youtube.com/c/DistroTube) — terminal workflows
- [Primeagen — terminal flow](https://www.youtube.com/c/ThePrimeagen)

### Best Free Course
- [explainshell.com](https://explainshell.com/) — incremental learning by exploring commands
- [bashscripting.io](https://bashscripting.io/)

### Best Advanced Resource
- [Bash Hackers Wiki](https://wiki.bash-hackers.org/) — gotchas and patterns
- [shellcheck](https://www.shellcheck.net/) — lint your scripts

### Best Practice Project
Write a `dev-info` script that prints OS info, listening ports, top 5 memory hogs, last 10 commits in current dir, current Git branch — formatted with colors. Extend with flags.

### Recommended Order to Learn
1. File + nav commands
2. grep / awk / sed
3. Pipes + xargs
4. Process control
5. Networking commands
6. Shell scripting

## Interview Questions
**Q. Print line numbers where "ERROR" appears in big.log.**
A. `grep -n ERROR big.log`

**Q. Sort a CSV by column 2, descending.**
A. `sort -t, -k2 -rn file.csv`

**Q. Tail-follow a log but only show lines containing "auth".**
A. `tail -f app.log | grep --line-buffered auth`

**Q. Replace a string across many files.**
A. `grep -rl "OLD" . | xargs sed -i 's/OLD/NEW/g'`

## Related
- [[CLI]] · [[Linux Basics]]
