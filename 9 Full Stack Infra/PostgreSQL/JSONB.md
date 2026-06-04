---
tags: [postgresql, intermediate, concept]
---

# JSONB

> Binary JSON column type. Searchable, indexable, faster than `json` for everything but raw text fidelity.

## Why `jsonb` over `json`
- Stored as binary (faster reads)
- Whitespace + key order normalized
- Indexable (GIN)
- All operators available

## Basics
```sql
CREATE TABLE products (
  id serial PRIMARY KEY,
  data jsonb
);

INSERT INTO products (data) VALUES (
  '{"name": "T-Shirt", "tags": ["sale","new"], "price": 29.9}'
);

SELECT data->>'name'       FROM products;   -- text
SELECT data->'tags'        FROM products;   -- jsonb
SELECT data #>> '{tags,0}' FROM products;   -- text deep path
```

## Querying
```sql
SELECT * FROM products WHERE data @> '{"tags": ["sale"]}';     -- contains
SELECT * FROM products WHERE data ? 'price';                   -- key exists
SELECT * FROM products WHERE data @@ '$.price > 20';           -- JSON path

SELECT * FROM products WHERE (data->>'price')::numeric > 20;   -- cast for math
```

## GIN index
```sql
CREATE INDEX idx_products_data ON products USING GIN (data);
-- specialized
CREATE INDEX idx_products_data_path ON products USING GIN (data jsonb_path_ops);
```

## Update sub-paths
```sql
UPDATE products SET data = jsonb_set(data, '{price}', '34.9'::jsonb)
WHERE id = 1;
```

## Real World Usage
- Flexible schema for early-stage data
- User-defined fields (form builders)
- Per-tenant custom fields
- Storing API responses verbatim
- Hybrid relational + document

## Common Mistakes
- JSONB-everything as schema avoidance → loses constraint power
- Forgetting indexes → table scan on large tables
- `data->'x'` returns jsonb; `data->>'x'` returns text — easy to mix up
- Casting in WHERE without expression index → no index used
- Hot JSONB columns getting bloat — vacuum behavior matters

## Prerequisites
- [[PostgreSQL]] · [[Indexes in PostgreSQL]]

## What To Learn Next
- [[Full-Text Search]] · [[CTEs and Window Functions]]

## Best Learning Resources

### Official Documentation
- [JSONB docs](https://www.postgresql.org/docs/current/datatype-json.html)
- [JSON functions](https://www.postgresql.org/docs/current/functions-json.html)

### Best YouTube Resource
- [Hussein Nasser — JSONB indexing](https://www.youtube.com/@hnasr)

### Best Free Course
- [PostgreSQL Tutorial — JSON](https://www.postgresqltutorial.com/postgresql-json/)

### Best Advanced Resource
- [Crunchy Data — JSONB performance](https://www.crunchydata.com/blog/)
- [PostgreSQL JSON-Path standard](https://www.postgresql.org/docs/current/functions-json.html#FUNCTIONS-SQLJSON-PATH)

### Best Practice Project
Build a "form builder" where each form definition is JSONB. Add GIN index. Query for forms containing specific fields, and measure perf with and without the index.

### Recommended Order to Learn
1. jsonb vs json
2. `->`, `->>`, `#>`, `#>>`
3. `@>` contains operator
4. GIN index + `jsonb_path_ops`
5. `jsonb_set` updates
6. JSON Path expressions
7. When to migrate fields out to columns

## Interview Questions
**Q. `->` vs `->>`?**
A. `->` returns jsonb. `->>` returns text. Use `->>` when you want a string out.

**Q. When should you NOT use JSONB?**
A. When the schema is stable — columns give you better constraints, statistics, and joins.

## Related
- [[Indexes in PostgreSQL]] · [[Full-Text Search]] · [[PostgreSQL]]
