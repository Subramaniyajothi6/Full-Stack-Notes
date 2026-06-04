---
tags: [mern, deployment, intermediate]
---

# Feature Flags

> Decouple deploy from release. Ship code dark, turn it on for some users, ramp up, roll back without redeploying.

## What flags enable
- **Progressive rollouts** — 1% → 10% → 100%
- **Kill switches** — disable a feature without a deploy
- **A/B experiments** — assign variants, measure, decide
- **Trunk-based dev** — merge half-built features behind a flag
- **Per-user / per-tenant beta access**

## Tools
- **LaunchDarkly** — gold standard, paid
- **GrowthBook** — open-source, self-hostable
- **Statsig** — analytics + flags combined
- **PostHog** — analytics + flags + replays
- **Unleash** — open-source
- **Custom in-house** — fine for simple cases (DB-backed config)

## Server-side example
```ts
import { GrowthBook } from '@growthbook/growthbook';

const gb = new GrowthBook({ attributes: { id: req.user.sub, tenantId: req.tenant.id } });
await gb.loadFeatures();

if (gb.isOn('new-checkout')) {
  return await newCheckout(req);
}
return await legacyCheckout(req);
```

## Client-side example
```tsx
const { isOn } = useGrowthBook();
return isOn('new-dashboard') ? <NewDashboard /> : <OldDashboard />;
```

## Flag hygiene
- **Name flags clearly** — `new-checkout`, not `flag1`
- **Set an expiry** — every flag should have an owner + remove-by date
- **Monitor flag age** — old flags are tech debt and risk
- **Remove dead flags** in a quarterly cleanup
- Document the **default** behavior when the flag service is unreachable

## Real World Usage
- Risky migrations behind a flag (revert without redeploy)
- Beta program (internal team / paid tier / specific tenants)
- A/B test new UX or pricing
- Maintenance mode toggle
- Per-region rollouts

## Common Mistakes
- Flags that never get removed — accumulate as permanent forks of behavior
- No default — flag service down = unpredictable behavior
- Boolean flags for what should be a config value (e.g., timeout amount → use a string flag, not boolean)
- Reading flag inside a tight loop (cache the value)
- Coupling flags to business logic (better: flags switch *which implementation* runs)
- No analytics tying flag to outcome (you can't measure the experiment)

## Prerequisites
- [[Full-Stack CI CD]] · [[Environment Management]] · [[Multi-Tenant Patterns]]

## What To Learn Next
- [[Webhooks]] · [[File Upload Pipeline]]

## Best Learning Resources

### Official Documentation
- [LaunchDarkly docs](https://docs.launchdarkly.com/)
- [GrowthBook docs](https://docs.growthbook.io/)
- [PostHog feature flags](https://posthog.com/docs/feature-flags)
- [Unleash docs](https://docs.getunleash.io/)

### Best YouTube Resource
- [Theo — feature flags & A/B testing](https://www.youtube.com/@t3dotgg)
- [LaunchDarkly Tech Talks](https://www.youtube.com/@LaunchDarkly)

### Best Free Course
- [Martin Fowler — Feature Toggles essay](https://martinfowler.com/articles/feature-toggles.html) — the canonical text
- [GrowthBook quickstart](https://docs.growthbook.io/quick-start)

### Best Advanced Resource
- ["Feature Flag Best Practices" — O'Reilly free PDF (LaunchDarkly)](https://learn.launchdarkly.com/feature-flag-best-practices/)
- [Statsig engineering blog](https://www.statsig.com/blog) — experiment design

### Best Practice Project
Add GrowthBook to a MERN app. Hide a refactored route behind a flag. Roll out 10% → 50% → 100% with metrics on error rate. Then add an A/B experiment on a marketing button copy.

### Recommended Order to Learn
1. Boolean kill switches
2. Percentage rollouts
3. Targeting (user, tenant, region)
4. A/B experimentation + statistical significance
5. SDK reliability + defaults
6. Flag lifecycle (creation → cleanup)

## Interview Questions
**Q. Difference between deploy and release?**
A. Deploy = code in production. Release = users see the new behavior. Flags decouple them.

**Q. Why is flag cleanup important?**
A. Stale flags become silent forks of code paths — bugs hide in unused branches.

**Q. How does a percentage rollout assign users?**
A. Hash user id; if `hash(user.id) % 100 < pct`, the flag is on. Stable across requests.

## Related
- [[Full-Stack CI CD]] · [[Multi-Tenant Patterns]] · [[Logging Across Services]]
