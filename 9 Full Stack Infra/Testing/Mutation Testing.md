---
tags: [testing, advanced, quality]
---

# Mutation Testing

> Quality test for your tests. The tool mutates your code (changes `>` to `>=`, `+` to `-`); if tests still pass, your suite is weak there.

## Why coverage isn't enough
100% line coverage can mean every line executes but nothing's asserted. Mutation testing checks that tests actually *catch bugs*.

## Score
- **Mutation score** = killed mutations / total mutations
- Higher = better. ~75–85% is realistic for well-tested code

## Tools
- **Stryker** — JS/TS/.NET; the most popular
- **PIT** — Java
- **Cosmic Ray** — Python
- **mutmut** — Python

## Stryker quickstart
```bash
npx -p @stryker-mutator/core stryker init
npx stryker run
```

`stryker.conf.json`:
```json
{
  "testRunner": "vitest",
  "reporters": ["progress", "clear-text", "html"],
  "coverageAnalysis": "perTest"
}
```

## Where mutation testing pays off
- Critical financial / safety code
- Library code with many consumers
- Domain logic (pricing, scoring, eligibility)
- Crypto / parsing / validation

## Where it's overkill
- UI shells (use [[Visual Regression]] instead)
- Glue code
- Anything where 100% line coverage was wasteful too

## Real World Usage
- Pre-release quality gates
- Discovering "this test only runs the code, doesn't verify it"
- Test-suite maintenance triage (which tests actually help?)
- Comparing test approaches

## Common Mistakes
- Running mutation testing on huge codebases without filtering → hours-long runs
- Tracking mutation score as a vanity metric without acting on missed mutants
- Surviving mutants in trivial code (logging, getters) — exclude or accept
- Running on every PR (too slow) → schedule nightly / on touched modules

## Prerequisites
- [[Unit Testing]] · [[Vitest]] · [[Integration Testing]]

## What To Learn Next
- [[Contract Testing]] · [[Visual Regression]]

## Best Learning Resources

### Official Documentation
- [Stryker docs](https://stryker-mutator.io/docs/)
- [Pitest docs](https://pitest.org/)

### Best YouTube Resource
- [Stryker YouTube](https://www.youtube.com/results?search_query=stryker+mutator)

### Best Free Course
- [Stryker Quickstart](https://stryker-mutator.io/docs/stryker-js/getting-started/)

### Best Advanced Resource
- ["Mutation testing in industry" — Google engineering blog](https://research.google/pubs/state-of-mutation-testing-at-google/)

### Best Practice Project
Run Stryker on a domain module (e.g., pricing logic). Identify the top 5 surviving mutants. Write tests that kill them. Recompute the mutation score.

### Recommended Order to Learn
1. Run Stryker once on a small module
2. Read the HTML report
3. Kill obvious surviving mutants
4. Exclude trivial code
5. Schedule in CI (nightly)
6. Track score over time for critical modules

## Interview Questions
**Q. Why isn't line coverage enough?**
A. Coverage measures execution. Mutation testing measures *detection* — your tests must fail when the code is wrong.

**Q. When NOT to use mutation testing?**
A. UI shells, glue code, anything where 100% coverage was already overkill. Reserve it for high-value domain logic.

## Related
- [[Unit Testing]] · [[Vitest]] · [[Contract Testing]] · [[Visual Regression]]
