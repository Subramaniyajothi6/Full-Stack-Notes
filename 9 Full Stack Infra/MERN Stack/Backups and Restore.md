---
tags: [mern, deployment, intermediate]
---

# Backups and Restore

> A backup you've never restored is not a backup. The whole point of this discipline is the *restore*, not the dump.

## What to back up
- **Primary DB** (Mongo / Postgres) — your business data
- **Object storage** (S3 user uploads) — irreplaceable user content
- **Secrets / config** — Vault, SSM, Doppler exports
- **Logs / audit trail** — for compliance, retention varies

## Strategies (cheapest → safest)
| Strategy                   | RPO            | RTO            | Cost     |
| -------------------------- | -------------- | -------------- | -------- |
| Daily dump + S3            | up to 24h loss | 30+ min restore| $        |
| Continuous WAL / oplog     | seconds        | minutes        | $$       |
| Read replicas + PITR       | seconds        | seconds        | $$$      |
| Multi-region active-active | near zero      | near zero      | $$$$     |

- **RPO** (recovery point objective) — how much data can you lose?
- **RTO** (recovery time objective) — how fast can you be back up?

## Tooling
- **Mongo Atlas** — built-in continuous backup with PITR
- **Postgres on RDS** — automated snapshots + PITR
- **Self-hosted Mongo** — `mongodump` / oplog tailing → S3
- **Self-hosted Postgres** — `pg_basebackup` + WAL-G archiving → S3
- **S3** — versioning + lifecycle + replication to a separate region

## Restore drills
Schedule them. Quarterly minimum. Steps:
1. Spin up a clean staging env
2. Restore latest backup
3. Validate row counts, sample records, index existence
4. Time the restore (this is your real RTO)
5. Document what broke

If you've never tested restore, assume it doesn't work.

## Real World Usage
- Pre-deploy backups before risky migrations
- Disaster recovery (region outage)
- "Help, I deleted the wrong table" rollback
- Compliance audits (SOC 2, ISO 27001 require restore evidence)
- Forensic investigations

## Common Mistakes
- Backups stored in the same account/region as the DB (one account compromise → both gone)
- No retention policy → infinite cost
- No off-platform copy (e.g., AWS-only setups; consider Backblaze B2 for off-cloud)
- Untested backups
- Encrypted backups with keys lost when ops engineer left
- Backing up the DB but not its supporting state (Redis sessions, Elasticsearch indexes)
- Forgetting to back up uploads bucket (assumed S3 = backup; deletion or bug propagates)

## Prerequisites
- [[Deployment Architecture]] · [[MongoDB]] · [[PostgreSQL]] · [[AWS S3]]

## What To Learn Next
- [[DB Migrations]] · [[Multi-Tenant Patterns]]

## Best Learning Resources

### Official Documentation
- [MongoDB Atlas backup docs](https://www.mongodb.com/docs/atlas/backup-restore-cluster/)
- [PostgreSQL Continuous Archiving](https://www.postgresql.org/docs/current/continuous-archiving.html)
- [AWS RDS automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)
- [WAL-G](https://github.com/wal-g/wal-g) — Postgres / Mongo archiver

### Best YouTube Resource
- [Hussein Nasser — Postgres replication & backups](https://www.youtube.com/@hnasr)
- [TechWorld with Nana — backup strategies](https://www.youtube.com/c/TechWorldwithNana)

### Best Free Course
- [AWS Skill Builder — RDS backup](https://explore.skillbuilder.aws/)
- [PostgreSQL Backup tutorial (postgresqltutorial.com)](https://www.postgresqltutorial.com/postgresql-administration/postgresql-backup/)

### Best Advanced Resource
- [Google SRE Workbook — Data integrity](https://sre.google/workbook/data-integrity/)
- [Designing Data-Intensive Applications — durability chapters](https://dataintensive.net/)

### Best Practice Project
Take a copy of a small MERN database, set up nightly `mongodump` to S3 with versioning, write a restore runbook, then actually run it on a clean staging env. Time it. Then break the script in one place and re-run to discover the gap.

### Recommended Order to Learn
1. RPO / RTO concepts
2. Native DB backup tools (Atlas / RDS)
3. WAL / oplog continuous backup
4. S3 object versioning + lifecycle
5. Restore drills + runbooks
6. Cross-region / cross-account copies
7. PITR (point-in-time recovery)

## Interview Questions
**Q. RPO vs RTO?**
A. RPO = data loss tolerance. RTO = downtime tolerance. They drive backup frequency and architecture.

**Q. Why is "backup exists" not enough?**
A. Untested backups frequently fail to restore. Drills validate the whole pipeline.

**Q. Why store backups in a separate account?**
A. Defense against compromised credentials and rogue actors deleting both prod and backups.

## Related
- [[MongoDB]] · [[PostgreSQL]] · [[AWS S3]] · [[Deployment Architecture]] · [[DB Migrations]]
