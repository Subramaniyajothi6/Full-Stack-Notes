---
tags: [infra, language, advanced]
---

# Rust

> Systems language with memory safety without GC. Increasingly the language of fast tooling: Vite/Rolldown (Rolldown), SWC, Turbopack, Biome, Deno (parts), Cloudflare, Discord backend.

## Why it matters
Performance + safety + ergonomics combine in a way C/C++ never offered. Frontend tooling, databases, CLI tools, and WASM modules all increasingly Rust.

## Core ideas
- **Ownership** — every value has one owner; on scope-exit, dropped
- **Borrowing** — `&` shared (read), `&mut` exclusive; checked at compile time
- **Lifetimes** — compiler tracks how long references live
- **Traits** — typeclass-like generics
- **Enums + pattern matching** — sum types are first-class
- **No null, no exceptions** — `Option<T>`, `Result<T, E>`
- **Cargo** — built-in build/test/dependency manager

## Example
```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}

fn main() {
    let s = String::from("hello");
    let t = "world";
    println!("{}", longest(&s, t));
}
```

## Real World Usage
- Frontend tooling: SWC, Turbopack, Biome, Vite (parts), Rolldown
- Databases: TiKV, Materialize parts, sled, qdrant
- Cloud: Firecracker, Cloudflare Workers (parts)
- CLIs: ripgrep, fd, bat
- WASM modules

## Common Mistakes
- Fighting the borrow checker instead of redesigning ownership
- Cloning everywhere to bypass borrow rules
- Reaching for `unsafe` without justification
- Async without understanding `Send`/`Sync`/pinning
- Ignoring `Result` (`unwrap` in production)

## Prerequisites
- [[CLI]] · prior programming experience

## What To Learn Next
- [[WASM]] · [[Go]] · [[Sandboxing]]

## Best Learning Resources

### Official Documentation
- [The Rust Programming Language ("The Book")](https://doc.rust-lang.org/book/) — canonical, free
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
- [Rust Reference](https://doc.rust-lang.org/reference/)

### Best YouTube Resource
- [Jon Gjengset (Crust of Rust)](https://www.youtube.com/c/JonGjengset) — best deep-dive Rust channel
- [Let's Get Rusty](https://www.youtube.com/c/LetsGetRusty) — beginner-friendly
- [No Boilerplate](https://www.youtube.com/c/NoBoilerplate) — stylish primers

### Best Free Course
- [The Rust Book + Rustlings](https://github.com/rust-lang/rustlings) — book + exercises, official
- [Comprehensive Rust (Google)](https://google.github.io/comprehensive-rust/) — free course

### Best Advanced Resource
- [Programming Rust (book) — O'Reilly](https://www.oreilly.com/library/view/programming-rust-2nd/9781492052586/)
- [Tokio docs](https://tokio.rs/) — async ecosystem
- [Crust of Rust playlist](https://www.youtube.com/c/JonGjengset)

### Best Practice Project
Build a CLI tool in Rust (e.g., a fast log search like ripgrep-lite): traverses dirs, regex match, parallel via `rayon`, colored output via `crossterm`. Then port to WASM and call from a Next.js page.

### Recommended Order to Learn
1. The Book chapters 1–10 (ownership, borrows, lifetimes)
2. Cargo + Rustlings exercises
3. Traits + generics
4. Iterators + closures
5. Error handling (`?`, `anyhow`, `thiserror`)
6. Async with Tokio
7. WASM bindings via `wasm-bindgen`

## Interview Questions
**Q. What problem does ownership solve?**
A. Memory safety without GC — compiler enforces single owner + drop on scope exit, eliminating use-after-free and data races.

**Q. Difference between `Box`, `Rc`, `Arc`?**
A. `Box` = unique heap pointer. `Rc` = single-thread ref-counted shared. `Arc` = atomic ref-counted (thread-safe).

**Q. Why no exceptions?**
A. Errors are values (`Result<T, E>`); explicit handling. Panics exist for unrecoverable bugs.

**Q. What's `?` operator?**
A. Propagates `Err`/`None` upward — short-circuit error handling.

## Related
- [[WASM]] · [[Go]] · [[Sandboxing]]
