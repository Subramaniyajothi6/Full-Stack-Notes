---
tags: [infra, backend, advanced, security]
---

# Remote Code Execution

> Running user-supplied code on your server safely. The hardest problem in backend security.

## Why it matters
Code playgrounds (Replit, CodeSandbox), AI agents that run shell, build pipelines that take untrusted input — all need RCE done right.

## Threat model
A malicious user payload may try to:
- Read other users' files / data
- Spawn long-running CPU/memory hogs
- Make network calls (data exfil, internal SSRF)
- Persist (cron, systemd unit)
- Escape the sandbox (kernel exploits)

## Defense layers (defense-in-depth)
1. **Process isolation** — separate user; no shared FS
2. **Container** — Docker namespace + cgroups for CPU/memory limits
3. **MicroVM** — Firecracker, Kata Containers — kernel-level isolation
4. **WASM** — capability-based sandbox; no syscalls without grants
5. **gVisor** — user-space kernel intercepts syscalls
6. **Network policy** — deny-by-default egress; whitelist
7. **Resource limits** — CPU shares, memory caps, ulimits, timeouts
8. **Static analysis** — reject obvious bad inputs before execution

## Real World Usage
- Code execution for online editors (Replit uses Firecracker; CodeSandbox uses VMs/containers)
- AI agent tools that run shell or Python
- CI runners (GitHub Actions, CircleCI)
- Plugin systems

## Common Mistakes
- Running user code in a shared Node `vm` module thinking it's a sandbox (it's not)
- Allowing network egress to internal metadata endpoints (cloud SSRF — `169.254.169.254`)
- Forgetting to limit pids → fork bombs
- Trusting cgroups but skipping seccomp
- Mounting host docker socket → trivial container escape

## Prerequisites
- [[Linux Basics]] · [[Docker]] · [[DoS Protection]]

## What To Learn Next
- [[Sandboxing]] · [[Firecracker]] · [[WASM]]

## Best Learning Resources

### Official Documentation
- [Firecracker docs](https://firecracker-microvm.github.io/) — open-source microVM
- [gVisor docs](https://gvisor.dev/) — user-space kernel
- [seccomp man pages](https://man7.org/linux/man-pages/man2/seccomp.2.html)

### Best YouTube Resource
- [Hussein Nasser — sandboxing](https://www.youtube.com/@hnasr)
- [TechWorld with Nana — container security](https://www.youtube.com/c/TechWorldwithNana)

### Best Free Course
- [LinuxFoundation — Container Security](https://www.linuxfoundation.org/) — free audits available
- [OWASP — Container Security Verification Standard](https://owasp.org/)

### Best Advanced Resource
- [Replit blog — How we run code](https://blog.replit.com/) — production-grade RCE
- [Fly.io blog — Firecracker in production](https://fly.io/blog/) — operational deep dives
- [Cloudflare Workers internals](https://blog.cloudflare.com/) — V8 isolates approach

### Best Practice Project
Build a tiny Python sandbox: Docker container with no network, read-only FS, 100ms CPU/64MB RAM limit, 1s timeout. Test with simple programs, then attempt fork bombs and infinite loops to confirm it kills them.

### Recommended Order to Learn
1. Threat model
2. Docker isolation + cgroups
3. seccomp + AppArmor profiles
4. gVisor/Firecracker for stronger isolation
5. WASM sandbox alternatives
6. Production case studies

## Interview Questions
**Q. Why isn't a Docker container alone enough for hostile RCE?**
A. Shared kernel. A kernel exploit lets the user escape. Use Firecracker/gVisor for tenant isolation.

**Q. How do you stop a fork bomb?**
A. Set `pids` cgroup limit; configure ulimits; kill the cgroup on threshold breach.

**Q. Why is `vm` in Node not a real sandbox?**
A. Same process, same heap; no syscall isolation. Easy to break out via prototype tampering.

**Q. SSRF mitigation in user code?**
A. Block egress to RFC1918, link-local (169.254.x), IPv6 link-local; explicit allow-list for outbound URLs.

## Related
- [[Sandboxing]] · [[Firecracker]] · [[DoS Protection]]
