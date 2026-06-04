---
tags: [mern, integration, intermediate]
---

# Webhooks

> Event-driven HTTP callbacks. Two flavors: **incoming** (you receive from Stripe, GitHub, Twilio) and **outgoing** (you fire to your customers' systems).

## Incoming webhooks (you're the receiver)

### Verify signatures (always)
```ts
import crypto from 'crypto';

app.post('/webhooks/stripe',
  express.raw({ type: 'application/json' }),       // raw body required
  (req, res) => {
    const sig = req.headers['stripe-signature'];
    let event;
    try {
      event = stripe.webhooks.constructEvent(req.body, sig, STRIPE_WEBHOOK_SECRET);
    } catch (err) {
      return res.status(400).send(`bad signature: ${err.message}`);
    }
    // … handle event
    res.json({ received: true });
  }
);
```

### Idempotency
Webhook providers retry. Same event id can arrive multiple times.
```ts
async function handleEvent(event) {
  const existing = await ProcessedEvent.findOne({ providerEventId: event.id });
  if (existing) return;                            // already processed
  await ProcessedEvent.create({ providerEventId: event.id });
  await dispatch(event);
}
```

### Respond fast, work async
Webhook senders time out at 5–30s. Acknowledge with 200 immediately, do the heavy work in a background job ([[Background Jobs]]).

## Outgoing webhooks (you're the sender)

### Per-tenant subscriptions
```ts
const Webhook = {
  tenantId, url, secret, events: ['invoice.paid', 'user.created'],
  active: true, failures: 0
};
```

### Sign your payloads
```ts
const sig = crypto.createHmac('sha256', wh.secret).update(payload).digest('hex');
await fetch(wh.url, {
  method: 'POST',
  headers: { 'X-Signature': sig, 'X-Event-Id': eventId },
  body: payload,
  signal: AbortSignal.timeout(10_000),
});
```

### Retry policy
- Exponential backoff: 1m, 5m, 30m, 2h, 12h, 24h
- Cap at N retries
- Disable subscription after sustained failure; notify customer

## Real World Usage
- **Incoming**: Stripe payment events, GitHub PR events, Slack slash commands, Twilio SMS delivery
- **Outgoing**: notifying customers of order status, integrations they configure (Zapier-style)
- ETL triggers
- Cross-service event propagation

## Common Mistakes
- **No signature verification** → spoofed webhooks
- Heavy work in the handler → timeouts → retry storms
- **Not idempotent** → double charges, double notifications
- Returning 4xx for transient errors (the sender stops retrying!) — use 5xx for "try again"
- Storing webhook URLs in plaintext (encrypt the customer-provided secret)
- No replay UI for the customer — when they miss events, they need a way to refetch
- Synchronous fan-out to many subscribers — first slow subscriber blocks others; use a queue

## Prerequisites
- [[Express MOC]] · [[Background Jobs]] · [[Full-Stack Auth Flow]]

## What To Learn Next
- [[File Upload Pipeline]] · [[Stripe Integration]]

## Best Learning Resources

### Official Documentation
- [Stripe Webhooks](https://docs.stripe.com/webhooks)
- [GitHub Webhooks](https://docs.github.com/en/webhooks)
- [Svix docs](https://docs.svix.com/) — webhook-as-a-service for outgoing

### Best YouTube Resource
- [Hussein Nasser — webhooks vs polling](https://www.youtube.com/@hnasr)
- [Theo — webhook patterns](https://www.youtube.com/@t3dotgg)

### Best Free Course
- [Stripe webhook docs walkthrough](https://docs.stripe.com/webhooks)
- [Hookdeck — webhook engineering blog (free)](https://hookdeck.com/blog)

### Best Advanced Resource
- [Svix engineering blog](https://www.svix.com/blog/) — webhook infrastructure deep dives
- [Stripe engineering — webhook delivery at scale](https://stripe.com/blog/online-migrations)

### Best Practice Project
Build both sides: (1) an Express endpoint that receives Stripe webhooks (test mode), verifies signatures, dedupes by event id, records to DB. (2) An outgoing webhook system that lets a tenant register a URL + secret and receives `order.created` events with retry on failure.

### Recommended Order to Learn
1. Verify signatures
2. Idempotency / dedup
3. Async processing (queue)
4. Outgoing subscription model
5. Signing + secrets per subscriber
6. Retry strategy + backoff
7. Replay / dashboard UI

## Interview Questions
**Q. Why verify signatures?**
A. Without them, anyone can POST a fake event to your webhook URL — could trigger refunds, account changes, etc.

**Q. Webhooks vs polling?**
A. Webhooks are push (real-time, fewer requests); polling is pull (simpler, but lag + waste). Webhooks need failure handling; polling is naturally idempotent.

**Q. Why must handlers be idempotent?**
A. Senders retry. Same event arrives multiple times. Non-idempotent handlers double-charge / double-process.

## Related
- [[Background Jobs]] · [[Stripe Integration]] · [[File Upload Pipeline]] · [[Express MOC]]
