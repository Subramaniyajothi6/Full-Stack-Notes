---
tags: [cloud, intermediate, security]
---

# Secrets Management

> Centralized storage for API keys, DB credentials, TLS keys — encrypted at rest, audited, rotated.

## Tools
- **AWS SSM Parameter Store** — cheap, secure strings, basic
- **AWS Secrets Manager** — rotation, cross-account, JSON secrets
- **GCP Secret Manager** — similar
- **Azure Key Vault** — Azure-native
- **HashiCorp Vault** — multi-cloud, enterprise-grade
- **Doppler / 1Password / Infisical** — dev-friendly + sync
- **SOPS + KMS** — encrypted YAML in repo

## Patterns
- **App boot** — fetch secrets once via SDK, cache in memory
- **K8s** — External Secrets Operator syncs cloud secrets → K8s secrets
- **CI** — OIDC to cloud → assume role → fetch secrets
- **Local dev** — Doppler / 1Password CLI injects env

## Rotation
- DB creds rotate every 30–90 days with Secrets Manager
- Apps re-fetch on auth failure
- Multi-version retrieval during cutover

## Real World Usage
- Stripe API keys, Twilio tokens, OpenAI keys
- DB user passwords with automated rotation
- TLS private keys for nginx / Envoy
- JWT signing keys
- Webhook signing secrets

## Common Mistakes
- Secrets in `.env` committed to git
- Long-lived static secrets that never rotate
- Logging the secret on startup (`console.log(env)`)
- One secret shared by many services — blast radius huge
- No audit trail (who accessed what, when)
- App caches a secret forever then breaks after rotation

## Prerequisites
- [[AWS]] · [[IAM and Least Privilege]] · [[Environment Management]]

## What To Learn Next
- [[Cost Optimization]] · [[Logging Across Services]]

## Best Learning Resources

### Official Documentation
- [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/)
- [SSM Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)
- [HashiCorp Vault](https://developer.hashicorp.com/vault/docs)
- [Doppler docs](https://docs.doppler.com/)

### Best YouTube Resource
- [TechWorld with Nana — Vault + cloud secrets](https://www.youtube.com/c/TechWorldwithNana)
- [Anton Putra — Secrets Manager](https://www.youtube.com/c/AntonPutra)

### Best Free Course
- [HashiCorp Learn — Vault](https://developer.hashicorp.com/vault/tutorials)
- [SOPS GitHub repo + examples](https://github.com/getsops/sops)

### Best Advanced Resource
- [Bridgecrew / Snyk — secret scanning patterns](https://snyk.io/blog/)
- [Cloud Security Alliance guides](https://cloudsecurityalliance.org/)

### Best Practice Project
Migrate a project's `.env` to AWS Secrets Manager. Wire app boot to fetch via SDK. Add automatic DB password rotation. Verify with gitleaks that no secret ever lands in the repo.

### Recommended Order to Learn
1. `.env` + gitignore + gitleaks
2. SSM Parameter Store basics
3. Secrets Manager + rotation
4. External Secrets Operator for K8s
5. Doppler / Infisical for dev sync
6. Vault for multi-cloud or enterprise

## Interview Questions
**Q. Why is `.env` insufficient for prod?**
A. No rotation, no audit, often committed accidentally, no per-service access control.

**Q. SSM Parameter Store vs Secrets Manager?**
A. SSM is cheaper + simpler. Secrets Manager adds rotation, multi-region, KMS-tight integration, longer-lived versions.

**Q. How do CI pipelines fetch secrets without static keys?**
A. OIDC federation — GitHub Actions presents an OIDC token to AWS / GCP; STS issues short-lived credentials.

## Related
- [[IAM and Least Privilege]] · [[Environment Management]] · [[CI CD]]
