---
tags: [infra, language, intermediate]
---

# Go

> Simple, fast, garbage-collected language designed at Google for backend services and tooling.

## Why it matters
The default language of cloud-native: Docker, Kubernetes, Terraform, Caddy, etcd, Prometheus, gRPC. Easy to learn, fast to compile, single binary deploys.

## Core ideas
- **Goroutines** — cheap, M:N scheduled lightweight threads
- **Channels** — typed CSP-style communication
- **Interfaces** — implicit (duck-typed satisfaction)
- **No exceptions** — explicit `error` returns
- **One binary** — fast compile, static link
- **Standard library is enormous** — http, json, crypto, testing built-in
- **Tooling baked in** — `go test`, `go vet`, `go fmt`, `go mod`

## Example
```go
package main

import (
  "fmt"
  "net/http"
  "time"
)

func main() {
  http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "hello at %s", time.Now())
  })
  http.ListenAndServe(":8080", nil)
}
```

## Real World Usage
- Microservices, gRPC APIs
- Cloud-native infra (Kubernetes, Terraform, Docker)
- CLIs (gh, helm, kubectl)
- Network tooling, proxies
- High-throughput servers

## Common Mistakes
- Goroutine leaks (no exit path) — always have a way to stop
- Unbuffered channels causing deadlocks
- Ignoring returned errors
- `interface{}` everywhere (use generics or proper types)
- Mutating maps from multiple goroutines without `sync.Mutex` / `sync.Map`

## Prerequisites
- [[CLI]] · prior programming experience

## What To Learn Next
- [[Docker]] · [[Rust]] · [[AWS]]

## Best Learning Resources

### Official Documentation
- [Go Documentation](https://go.dev/doc/) — concise
- [A Tour of Go](https://go.dev/tour/) — interactive intro
- [Effective Go](https://go.dev/doc/effective_go) — idiomatic guide

### Best YouTube Resource
- [Anthony GG — Go](https://www.youtube.com/c/anthonygg_) — practical
- [TechWorld with Nana — Go](https://www.youtube.com/c/TechWorldwithNana)
- [Just for Func (Francesc Campoy)](https://www.youtube.com/c/justforfunc) — older but excellent

### Best Free Course
- [Go by Example](https://gobyexample.com/) — best beginner-to-intermediate reference
- [Learn Go with tests](https://quii.gitbook.io/learn-go-with-tests/)

### Best Advanced Resource
- [The Go Programming Language (Kernighan & Donovan)](https://www.gopl.io/) — definitive book
- [Dave Cheney's blog](https://dave.cheney.net/) — patterns + perf
- [Go talks](https://go.dev/talks/) — official conference talks

### Best Practice Project
Build a small URL shortener: `net/http` server, BoltDB or Postgres storage, rate limiting middleware, Prometheus metrics, structured logs (slog). Add a Dockerfile + GitHub Actions to publish image.

### Recommended Order to Learn
1. Tour of Go
2. `go mod` + project layout
3. Goroutines + channels
4. Interfaces + composition
5. `net/http` + `database/sql`
6. Concurrency patterns (errgroup, context)
7. Generics

## Interview Questions
**Q. Goroutines vs threads?**
A. Goroutines are M:N scheduled by Go runtime, ~2KB stack initial, millions per process. OS threads are heavier.

**Q. Channels — when to use?**
A. Communication between goroutines, fan-in/fan-out, backpressure. For shared mutable state, prefer mutex.

**Q. Why no inheritance?**
A. Composition + interfaces. Encourages flat, simple type hierarchies.

**Q. `defer` use case?**
A. Cleanup at function exit (close files, unlock mutexes) — runs in reverse declaration order.

## Related
- [[Rust]] · [[Docker]] · [[CI CD]]
