---
tags: [infra, devenv, beginner]
---

# Linux Basics

> The OS that runs almost every server, container, and cloud workload.

## Why it matters
Backend, DevOps, Docker, Kubernetes — all Linux underneath. Understanding the kernel/userspace boundary is essential for performance and reliability.

## Core ideas
- **Filesystem hierarchy** — `/etc` config, `/var` logs/state, `/usr` programs, `/home` users
- **Permissions** — owner/group/other × read/write/execute (`chmod 755`, `chown`)
- **Processes** — pid, ppid, signals (SIGTERM 15, SIGKILL 9), zombies, daemons
- **Users & groups** — `/etc/passwd`, `sudo`, `useradd`
- **Package managers** — `apt` (Debian/Ubuntu), `dnf`/`yum` (RHEL/Fedora), `pacman` (Arch), `apk` (Alpine)
- **Services** — `systemctl status/start/restart/enable`, journalctl
- **Networking** — `ip a`, `ss`, `iptables`/`nftables`, `/etc/hosts`, `/etc/resolv.conf`

## Cheat-sheet
```bash
top                    # live process view
htop                   # nicer top
df -h                  # disk usage
du -sh *               # folder sizes
free -h                # memory
journalctl -u nginx    # service logs
systemctl restart x    # restart service
useradd -m -s /bin/bash alice
chmod 644 file.txt     # rw-r--r--
chown -R user:group .  # recursive ownership
```

## Real World Usage
- Setting up a VPS with nginx + Let's Encrypt
- Dockerfile choices (Alpine vs Debian)
- Debugging "out of memory" via `dmesg | grep -i kill`
- Cron jobs for backups, log rotation

## Common Mistakes
- `rm -rf /` (or worse, `rm -rf $UNSET/`) — irrecoverable. Always quote and check.
- Editing `/etc/passwd` directly instead of `useradd`
- Using `sudo` for everything when group membership would suffice
- Not enabling `ufw`/firewall on cloud VMs

## Prerequisites
- [[CLI]]

## What To Learn Next
- [[Shell Commands]] · [[Docker]] · [[AWS]]

## Best Learning Resources

### Official Documentation
- [The Linux man-pages project](https://www.kernel.org/doc/man-pages/) — canonical
- [Arch Wiki](https://wiki.archlinux.org/) — best general-purpose Linux wiki even on Ubuntu

### Best YouTube Resource
- [TechWorld with Nana — Linux for DevOps](https://www.youtube.com/c/TechWorldwithNana) — clean operational depth
- [Learn Linux TV](https://www.youtube.com/c/LearnLinuxTV) — long-form practical

### Best Free Course
- [Linux Foundation — Intro to Linux (edX)](https://www.edx.org/course/introduction-to-linux) — official, free audit
- [LinuxJourney](https://linuxjourney.com/) — interactive

### Best Advanced Resource
- [The Linux Programming Interface (TLPI)](https://man7.org/tlpi/) — Michael Kerrisk; encyclopedic
- [Brendan Gregg's site](https://www.brendangregg.com/) — performance + observability gold

### Best Practice Project
Provision a $5 VPS, harden SSH (key-only, fail2ban, ufw), install nginx, deploy a Node service via systemd, set up TLS via certbot, set up nightly backups via cron + rsync to S3.

### Recommended Order to Learn
1. Filesystem + permissions
2. Processes + signals
3. Package managers + services (systemd)
4. Networking basics
5. Shell scripting
6. Performance tools (top, iostat, vmstat, perf)

## Interview Questions
**Q. Difference between SIGTERM and SIGKILL?**
A. SIGTERM (15) asks process to terminate cleanly; can be trapped. SIGKILL (9) is forced by kernel; cannot be caught.

**Q. What does `chmod 755` mean?**
A. Owner: rwx; group: r-x; others: r-x.

**Q. How do you see what's listening on port 80?**
A. `ss -tulpn | grep :80` (or `lsof -i :80`).

**Q. Difference between hard link and symlink?**
A. Hard link is another directory entry to the same inode (no path stored). Symlink is a file containing a path string; can cross filesystems and break.

## Related
- [[CLI]] · [[Shell Commands]] · [[Docker]]
