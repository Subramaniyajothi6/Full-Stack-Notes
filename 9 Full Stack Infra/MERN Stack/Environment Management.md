---
tags: [mern, deployment, intermediate]
---

# Environment Management

> Configuration that varies between environments (dev/stage/prod) — DB URIs, secrets, feature flags — managed safely.

## The hierarchy
```
1. Hard-coded constants    ← shouldn't change between envs
2. .env files              ← local dev convenience
3. Platform secret store   ← prod (Vercel envs, AWS SSM, Doppler, 1Password)
4. Runtime config service  ← dynamic flags (LaunchDarkly, GrowthBook)
```

## .env in dev
```bash
# .env (gitignored)
NODE_ENV=development
PORT=3001
MONGO_URI=mongodb://localhost:27017/myapp
JWT_SECRET=local-dev-secret-do-not-ship
S3_BUCKET=myapp-dev-uploads

# .env.example (committed, no real values)
MONGO_URI=
JWT_SECRET=
S3_BUCKET=
```

## Type-safe loader
```ts
import { z } from 'zod';
import 'dotenv/config';

const Env = z.object({
  NODE_ENV: z.enum(['development', 'test', 'production']),
  PORT: z.coerce.number().default(3001),
  MONGO_URI: z.string().url(),
  JWT_SECRET: z.string().min(32),
});
export const env = Env.parse(process.env);  // crashes loud on missing/invalid
```

## Where secrets actually live in prod
| Platform     | Secret store                                  |
|--------------|-----------------------------------------------|
| Vercel       | Project Settings → Environment Variables      |
| Render       | Service → Environment                          |
| AWS          | SSM Parameter Store / Secrets Manager          |
| GCP          | Secret Manager                                 |
| K8s          | Sealed Secrets / External Secrets Operator     |
| Self-hosted  | SOPS-encrypted YAML in repo                    |

## Per-stage configs (the right way)
- One **schema** validating env vars
- Three **value sets**: dev, staging, prod
- Same code, env-injected differences
- Never commit real secrets — even staging

## Real World Usage
- API keys (Stripe, Twilio, OpenAI)
- DB credentials
- Feature flags
- OAuth client IDs / secrets
- Per-region URL bases

## Common Mistakes
- Committing `.env` to git (use `.gitignore`!)
- Hardcoding "dev mode" workarounds (`if (process.env.NODE_ENV === 'development')` everywhere)
- Reading `process.env.X` deep in business logic — wrap in `env` module
- No validation → silent boot with broken config
- Sharing one `.env` file between teammates via Slack/Drive (use a vault: 1Password, Doppler)
- Logging the env on startup (leaks secrets to CloudWatch)
- Trusting frontend env vars (`VITE_*`, `NEXT_PUBLIC_*`) for secrets — they're public!

## Prerequisites
- [[Process and Environment]] · [[Deployment Architecture]] · [[Docker]]

## What To Learn Next
- [[Full-Stack CI CD]] · [[Logging Across Services]]

## Best Learning Resources

### Official Documentation
- [Twelve-Factor App — Config](https://12factor.net/config)
- [dotenv](https://github.com/motdotla/dotenv)
- [Doppler docs](https://docs.doppler.com/) — secret manager
- [Vercel — Environment Variables](https://vercel.com/docs/environment-variables)

### Best YouTube Resource
- [Theo — env management](https://www.youtube.com/@t3dotgg)
- [Hussein Nasser — secret rotation](https://www.youtube.com/@hnasr)

### Best Free Course
- [Twelve-Factor App](https://12factor.net/) — read end-to-end (free)
- [SOPS tutorial — Mozilla](https://github.com/getsops/sops)

### Best Advanced Resource
- [HashiCorp Vault](https://developer.hashicorp.com/vault/docs) — enterprise-grade secrets
- [AWS — secret rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)

### Best Practice Project
Take an existing MERN app: extract every `process.env.X` reference into one `env.ts` module with Zod validation. Add a startup check that crashes if env is invalid. Migrate prod secrets to Doppler or SSM. Document the dev onboarding flow.

### Recommended Order to Learn
1. `.env` + `.gitignore` + `.env.example`
2. Single typed env module
3. Per-stage configs
4. Cloud secret store
5. Secret rotation
6. Frontend env vars (and their security model)

## Interview Questions
**Q. How do you keep `.env` out of git?**
A. `.gitignore` it; commit `.env.example` with empty values. Pre-commit hook (gitleaks) for safety.

**Q. Why fail loud on missing env?**
A. A boot crash is easier to fix than a silent runtime error in production at 3am.

**Q. Why aren't `NEXT_PUBLIC_*` variables secret?**
A. They're inlined into the JS bundle the browser downloads. Anything client-side is public.

## Related
- [[Process and Environment]] · [[Docker]] · [[Deployment Architecture]] · [[Full-Stack CI CD]]
