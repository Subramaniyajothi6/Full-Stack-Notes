---
tags: [cloud, intermediate, compute]
---

# Containers in the Cloud

> Running Docker images on managed orchestrators. ECS / Fargate, EKS, Cloud Run, App Runner, Fly Machines.

## Options (managed → DIY)
| Service               | Model                            | Use when                              |
|-----------------------|----------------------------------|---------------------------------------|
| Cloud Run (GCP)       | Serverless containers            | Stateless HTTP, fastest DX            |
| AWS App Runner        | PaaS-like                        | Single-container web app              |
| ECS on Fargate        | Managed container orchestrator   | AWS-native, no K8s                    |
| Fly Machines          | Globally distributed microVMs    | Edge + stateful workloads             |
| EKS                   | Managed Kubernetes               | K8s ecosystem, complex topologies     |
| Self-hosted K8s       | DIY                              | Specific compliance / control needs   |

## ECS Fargate (AWS-native default)
- **Task definition** = container spec + resources
- **Service** = desired count + load balancer integration
- **Cluster** = logical group
- Fargate = no nodes to manage; pay per task

```hcl
# Terraform sketch
resource "aws_ecs_task_definition" "api" {
  family                   = "api"
  cpu                      = 512
  memory                   = 1024
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  execution_role_arn       = aws_iam_role.exec.arn
  task_role_arn            = aws_iam_role.task.arn
  container_definitions    = jsonencode([{ name = "api", image = "...:abc", portMappings = [...] }])
}
```

## Cloud Run essentials
```bash
gcloud run deploy api \
  --image gcr.io/proj/api:abc \
  --concurrency 80 --min-instances 0 --max-instances 50 \
  --memory 512Mi
```
Auto-scales 0 → N on request rate.

## Common needs
- **Image registry** — ECR / GAR / GHCR / Docker Hub
- **Load balancer / ALB / GCLB** in front
- **Service discovery** — Cloud Map, Consul, K8s services
- **Secrets** — SSM / Secret Manager → env or volumes
- **Observability** — CloudWatch, Stackdriver, Datadog
- **Autoscaling** — CPU / requests / custom metrics

## Real World Usage
- Containerized Node / Express APIs
- Background workers
- Build / CI runners
- Migration target from EC2 / Heroku
- Multi-region deploys (Fly, Cloud Run regions)

## Common Mistakes
- Not setting CPU/memory → throttled at runtime
- Reading huge logs to stdout in tight loops (cost)
- Forgetting healthchecks → load balancer treats failing instance as healthy
- One giant container with frontend + backend (split them)
- Skipping graceful shutdown (`SIGTERM` handling) → in-flight requests dropped
- Long cold starts on min-instance=0 services for user-facing paths

## Prerequisites
- [[Docker]] · [[VPC and Networking]] · [[IAM and Least Privilege]]

## What To Learn Next
- [[Kubernetes]] (in Standalone topics) · [[Cost Optimization]] · [[Secrets Management]]

## Best Learning Resources

### Official Documentation
- [AWS ECS docs](https://docs.aws.amazon.com/ecs/)
- [Cloud Run docs](https://cloud.google.com/run/docs)
- [AWS App Runner](https://docs.aws.amazon.com/apprunner/)
- [Fly Machines](https://fly.io/docs/machines/)

### Best YouTube Resource
- [TechWorld with Nana — ECS / Cloud Run / K8s](https://www.youtube.com/c/TechWorldwithNana)
- [Anton Putra — containers in cloud](https://www.youtube.com/c/AntonPutra)

### Best Free Course
- [AWS Workshop — ECS Fargate](https://catalog.workshops.aws/ecsworkshop)
- [Google Cloud — Cloud Run quickstart](https://cloud.google.com/run/docs/quickstarts)

### Best Advanced Resource
- [The Twelve-Factor App](https://12factor.net/) — containerable architecture principles
- [Fly.io engineering blog](https://fly.io/blog/)

### Best Practice Project
Containerize a MERN API. Deploy three ways: (1) Cloud Run, (2) ECS Fargate, (3) Fly Machines. Compare cold start, latency, cost at 1000 req/h vs 1M req/h.

### Recommended Order to Learn
1. Container basics ([[Docker]])
2. Cloud Run or App Runner (fastest)
3. ECS Fargate
4. Health checks + graceful shutdown
5. Multi-region deploys
6. Move to K8s only when needed

## Interview Questions
**Q. Fargate vs ECS on EC2?**
A. Fargate is serverless containers — AWS manages nodes. ECS on EC2 means you run + patch the host fleet. Fargate trades flexibility for ops simplicity.

**Q. When pick Kubernetes over ECS / Cloud Run?**
A. Ecosystem need (Helm, operators), multi-cloud portability, complex topologies. Otherwise it's overkill.

**Q. Cloud Run cold start mitigation?**
A. `--min-instances`, lighter image, avoid heavy init outside the handler.

## Related
- [[Docker]] · [[Lambda and Serverless]] · [[VPC and Networking]] · [[IAM and Least Privilege]]
