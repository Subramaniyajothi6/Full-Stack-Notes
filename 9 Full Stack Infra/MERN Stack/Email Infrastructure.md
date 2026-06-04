---
tags: [mern, integration, intermediate]
---

# Email Infrastructure

> Sending mail reliably from your backend — transactional (auth, receipts, alerts) and marketing — without ending up in spam.

## Transactional vs marketing
| Type            | Examples                       | Tools                              |
|-----------------|--------------------------------|------------------------------------|
| Transactional   | Verify, reset, receipt         | Resend, Postmark, Sendgrid, SES    |
| Marketing       | Newsletters, drip campaigns    | Loops, Customer.io, Mailchimp, Beehiiv |

Transactional needs **fast, reliable, never-spam-flagged** delivery.

## Modern transactional stack
- **Resend** — DX-first, React-Email templates
- **Postmark** — best deliverability, plain-text-friendly
- **Amazon SES** — cheapest at scale, more setup
- **SendGrid / Mailgun** — older incumbents

## React Email + Resend example
```tsx
// emails/Welcome.tsx
import { Html, Head, Body, Container, Heading, Text, Button } from '@react-email/components';

export default function Welcome({ name, verifyUrl }: { name: string; verifyUrl: string }) {
  return (
    <Html>
      <Head />
      <Body style={{ fontFamily: 'sans-serif' }}>
        <Container>
          <Heading>Welcome, {name}!</Heading>
          <Text>Click below to verify your email:</Text>
          <Button href={verifyUrl}>Verify email</Button>
        </Container>
      </Body>
    </Html>
  );
}
```

```ts
// services/email.ts
import { Resend } from 'resend';
import Welcome from '../emails/Welcome';

const resend = new Resend(process.env.RESEND_API_KEY);

export async function sendWelcome(to: string, name: string, verifyUrl: string) {
  await resend.emails.send({
    from: 'auth@app.example.com',
    to,
    subject: 'Verify your email',
    react: Welcome({ name, verifyUrl }),
  });
}
```

Always queue the actual send via [[Background Jobs]] so the request returns instantly.

## Deliverability essentials
- **SPF, DKIM, DMARC** DNS records — prove you own the sending domain
- **Dedicated sending domain** (`mail.app.com`), not your apex
- **Warm up gradually** — don't blast 10k from a brand-new domain
- **Bounce + complaint handling** — auto-suppress repeats
- **Clear unsubscribe** for any non-transactional content (CAN-SPAM / GDPR)
- **Plain-text version** alongside HTML

## Real World Usage
- Email verification on signup
- Password reset
- Magic-link login
- Order receipts, shipping notifications
- Weekly digests
- Team invitations
- Incident notifications

## Common Mistakes
- Sending from the apex domain (one bad campaign trashes your main domain reputation)
- Skipping SPF/DKIM/DMARC → straight to spam folder
- Sending synchronously in the request → 3-second sign-ups
- No retry queue → emails lost on transient errors
- Logging full email body (PII / spam-triggers in logs)
- Not handling bounces (keeps sending to bad addresses → reputation hit)
- Hardcoding email content (HTML strings in TS) — use React Email or MJML
- No dev-mode preview (Mailtrap / Postmark sandbox)

## Prerequisites
- [[Background Jobs]] · [[Full-Stack Auth Flow]] · [[Environment Management]] · [[DNS]]

## What To Learn Next
- [[Stripe Integration]] · [[Webhooks]]

## Best Learning Resources

### Official Documentation
- [Resend docs](https://resend.com/docs)
- [React Email](https://react.email/)
- [Postmark — Rebel's Guide to Email Marketing (free)](https://postmarkapp.com/guides)
- [AWS SES docs](https://docs.aws.amazon.com/ses/)

### Best YouTube Resource
- [Theo — Resend & React Email](https://www.youtube.com/@t3dotgg)
- [Postmark YouTube — deliverability](https://www.youtube.com/@postmarkapp)

### Best Free Course
- [Mail Tester](https://www.mail-tester.com/) — test deliverability + DNS
- [Sender Score guides](https://www.senderscore.org/) — reputation explainers

### Best Advanced Resource
- [Postmark blog](https://postmarkapp.com/blog) — deep deliverability content
- [Email Geeks Slack](https://email.geeks.chat/) — community of deliverability experts

### Best Practice Project
Set up a custom subdomain `mail.example.com` with SPF + DKIM + DMARC. Send via Resend with React Email templates. Queue every send. Add bounce-handling (Resend webhook → suppression list). Track opens/clicks with consent.

### Recommended Order to Learn
1. Pick a provider (Resend or Postmark)
2. Authenticate sending domain (SPF / DKIM)
3. Templating (React Email / MJML)
4. Queue all sends
5. DMARC + reporting
6. Bounce + complaint handling
7. Marketing / sequence tools (Customer.io, Loops)

## Interview Questions
**Q. Why send through a provider instead of your own SMTP?**
A. IP reputation, deliverability, bounce handling, suppressions, compliance — all hard. Providers earn this.

**Q. SPF / DKIM / DMARC — what do they do?**
A. SPF lists allowed senders for a domain. DKIM signs the message. DMARC tells receivers what to do when SPF/DKIM fail and reports back to you.

**Q. Why queue email sends?**
A. Provider hiccups shouldn't fail user requests; retries belong in a queue.

## Related
- [[Background Jobs]] · [[Full-Stack Auth Flow]] · [[Webhooks]] · [[DNS]]
