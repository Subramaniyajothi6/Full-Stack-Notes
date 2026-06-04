---
tags: [interview, mongodb]
---

# MongoDB Interview Bank

**Q. SQL vs MongoDB?**
A. Relational rows vs documents; joins vs embedding; strict schema vs flexible. See [[SQL vs NoSQL]].

**Q. What's BSON?**
A. Binary JSON; richer types (ObjectId, Date, Decimal128). See [[BSON and Documents]].

**Q. Indexes — when do they hurt?**
A. Slower writes (every index updated), more memory/disk. Don't index everything. See [[Indexes]].

**Q. Compound index field order?**
A. ESR — Equality, Sort, Range. See [[Compound Indexes]].

**Q. How to debug a slow query?**
A. `.explain('executionStats')`, look for COLLSCAN, examined-vs-returned ratio. See [[Explain and Query Plans]].

**Q. Aggregation pipeline — basic stages?**
A. `$match` (filter), `$group`, `$project`, `$sort`, `$lookup` for joins, `$unwind`. Push `$match` early. See [[Aggregation Stages]].

**Q. Embedded vs referenced — how to choose?**
A. Embed when always read together, child has no independent lifecycle. Reference for M:N or unbounded children. See [[Embedded vs Referenced]].

**Q. Transactions in Mongo?**
A. Multi-doc ACID via replica set. Slower; design schema to keep ops single-doc. See [[Transactions]].

**Q. Replica set and sharding?**
A. Replica set = HA + read scaling. Sharding = horizontal partition. See [[Replication]] · [[Sharding]].

**Q. What's a good shard key?**
A. High cardinality, even distribution, aligns with query pattern. Avoid monotonic keys (causes hotspot).

**Q. Mongoose vs native driver?**
A. Mongoose adds schema, validation, hooks, population. Native driver is faster, used for heavy aggregation paths.

**Q. Population — how it works?**
A. Mongoose runs an extra query for each ref'd field. Watch out for N+1.
