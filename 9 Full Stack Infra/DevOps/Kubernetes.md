---
tags: [devops, advanced, orchestration]
---

# Kubernetes

> Container orchestrator. Declarative API: you describe desired state; the control plane reconciles reality.

## Building blocks
- **Pod** — smallest deployable unit (1+ containers sharing network/storage)
- **Deployment** — manages a set of Pod replicas with rollout strategy
- **Service** — stable network endpoint for a set of Pods (ClusterIP, NodePort, LoadBalancer)
- **Ingress** — HTTP(S) routing to Services
- **ConfigMap / Secret** — config + secret data
- **Namespace** — logical isolation
- **Node** — VM where Pods run
- **StatefulSet** — for stateful workloads (DBs)
- **DaemonSet** — one Pod per Node (log shippers, agents)
- **Job / CronJob** — batch + scheduled

## Minimal Deployment + Service
```yaml
apiVersion: apps/v1
kind: Deployment
metadata: { name: api }
spec:
  replicas: 3
  selector: { matchLabels: { app: api } }
  template:
    metadata: { labels: { app: api } }
    spec:
      containers:
      - name: api
        image: ghcr.io/me/api:abc
        ports: [{ containerPort: 3001 }]
        readinessProbe: { httpGet: { path: /health, port: 3001 }, periodSeconds: 5 }
        resources:
          requests: { cpu: 200m, memory: 256Mi }
          limits:   { cpu: 1,     memory: 512Mi }
---
apiVersion: v1
kind: Service
metadata: { name: api }
spec:
  selector: { app: api }
  ports: [{ port: 80, targetPort: 3001 }]
```

## Ecosystem
- **Helm** — package manager (charts = parametrized YAML)
- **Kustomize** — overlay-based config
- **Argo CD / Flux** — GitOps controller
- **Istio / Linkerd** — service mesh
- **Karpenter / Cluster Autoscaler** — node scaling
- **External Secrets Operator** — cloud secret sync
- **kubectl + k9s** — CLIs

## When to use K8s
- Multi-team platform with many services
- Specific compliance / control needs
- Heavy custom networking / mesh requirements
- Multi-cloud portability

## When NOT
- 1–10 services → ECS / Cloud Run / Fly is simpler
- Small team without dedicated platform engineer
- Stateful single-tenant apps

## Real World Usage
- EKS / GKE / AKS managed clusters in production
- Self-hosted k3s for edge
- Local dev with Kind / Minikube / OrbStack
- ML training (Kubeflow)
- CI runners (Actions Runner Controller)

## Common Mistakes
- Running stateful DBs without StatefulSet + persistent volumes
- No resource requests/limits → noisy-neighbor pain
- Latest tag on images → can't pin or rollback
- Skipping readiness probes → traffic to unhealthy pods
- One namespace for everything → blast radius huge
- Self-hosting K8s without a platform team

## Prerequisites
- [[Docker]] · [[Linux Basics]] · [[VPC and Networking]] · [[Containers in the Cloud]]

## What To Learn Next
- [[CI CD]] · [[Cost Optimization]]

## Best Learning Resources

### Official Documentation
- [Kubernetes docs](https://kubernetes.io/docs/home/)
- [Helm docs](https://helm.sh/docs/)
- [Argo CD docs](https://argo-cd.readthedocs.io/)

### Best YouTube Resource
- [TechWorld with Nana — Kubernetes Crash Course](https://www.youtube.com/c/TechWorldwithNana) — gold standard
- [Anton Putra — K8s in cloud](https://www.youtube.com/c/AntonPutra)

### Best Free Course
- [Kubernetes the Hard Way (Kelsey Hightower)](https://github.com/kelseyhightower/kubernetes-the-hard-way)
- [Killercoda interactive scenarios](https://killercoda.com/)

### Best Advanced Resource
- ["Kubernetes Up and Running" (O'Reilly)](https://www.oreilly.com/library/view/kubernetes-up-and/9781098110197/)
- [Brendan Burns' talks (K8s co-founder)](https://www.youtube.com/results?search_query=brendan+burns+kubernetes)

### Best Practice Project
Deploy a MERN app to a managed K8s (EKS/GKE): Deployments for API + web, Service + Ingress, Postgres as a managed RDS instead of in-cluster, Secrets from External Secrets Operator. Add Helm chart + Argo CD for GitOps.

### Recommended Order to Learn
1. Pod + Deployment + Service
2. ConfigMaps + Secrets
3. Ingress + TLS
4. Resource requests/limits + probes
5. Helm + Kustomize
6. Argo CD (GitOps)
7. Autoscaling (HPA + Cluster Autoscaler / Karpenter)
8. Service mesh (only when needed)

## Interview Questions
**Q. Pod vs Deployment?**
A. Pod is the unit running containers. Deployment manages a desired number of identical Pods with rollouts and scaling.

**Q. Why readiness vs liveness probes?**
A. Liveness restarts crashed containers. Readiness gates traffic until the container is actually ready (slow startup, warm-up).

**Q. When NOT to use K8s?**
A. Small footprint, no platform team, you'd be reinventing PaaS. ECS / Cloud Run / Fly cover most real needs at lower complexity.

## Related
- [[Docker]] · [[Containers in the Cloud]] · [[CI CD]] · [[Cost Optimization]]
