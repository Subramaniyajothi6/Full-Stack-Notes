---
tags: [infra, cloud, intermediate]
---

# GCP

> Google Cloud Platform. Strong in containers (GKE), data/ML (BigQuery, Vertex AI), and developer experience (Cloud Run).

## Why it matters
Cleanest serverless container experience (Cloud Run), best managed Kubernetes (GKE), and BigQuery defines the data-warehouse benchmark.

## Core building blocks
- **Compute** — Compute Engine (VMs), Cloud Run (serverless containers), Cloud Functions, GKE
- **Storage** — Cloud Storage (objects), Persistent Disk
- **Database** — Cloud SQL (Postgres/MySQL), Spanner (global SQL), Firestore (document), BigQuery (analytics)
- **Networking** — VPC, Cloud Load Balancing, Cloud CDN, Cloud DNS
- **Identity** — IAM, Identity Platform (end-user)
- **Messaging** — Pub/Sub, Eventarc
- **AI** — Vertex AI, Gemini API
- **Observability** — Cloud Logging, Cloud Monitoring, Cloud Trace

## Why teams pick GCP
- Cloud Run for "stateless containers in 30 seconds"
- BigQuery for ad-hoc analytics over TB
- GKE Autopilot — opinionated managed K8s
- Spanner for global strongly-consistent SQL

## Real World Usage
- Spotify, Twitter, Snap — heavy GCP users
- Data + ML workloads at scale
- Containerized SaaS via Cloud Run

## Common Mistakes
- Treating Cloud Run like a long-running server (it's stateless; instances cycle)
- Default service accounts with broad perms — apply least privilege
- Forgetting region pinning → unexpected egress
- Ignoring BigQuery query cost (TB scanned) — cluster + partition tables

## Prerequisites
- [[Linux Basics]] · [[Docker]]

## What To Learn Next
- [[AWS]] · [[Azure]] · [[Terraform]] · [[CI CD]]

## Best Learning Resources

### Official Documentation
- [Google Cloud Docs](https://cloud.google.com/docs)
- [Cloud Run docs](https://cloud.google.com/run/docs)
- [BigQuery docs](https://cloud.google.com/bigquery/docs)

### Best YouTube Resource
- [Google Cloud Tech](https://www.youtube.com/c/GoogleCloudTech) — official
- [TechWorld with Nana — GCP series](https://www.youtube.com/c/TechWorldwithNana)

### Best Free Course
- [Qwiklabs Free Tier (Cloud Skills Boost)](https://www.cloudskillsboost.google/) — hands-on labs
- [Google Cloud Skills Boost — Foundations](https://www.cloudskillsboost.google/journeys)

### Best Advanced Resource
- [Site Reliability Engineering (SRE) book — free](https://sre.google/books/) — Google's ops bible
- [GCP architecture center](https://cloud.google.com/architecture) — patterns

### Best Practice Project
Deploy a containerized API to Cloud Run, store data in Cloud SQL Postgres, push events to Pub/Sub, log into Cloud Logging. Wire CI from GitHub Actions to gcloud deploy. Add BigQuery analytics over an event log table.

### Recommended Order to Learn
1. IAM + projects + billing
2. Cloud Storage + Cloud SQL
3. Cloud Run
4. VPC + load balancing
5. BigQuery basics
6. GKE + advanced services

## Interview Questions
**Q. Cloud Run vs Cloud Functions?**
A. Cloud Run = container, any language, request-based scaling, more flexible. Cloud Functions = single-function, simpler, more event-bindings.

**Q. Why is BigQuery so fast?**
A. Columnar storage, massively parallel execution (Dremel), separation of storage + compute.

**Q. What's Spanner's claim to fame?**
A. Globally distributed strongly-consistent SQL via TrueTime (atomic clocks + GPS).

## Related
- [[AWS]] · [[Azure]] · [[Terraform]]
