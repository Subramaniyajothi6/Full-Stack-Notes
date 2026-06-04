---
tags: [moc, devops]
---

# DevOps MOC

> Operating, shipping, and securing software in production. Containers, IaC, CI/CD, runtime sandboxing, and command-line tooling.

## Containers + orchestration
- [[Docker]] — images, layers, multi-stage builds
- [[Sandboxing]] — namespaces, cgroups, seccomp, gVisor
- [[Firecracker]] — KVM microVMs for hostile multi-tenant
- [[Remote Code Execution]] — running untrusted code safely
- [[DoS Protection]] — rate limits, timeouts, ReDoS, body limits

## CI/CD
- [[CI CD]] — pipelines, secrets, artifacts, environments

## Infrastructure as Code
- [[Terraform]] — HCL, state, modules
- [[Pulumi]] — IaC in TS / Python / Go

## Runtime / performance
- [[WASM]] — portable sandboxed binary modules
- [[FFmpeg]] — audio/video pipelines

## Command-line + Linux
- [[CLI]] — pipes, redirection, filters
- [[Linux Basics]] — filesystem, processes, services
- [[Shell Commands]] — top-30 commands cheat sheet

## Languages (used heavily in DevOps tooling)
- [[Rust]] — Firecracker, ripgrep, modern frontend tooling
- [[Go]] — Docker, Kubernetes, Terraform, gRPC

## Suggested order
1. [[Linux Basics]] → [[CLI]] → [[Shell Commands]]
2. [[Docker]] → [[CI CD]]
3. [[Terraform]] (or [[Pulumi]])
4. [[Sandboxing]] → [[Firecracker]] → [[Remote Code Execution]]
5. [[WASM]] · [[FFmpeg]] · [[Rust]] · [[Go]] (per project need)

## Roadmap to fill in
- [ ] Kubernetes + Helm
- [ ] Service mesh (Istio / Linkerd)
- [ ] Observability (Prometheus, Grafana, OpenTelemetry, Sentry)
- [ ] Secrets management (Vault, SOPS)
- [ ] Git + GitHub workflows
- [ ] Argo CD / GitOps

## Related stacks
- [[Cloud MOC]] · [[CI CD]] · [[Testing MOC]]

## Related
- [[Full Stack Infra MOC]] · [[MERN MOC]]
