---
tags: [mern, integration, intermediate]
---

# Stripe Integration

> Accepting payments end-to-end: client collects card → server creates intent → webhook confirms → DB records → fulfillment.

## Two main shapes
- **One-time payment** — `PaymentIntent`
- **Subscriptions** — `Customer` + `Price` + `Subscription`

## One-time payment flow
```
1. Client calls /api/payments/create-intent { amount, currency }
2. Server creates PaymentIntent, returns clientSecret
3. Client uses Stripe.js / Payment Element to collect card + confirm
4. Stripe charges card → fires webhook payment_intent.succeeded
5. Server's webhook handler marks order as paid → triggers fulfillment
```

### Server
```ts
import Stripe from 'stripe';
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!);

app.post('/api/payments/create-intent', requireAuth, async (req, res) => {
  // RE-PRICE on server. Never trust client amount.
  const cart = await Cart.findOne({ userId: req.user.sub });
  const amount = computeTotal(cart);
  const intent = await stripe.paymentIntents.create({
    amount, currency: 'usd',
    metadata: { userId: req.user.sub, cartId: cart.id },
  });
  res.json({ clientSecret: intent.client_secret });
});
```

### Client (Stripe.js + Payment Element)
```tsx
const stripe = useStripe(); const elements = useElements();
async function pay() {
  const { error } = await stripe!.confirmPayment({
    elements: elements!,
    confirmParams: { return_url: window.location.origin + '/orders/success' },
  });
}
```

### Webhook (the source of truth)
```ts
app.post('/webhooks/stripe',
  express.raw({ type: 'application/json' }),
  async (req, res) => {
    let event;
    try {
      event = stripe.webhooks.constructEvent(req.body, req.headers['stripe-signature']!, STRIPE_WEBHOOK_SECRET);
    } catch (e) { return res.status(400).send(`bad sig`); }

    // Dedup
    if (await ProcessedEvent.findOne({ providerEventId: event.id })) return res.json({ ok: 1 });
    await ProcessedEvent.create({ providerEventId: event.id });

    if (event.type === 'payment_intent.succeeded') {
      const intent = event.data.object as Stripe.PaymentIntent;
      await Order.findOneAndUpdate(
        { stripeIntentId: intent.id, status: 'pending' },
        { $set: { status: 'paid' } }
      );
      await fulfillmentQueue.add('ship', { orderId: ... });
    }
    res.json({ received: true });
  }
);
```

## Subscriptions essentials
- Create a `Customer` for each user
- Use Stripe `Price` objects (not raw amounts) for plans
- Use `Checkout Session` (`mode: 'subscription'`) for the easiest UI
- Webhook events: `customer.subscription.created`, `.updated`, `.deleted`, `invoice.paid`, `invoice.payment_failed`
- Respect "trial", "past_due", "canceled" states in your UI

## Real World Usage
- E-commerce checkout
- SaaS subscriptions (monthly / annual)
- Marketplaces (Stripe Connect for split payments)
- Donations
- One-click upgrade flows

## Common Mistakes
- **Trusting the amount sent by the client** — re-price on server every time
- Treating client-side `confirmPayment` success as authoritative — always wait for the webhook
- Not handling the webhook idempotently → double-fulfillment
- Decrementing inventory before payment confirmation
- Storing card data yourself (PCI scope nightmare; let Stripe handle it)
- Hardcoding prices — use Stripe `Price` ids
- Not implementing `invoice.payment_failed` handling for subs (silent churn)
- Sending emails from the request handler instead of the webhook handler (the request can succeed but webhook fail / vice versa)

## Prerequisites
- [[Webhooks]] · [[Background Jobs]] · [[Full-Stack Auth Flow]]

## What To Learn Next
- [[Email Infrastructure]] · [[Multi-Tenant Patterns]]

## Best Learning Resources

### Official Documentation
- [Stripe Docs](https://docs.stripe.com/) — best in the industry
- [Stripe API Reference](https://docs.stripe.com/api)
- [Stripe testing cards](https://docs.stripe.com/testing)

### Best YouTube Resource
- [Stripe Developers (official)](https://www.youtube.com/c/StripeDevelopers)
- [Theo — Stripe deep dives](https://www.youtube.com/@t3dotgg)
- [Web Dev Cody — Stripe + Next.js](https://www.youtube.com/@WebDevCody)

### Best Free Course
- [Stripe Quickstarts](https://docs.stripe.com/quickstart)
- [Stripe Apps + sample repos](https://github.com/stripe/stripe-node) — full examples

### Best Advanced Resource
- [Stripe blog — engineering posts](https://stripe.com/blog/engineering)
- ["Stripe's API Quality" — Brandur Leach](https://brandur.org/) — deep API design

### Best Practice Project
Build subscription billing for a MERN SaaS: Customer creation, Checkout Session redirect, webhooks update local subscription state, gated features, customer portal for self-service. Test cards including 3DS challenges and `invoice.payment_failed`.

### Recommended Order to Learn
1. PaymentIntent + Stripe.js for one-time
2. Webhooks + signature verification + idempotency
3. Customer + Subscription + Checkout Session
4. Customer Portal
5. Subscription lifecycle events
6. Stripe Connect (multi-party payments)
7. PCI compliance basics

## Interview Questions
**Q. Why is the webhook the source of truth, not the client confirm?**
A. The browser may close, lose connectivity, or be tampered with after `confirmPayment` resolves. The webhook is the verified server-to-server confirmation.

**Q. Why re-price on server?**
A. Anything from the client is untrusted. Anyone can edit a hidden `amount` field.

**Q. How do you avoid double-fulfilling an order?**
A. Idempotency in webhook handlers (dedup by event id) + atomic `findOneAndUpdate` with the pending precondition.

## Related
- [[Webhooks]] · [[Background Jobs]] · [[Email Infrastructure]] · [[Multi-Tenant Patterns]] · [[Full-Stack Auth Flow]]
