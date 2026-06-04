---
tags: [system-design, advanced, concept]
---

# OAuth Flow

> Delegated authorization. User grants a third-party app limited access without sharing password.

## Authorization Code (web)
1. App redirects user to provider with `client_id`, `scope`, `state`, optional PKCE `code_challenge`
2. User logs in + consents
3. Provider redirects back with `code`
4. Backend exchanges `code` (+ secret + PKCE verifier) for `access_token` (+ optionally `refresh_token`, `id_token`)
5. App uses `access_token` to call provider APIs

## PKCE
Required for public clients (SPAs, mobile). Replaces client secret.

## Common mistakes
- Validating `state` for CSRF — required
- Trusting `id_token` without signature verification
- Storing tokens insecurely

## Related
- [[OAuth in Express|OAuth in Express]] · [[Authentication vs Authorization]]

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

## Best Learning Resources

### Official Documentation
- https://aws.amazon.com/architecture/ — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. ByteByteGo, Hussein Nasser

### Best Free Course
- TODO

### Best Advanced Resource
- TODO

### Best Practice Project
- TODO: 1-paragraph project idea

### Recommended Order to Learn
1. TODO
2. TODO
3. TODO

## Interview Questions
**Q. TODO** — A. ...

**Q. TODO** — A. ...
