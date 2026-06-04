---
tags: [infra, devops, intermediate]
---

# Docker

> Container runtime: package an app + its deps + a slim Linux userspace into a portable image.

## Why it matters
Identical environment across dev / CI / prod. Foundation for Kubernetes, ECS, Cloud Run, Fly. The shipping container of software.

## Core ideas
- **Image** — read-only filesystem layers + metadata
- **Container** — running instance of an image (process + namespaces + cgroups)
- **Dockerfile** — declarative build recipe
- **Layer caching** — each instruction is a layer; reuse on rebuilds
- **Multi-stage build** — separate "builder" and "runtime" stages for slim images
- **Volume** — persistent storage outside container
- **Network** — bridge, host, overlay (Swarm/K8s)

## Dockerfile (slim Node)
```dockerfile
FROM node:20-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev

FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
COPY --from=deps /app/node_modules ./node_modules
COPY . .
USER node
EXPOSE 3000
CMD ["node", "server.js"]
```

## Real World Usage
- Local dev parity (`docker compose up`)
- CI runners
- Container orchestration (Kubernetes, ECS, Fly)
- Reproducible build artifacts

## Common Mistakes
- Running as root (default UID 0) — use `USER node` etc.
- Copying `node_modules` from host — host platform mismatch
- Not pinning base image (`FROM node:latest`) — surprise breakages
- Huge images because of single-stage build
- Mounting `/var/run/docker.sock` into containers (= root on host)
- No `.dockerignore` → secrets in image, slow builds

## Prerequisites
- [[Linux Basics]] · [[CLI]]

## What To Learn Next
- [[CI CD]] · [[Sandboxing]] · [[AWS]]

## Best Learning Resources

### Official Documentation
- [Docker docs](https://docs.docker.com/) — strong getting-started + reference
- [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)

### Best YouTube Resource
- [TechWorld with Nana — Docker Crash Course](https://www.youtube.com/c/TechWorldwithNana) — beginner-perfect
- [Bret Fisher — Docker for devs](https://www.youtube.com/c/BretFisherDockerCaptain)
- [Hussein Nasser — container internals](https://www.youtube.com/@hnasr)

### Best Free Course
- [Docker — Get Started](https://docs.docker.com/get-started/) — official walkthrough
- [Play with Docker labs](https://labs.play-with-docker.com/) — browser sandbox

### Best Advanced Resource
- [Containers from Scratch (Liz Rice)](https://github.com/lizrice/containers-from-scratch) — Go talk + source
- [BuildKit docs](https://docs.docker.com/build/buildkit/) — modern build engine

### Best Practice Project
Containerize a MERN app: multi-stage build for the React frontend (nginx-served), Node API container, MongoDB via official image, all wired with `docker compose`. Add a healthcheck, non-root user, `.dockerignore`, and a CI step that builds + scans the image.

### Recommended Order to Learn
1. Image vs container
2. Dockerfile + caching
3. Compose for multi-service
4. Volumes + networks
5. Multi-stage builds
6. Security: non-root, capabilities, scanning

## Interview Questions
**Q. Image vs container?**
A. Image is the static template; container is the running instance with its own writable layer.

**Q. Why are layer order and `COPY package.json` first useful?**
A. Caches deps install layer; only re-runs when deps change.

**Q. What is the OCI?**
A. Open Container Initiative — standardizes image and runtime specs across Docker, Podman, containerd.

**Q. How is Docker different from a VM?**
A. Containers share host kernel via namespaces+cgroups; VMs run a full guest kernel via hypervisor.

## Related
- [[CI CD]] · [[Sandboxing]] · [[Linux Basics]]
