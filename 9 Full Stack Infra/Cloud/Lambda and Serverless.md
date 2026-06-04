---
tags: [cloud, intermediate, compute]
---

# Lambda and Serverless

> Run code in response to events without managing servers. Pay per invocation + memory × duration.

## Models
- **AWS Lambda** — original; broad ecosystem
- **Cloudflare Workers** — V8 isolates at edge — see [[Edge Computing]]
- **Vercel Edge / Functions** — Next-native serverless
- **Cloud Run (GCP)** — container-as-function
- **Azure Functions**
- **Fly Machines / AWS Fargate** — serverless containers (long-running)

## Lambda anatomy
- **Handler** — entry function `(event, context) => result`
- **Runtime** — Node 20, Python, Go, custom
- **Memory** — 128 MB – 10 GB (CPU scales with memory)
- **Timeout** — up to 15 min
- **Concurrency** — auto-scales per concurrent request
- **Reserved / Provisioned concurrency** — caps + warm pools
- **Triggers** — API Gateway, SQS, EventBridge, S3, DynamoDB streams

## Cold starts
First invocation per container instance pays init cost. Mitigate:
- Smaller deployment package
- Lighter runtime (Node, Go > Java/JVM)
- Provisioned concurrency for latency-critical paths
- Avoid heavy init outside handler
- Lambda SnapStart (Java)

## Async event sources
- **SQS** — at-least-once; max concurrency configurable
- **EventBridge** — cron + cross-service events
- **S3 ObjectCreated** — file pipelines
- **DynamoDB Streams** — change capture

## Real World Usage
- API endpoints behind API Gateway
- S3 → process → notify pipelines
- Cron jobs via EventBridge
- Webhooks (Stripe, GitHub)
- Image / video transformations triggered on upload
- Glue logic between services

## Common Mistakes
- Treating Lambda as a long-running server (15-min timeout hard cap)
- Heavy init code → slow cold starts
- Per-Lambda DB connections (use RDS Proxy / Hyperdrive / Aurora DSQL)
- No DLQ on async → silent failures
- Ignoring concurrency limits → throttle storms
- Tight VPC-attached Lambdas during cold start (ENI provisioning historically slow)
- Polluting cost with debug logging (CloudWatch ingest priced per GB)

## Prerequisites
- [[AWS]] · [[VPC and Networking]] · [[IAM and Least Privilege]]

## What To Learn Next
- [[Containers in the Cloud]] · [[Cost Optimization]] · [[Edge Computing]]

## Best Learning Resources

### Official Documentation
- [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/)
- [Lambda Best Practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
- [Serverless Framework](https://www.serverless.com/framework/docs)
- [SST docs](https://sst.dev/docs/)

### Best YouTube Resource
- [Yan Cui (theburningmonk) — Lambda patterns](https://www.youtube.com/@theburningmonk)
- [Be A Better Dev — Lambda deep dives](https://www.youtube.com/c/BeABetterDev)

### Best Free Course
- [AWS Skill Builder — Serverless](https://explore.skillbuilder.aws/)
- [SST tutorial](https://sst.dev/docs/start)

### Best Advanced Resource
- ["Serverless Architectures on AWS" (Manning) — Peter Sbarski](https://www.manning.com/books/serverless-architectures-on-aws-second-edition)
- [Yan Cui blog — production Lambda](https://theburningmonk.com/)

### Best Practice Project
Build a thumbnail pipeline: S3 PutObject → Lambda → sharp → S3. Add a DLQ via SQS for failures. Measure cold/warm latency at 128, 512, 2048 MB.

### Recommended Order to Learn
1. Single function via console
2. Deploy via SST / Serverless / SAM
3. Triggers (API Gateway, S3, SQS)
4. Cold start + memory tuning
5. Idempotency for async events
6. RDS Proxy / connection pooling for DB
7. Step Functions for orchestration

## Interview Questions
**Q. Why does memory size affect Lambda speed?**
A. CPU scales linearly with memory — more memory = more vCPU.

**Q. When NOT to use Lambda?**
A. Long-running tasks (>15 min), websocket-heavy realtime (use Fargate / EC2), latency-critical paths with cold-start budgets <50ms (use edge).

**Q. SQS + Lambda — at-least-once delivery, what does that mean for your handler?**
A. Make it idempotent — dedup by message id; tolerate the same payload twice.

## Related
- [[AWS]] · [[Containers in the Cloud]] · [[Edge Computing]] · [[IAM and Least Privilege]]
