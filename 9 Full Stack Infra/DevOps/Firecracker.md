---
tags: [infra, backend, advanced]
---

# Firecracker

> Open-source KVM microVM monitor by AWS. Boots tiny virtual machines in ~125ms — built for serverless and untrusted multi-tenant workloads.

## Why it matters
Powers AWS Lambda and Fargate. Pioneered the "VM with container speed" niche. Used by Fly.io, Replit, Modal, and many AI-code-execution products.

## Core ideas
- **microVM** — minimal Linux VM with stripped-down devices
- **KVM-based** — uses the same kernel feature as real cloud hypervisors → strong tenant isolation
- **Single binary** — no daemon, no orchestration baked in
- **API-driven** — REST API to configure and start VMs
- **Jailer** — companion process applying seccomp + cgroups + namespaces *around* Firecracker itself
- **Snapshotting** — pause + resume VMs in milliseconds for warm starts

## Why pick Firecracker over Docker?
- Hostile tenants (running arbitrary user code)
- Per-VM kernel = no shared kernel attack surface
- Predictable cold start (~125ms) at high density (thousands per host)

## Real World Usage
- AWS Lambda (each invocation in a microVM)
- Fly.io Machines (one app = one Firecracker VM)
- Replit code execution
- Modal / E2B / sandbox products
- Cloud build runners

## Common Mistakes
- Treating it as Docker replacement for everything — overkill for trusted workloads
- Skipping the Jailer wrapper — defense-in-depth matters
- Misconfiguring vsock or networking, leaving VMs without internet (or worse, with everything)
- Ignoring snapshot warm-start opportunity → poor cold-start UX

## Prerequisites
- [[Linux Basics]] · [[Sandboxing]] · [[Docker]]

## What To Learn Next
- [[Remote Code Execution]] · [[AWS]] · [[Edge Computing]]

## Best Learning Resources

### Official Documentation
- [Firecracker docs](https://firecracker-microvm.github.io/) — concepts + getting started
- [GitHub — firecracker-microvm/firecracker](https://github.com/firecracker-microvm/firecracker)

### Best YouTube Resource
- [Re:Invent — Firecracker talks](https://www.youtube.com/results?search_query=aws+reinvent+firecracker) — production architecture
- [Hussein Nasser — Firecracker explained](https://www.youtube.com/@hnasr)

### Best Free Course
- [Firecracker 101 README](https://github.com/firecracker-microvm/firecracker/tree/main/docs) — official walkthroughs

### Best Advanced Resource
- [Fly.io blog — Firecracker in production](https://fly.io/blog/) — operational deep dives
- ["Firecracker: Lightweight Virtualization for Serverless Applications" paper (NSDI 2020)](https://www.usenix.org/conference/nsdi20/presentation/agache)
- [E2B blog — sandboxes for AI agents](https://e2b.dev/blog) — current usage patterns

### Best Practice Project
Boot Alpine in a Firecracker VM from a script. Configure 1 vCPU, 128MB, no networking. Run a "hello world" inside, then enable a single TCP port. Add the Jailer to harden the host side.

### Recommended Order to Learn
1. microVM concept vs container
2. Booting a VM from rootfs + kernel
3. Configuring devices (network, vsock)
4. Jailer + production hardening
5. Snapshots + warm starts
6. Operating at scale (orchestration around Firecracker)

## Interview Questions
**Q. Firecracker vs Docker — when do you pick which?**
A. Docker for trusted workloads (high density, lower overhead). Firecracker for hostile tenants where shared kernel is unacceptable.

**Q. How does Lambda achieve sub-100ms cold start at scale?**
A. Firecracker microVMs + snapshot/restore + warm pools.

**Q. Why is Firecracker minimal device emulation?**
A. Smaller attack surface; faster boot; no need for legacy devices in serverless.

**Q. What's the role of the Jailer?**
A. Wraps Firecracker itself in seccomp + namespaces + cgroups so even a Firecracker compromise is contained.

## Related
- [[Sandboxing]] · [[Remote Code Execution]] · [[AWS]] · [[Docker]]
