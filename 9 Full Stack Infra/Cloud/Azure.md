---
tags: [infra, cloud, intermediate]
---

# Azure

> Microsoft's cloud. Dominant in enterprise, deep Microsoft 365 / AD integration, Azure OpenAI partnership.

## Why it matters
Many enterprises run primarily on Azure. Strong .NET/Windows ecosystem, but supports everything Linux/Node/Python as well. Hosts Azure OpenAI for compliance-bound LLM use.

## Core building blocks
- **Compute** — VMs, App Service, Functions, AKS (Kubernetes), Container Apps
- **Storage** — Blob Storage, Files, Disks
- **Database** — Azure SQL, Cosmos DB (multi-model), PostgreSQL/MySQL flexible servers
- **Networking** — VNet, Load Balancer, Front Door, Application Gateway, Azure DNS
- **Identity** — Microsoft Entra ID (formerly Azure AD)
- **AI** — Azure OpenAI Service, AI Foundry, Cognitive Services
- **Messaging** — Service Bus, Event Grid, Event Hubs (Kafka-compatible)
- **DevOps** — Azure DevOps, GitHub (owned by MS)

## Real World Usage
- Enterprise apps with SSO via Entra ID
- Azure OpenAI for regulated industries
- AKS for K8s with full integration
- Hybrid cloud (Azure Arc)

## Common Mistakes
- Confusing legacy Cloud Services with App Service
- Not using managed identities → secrets in config
- Ignoring resource groups discipline → cleanup nightmare
- Cosmos DB cost surprises (RU/s consumption)

## Prerequisites
- [[Linux Basics]] · [[Docker]]

## What To Learn Next
- [[AWS]] · [[GCP]] · [[Terraform]] · [[Pulumi]]

## Best Learning Resources

### Official Documentation
- [Azure Docs](https://learn.microsoft.com/azure/) — recently revamped, very good
- [Cloud Adoption Framework](https://learn.microsoft.com/azure/cloud-adoption-framework/)

### Best YouTube Resource
- [John Savill's Technical Training](https://www.youtube.com/c/NTFAQGuy) — best Azure educator
- [Microsoft Azure (official)](https://www.youtube.com/c/MicrosoftAzure)

### Best Free Course
- [Microsoft Learn — Azure Fundamentals (AZ-900)](https://learn.microsoft.com/training/paths/azure-fundamentals/) — free
- [Azure for the AWS Professional](https://learn.microsoft.com/azure/architecture/aws-professional/)

### Best Advanced Resource
- [Azure Architecture Center](https://learn.microsoft.com/azure/architecture/) — patterns
- [Mark Russinovich's blog (Azure CTO)](https://learn.microsoft.com/en-us/shows/azure-friday/) — internals

### Best Practice Project
Deploy a containerized API to Azure Container Apps, fronted by Front Door, with Azure SQL backend, secrets in Key Vault, identity via Entra ID, and CI/CD from GitHub Actions. Add Application Insights for observability.

### Recommended Order to Learn
1. Subscriptions + resource groups + IAM
2. Storage + Azure SQL
3. App Service + Container Apps
4. VNet + Front Door
5. Functions + Service Bus
6. AKS + AI services

## Interview Questions
**Q. Container Apps vs App Service vs AKS?**
A. App Service = managed PaaS. Container Apps = serverless containers (Knative). AKS = full managed K8s.

**Q. Cosmos DB consistency levels?**
A. Five: Strong, Bounded Staleness, Session (default), Consistent Prefix, Eventual.

**Q. What's Entra ID?**
A. Identity provider for both org users (SSO, MFA) and apps. Replacement name for Azure AD.

## Related
- [[AWS]] · [[GCP]] · [[Terraform]]
