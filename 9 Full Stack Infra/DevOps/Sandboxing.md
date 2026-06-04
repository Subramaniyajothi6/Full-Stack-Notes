---
tags: [infra, backend, advanced, security]
---

# Sandboxing

> Constraining what a process can do — what files it sees, what syscalls it can make, what network it can reach.

## Why it matters
Untrusted code, plugins, or even your own dependencies should run with least privilege. The blast radius of a compromised process should be tiny.

## Mechanisms (Linux)
- **Namespaces** — isolate PID, mount, network, user, IPC, UTS
- **cgroups v2** — CPU, memory, IO, pids quotas
- **seccomp-bpf** — filter syscalls (allow-list)
- **AppArmor / SELinux** — MAC policies
- **chroot / pivot_root** — limit FS view
- **landlock** — newer, capability-style restrictions

## Higher-level options
- **Docker** — namespaces + cgroups + seccomp by default
- **gVisor** — user-space kernel intercepts syscalls
- **Firecracker** — KVM microVMs — see [[Firecracker]]
- **WASM** — capability-based, runs in V8/wasmtime — see [[WASM]]
- **V8 isolates** — Cloudflare Workers approach

## Tradeoff matrix
| Tech         | Isolation | Cold-start | Density | Use case                   |
| ------------ | --------- | ---------- | ------- | -------------------------- |
| Container    | medium    | ~100ms     | high    | trusted multi-tenant       |
| gVisor       | high      | ~200ms     | high    | hostile multi-tenant       |
| Firecracker  | very high | ~125ms     | high    | hostile, kernel boundary   |
| V8 isolate   | medium    | ~5ms       | huge    | edge functions             |
| WASM         | high      | ~1–10ms    | huge    | plugins, edge              |

## Real World Usage
- Cloudflare Workers (V8 isolates)
- AWS Lambda (Firecracker)
- Replit / Fly.io (Firecracker)
- Browsers (process per site + sandbox)
- Plugin systems via WASM (Figma, Shopify Functions)

## Common Mistakes
- Running as root inside a container
- Mounting `/var/run/docker.sock` (host docker access = root)
- Trusting `--read-only` without `--tmpfs /tmp` (apps crash, devs disable readonly)
- Forgetting seccomp profile in Kubernetes (default RuntimeDefault is recommended)
- Treating containers as VMs for hostile tenants

## Prerequisites
- [[Linux Basics]] · [[Docker]]

## What To Learn Next
- [[Firecracker]] · [[WASM]] · [[Remote Code Execution]]

## Best Learning Resources

### Official Documentation
- [Linux man-pages — namespaces, seccomp, cgroups](https://man7.org/linux/man-pages/) — canonical
- [Docker security docs](https://docs.docker.com/engine/security/)
- [gVisor docs](https://gvisor.dev/)

### Best YouTube Resource
- [Liz Rice — Container security talks](https://www.youtube.com/results?search_query=liz+rice+containers)
- [TechWorld with Nana — container security](https://www.youtube.com/c/TechWorldwithNana)

### Best Free Course
- [KubeCon talks on YouTube — sandboxing track](https://www.youtube.com/c/cloudnativefdn)

### Best Advanced Resource
- [Containers from Scratch — Liz Rice](https://github.com/lizrice/containers-from-scratch) — write a container in Go
- [Fly.io blog — Firecracker operations](https://fly.io/blog/)
- [Cloudflare blog — V8 isolates](https://blog.cloudflare.com/cloud-computing-without-containers/)

### Best Practice Project
Build a Python plugin runner that uses Docker + readonly FS + tmpfs `/tmp` + seccomp default + `--cap-drop=ALL` + memory/CPU limits + 1-second timeout. Then port it to gVisor and compare cold start, throughput, and an attempted syscall escape.

### Recommended Order to Learn
1. Namespaces + cgroups
2. seccomp basics
3. Docker security defaults
4. gVisor + Firecracker
5. WASM sandboxing
6. Multi-tenant production patterns

## Interview Questions
**Q. Difference between namespaces and cgroups?**
A. Namespaces isolate *what you see*; cgroups limit *how much you can use*.

**Q. Why are V8 isolates faster than containers?**
A. They start a new JavaScript context inside an already-running V8 process — no new OS process or kernel.

**Q. Why is gVisor slower than Docker?**
A. It intercepts syscalls in user-space ("Sentry"), trading throughput for stronger isolation.

**Q. Best practice: should containers run as root?**
A. No. Use `USER` in Dockerfile, drop capabilities, use non-root file ownership.

## Related
- [[Firecracker]] · [[WASM]] · [[Remote Code Execution]] · [[Docker]]
