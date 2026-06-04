---
tags: [infra, performance, advanced]
---

# WASM

> WebAssembly — portable binary instruction format. Runs near-native speed in browsers, Node, edge runtimes, and standalone (wasmtime).

## Why it matters
Run C/C++/Rust/Go in the browser at native-ish speed. Sandboxed by design. Increasingly the runtime for edge functions and plugin systems.

## Core ideas
- **`.wasm` module** — compiled binary; can be loaded by JS, Node, wasmtime, etc.
- **Capability sandbox** — no syscalls without explicit imports → safe by default
- **Linear memory** — single contiguous bytes addressable from host and module
- **WASI** — system interface (files, env, time) for non-browser hosts
- **Component Model** — typed inter-module composition (newer)

## Real World Usage
- Browser: Figma renderer, Photoshop Web, FFmpeg.wasm, AutoCAD Web
- Edge: Fastly Compute@Edge, Shopify Functions, Cloudflare Workers (Rust→WASM)
- Plugins: Envoy (filters), TiDB, sandboxed user scripts
- ML: ONNX Runtime Web

## Common Mistakes
- Using WASM where JS is fast enough — added complexity
- Forgetting JS↔WASM boundary cost (frequent crossings = slow)
- Loading huge modules without streaming compilation
- Ignoring WASI — your module won't open files unless granted

## Prerequisites
- [[Browser Internals]] · [[Sandboxing]]

## What To Learn Next
- [[Edge Computing]] · [[Rust]] · [[Go]]

## Best Learning Resources

### Official Documentation
- [WebAssembly.org](https://webassembly.org/) — spec + tutorials
- [MDN — WebAssembly](https://developer.mozilla.org/en-US/docs/WebAssembly)
- [WASI docs](https://wasi.dev/)

### Best YouTube Resource
- [Fireship — WASM in 100 seconds](https://www.youtube.com/c/Fireship)
- [Hussein Nasser — WASM internals](https://www.youtube.com/@hnasr)
- [Bytecode Alliance talks](https://www.youtube.com/@BytecodeAlliance)

### Best Free Course
- [Rust + WebAssembly book](https://rustwasm.github.io/docs/book/) — official, free
- [WasmEdge tutorials](https://wasmedge.org/docs/) — server-side WASM

### Best Advanced Resource
- [Lin Clark — Code Cartoons on WASM](https://hacks.mozilla.org/category/code-cartoons/) — best conceptual diagrams
- [Component Model proposal docs](https://component-model.bytecodealliance.org/)

### Best Practice Project
Compile a Rust image-resize function to WASM, call it from a Next.js client to avoid round-trips. Then take the same WASM and run it on Cloudflare Workers. Measure size, cold start, and throughput.

### Recommended Order to Learn
1. Why WASM exists
2. Loading + calling from JS
3. Linear memory + boundary cost
4. WASI basics
5. Toolchains: emscripten, Rust+wasm-bindgen, AssemblyScript
6. Server-side WASM + Component Model

## Interview Questions
**Q. WASM vs JS — when faster?**
A. CPU-bound numerical code, image/audio/video processing, parsers. JS is faster for short-lived tasks dominated by JS↔WASM boundary cost.

**Q. Is WASM safe to run untrusted?**
A. Sandboxed by spec — no syscalls without imports. Combined with WASI capabilities, it's a strong sandbox model.

**Q. WASI vs browser WASM?**
A. Browser provides web APIs; WASI provides POSIX-like syscalls for server-side WASM in a portable way.

## Related
- [[Sandboxing]] · [[Edge Computing]] · [[Rust]]
