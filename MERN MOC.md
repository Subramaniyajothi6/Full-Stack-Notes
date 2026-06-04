---
tags: [moc, mern, index]
aliases: [MERN Index, Vault Home]
---

# MERN Stack — Master Map of Content

> Single entry point for the entire vault. Start here, branch into any section.

## How to use this vault

- **Atomic notes** — each note covers one idea. Skim quickly, link freely.
- **MOCs** — every section has its own MOC; this note links them all.
- **Canvas roadmaps** — visual dependency flows. Open the `.canvas` files in each section.
- **Levels** — notes are tagged `#beginner`, `#intermediate`, or `#advanced`.

## Sections

### Foundations
- [[JavaScript MOC|1. JavaScript]] — language fundamentals → async → OOP → DOM
- [[System Design MOC|6. System Design]] — how the web actually works

### Frontend
- [[React MOC|2. React]] — components, hooks, state, routing, performance

### Backend
- [[NodeJS MOC|3. NodeJS]] — runtime, modules, streams, async patterns
- [[Express MOC|4. Express]] — routing, middleware, auth, security
- [[MongoDB MOC|5. MongoDB]] — schemas, queries, aggregation, Mongoose

### Application
- [[Projects MOC|7. Projects]] — beginner → advanced builds
- [[Interview MOC|8. Interview Questions]] — topic-wise Q&A

### Modern Engineering
- [[Full Stack Infra MOC|9. Full Stack Infra]] — internet, dev env, frontend ecosystem, backend runtime, DBs, DevOps, AI, perf, languages, testing

## Master roadmaps (open in Obsidian Canvas)

- [[MERN Roadmap.canvas]] — MERN stack flow
- [[Full Stack Infra Roadmap.canvas]] — modern infra + AI ecosystem

## Suggested learning path

1. **Weeks 1–3** — Solidify [[JavaScript MOC|JavaScript]] (closures, prototypes, event loop, promises).
2. **Weeks 4–6** — Build with [[React MOC|React]] (hooks → state → router).
3. **Weeks 7–8** — Learn [[NodeJS MOC|Node]] internals + [[Express MOC|Express]] basics.
4. **Weeks 9–10** — [[MongoDB MOC|MongoDB]] + Mongoose, integrate with Express.
5. **Weeks 11–12** — Build a full-stack project from [[Projects MOC|Projects]].
6. **Weeks 13–16** — Layer in [[Full Stack Infra MOC|Full Stack Infra]] (Docker → CI/CD → AWS → AI).
7. **Ongoing** — [[System Design MOC|system design]] + [[Interview MOC|interview prep]].

## Tags glossary

- `#beginner` `#intermediate` `#advanced` — difficulty
- `#concept` `#syntax` `#pattern` `#pitfall` — note kind
- `#interview` — frequently asked
- `#infra` — cloud/devops/AI ecosystem
- `#ai` — AI engineering specific

## Note template (every atomic note)

Every note in this vault follows this shape:

1. **Title + frontmatter (tags)**
2. **One-line definition** under `>`
3. **Why it matters** — quick motivation
4. **Core ideas** — bullets / table
5. **Example** — practical code or diagram
6. **Real World Usage** — where you'll see it
7. **Common Mistakes** — pitfalls
8. **Prerequisites** — wiki-links to predecessor notes
9. **What To Learn Next** — wiki-links forward
10. **Best Learning Resources** — official docs · YouTube · free course · advanced · practice project · recommended order
11. **Interview Questions** — Q&A pairs
12. **Related** — adjacent notes

Existing JavaScript notes are minimal; new sections (React, Node, Express, Mongo, System Design, Projects, Interview, Full Stack Infra) follow the full template. A vault-wide upgrade script lives at [[upgrade-notes.py]] (run with Python 3) to append missing sections to older notes.

## Related

- [[MERN Roadmap.canvas]]
- [[Full Stack Infra Roadmap.canvas]]
- [[Projects MOC|Projects MOC]]
- [[Interview MOC|Interview MOC]]
