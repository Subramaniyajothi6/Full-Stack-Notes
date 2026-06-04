---
tags: [postgresql, intermediate, syntax]
---

# Full-Text Search

> Built-in lexeme-aware search using `tsvector` (document) and `tsquery` (search expression).

## Basics
```sql
SELECT to_tsvector('english', 'The quick brown fox jumps over the lazy dogs');
-- 'brown':3 'dog':9 'fox':4 'jump':5 'lazi':8 'quick':2

SELECT to_tsvector('english','running') @@ to_tsquery('english','runs');
-- true — stem normalization
```

## Schema with a generated tsvector column
```sql
CREATE TABLE posts (
  id serial PRIMARY KEY,
  title text,
  body text,
  search_vector tsvector GENERATED ALWAYS AS (
    setweight(to_tsvector('english', coalesce(title,'')), 'A') ||
    setweight(to_tsvector('english', coalesce(body,'')),  'B')
  ) STORED
);

CREATE INDEX idx_posts_search ON posts USING GIN (search_vector);
```

## Query
```sql
SELECT id, ts_rank(search_vector, q) AS rank
FROM posts, plainto_tsquery('english', 'redis cache') q
WHERE search_vector @@ q
ORDER BY rank DESC
LIMIT 10;
```

## Highlight matches
```sql
SELECT ts_headline('english', body, plainto_tsquery('redis cache'))
FROM posts WHERE search_vector @@ plainto_tsquery('redis cache');
```

## Trigram fuzzy matching
```sql
CREATE EXTENSION pg_trgm;
SELECT * FROM users
WHERE name % 'jonh';                      -- similarity match
SELECT similarity('postgres','postgrs');  -- 0.7...
```
Pair with GIN/GiST trgm ops for fast fuzzy.

## Real World Usage
- Docs / blog search
- Product search
- Code search
- Autocomplete with `pg_trgm`
- Hybrid with [[Vector Search]] for semantic + lexical

## Common Mistakes
- Building the tsvector on read instead of storing it (slow!)
- Forgetting GIN index
- Mixing languages without selecting the right config
- Using `to_tsquery` with raw user input (breaks on punctuation) — use `plainto_tsquery` / `websearch_to_tsquery`
- Treating full-text as semantic — it's not; pair with embeddings for semantic

## Prerequisites
- [[PostgreSQL]] · [[Indexes in PostgreSQL]]

## What To Learn Next
- [[JSONB]] · [[Vector Search]]

## Best Learning Resources

### Official Documentation
- [Full Text Search docs](https://www.postgresql.org/docs/current/textsearch.html)
- [pg_trgm](https://www.postgresql.org/docs/current/pgtrgm.html)

### Best YouTube Resource
- [Hussein Nasser — Postgres full-text search](https://www.youtube.com/@hnasr)

### Best Free Course
- [PostgreSQL Tutorial — FTS](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-full-text-search/)

### Best Advanced Resource
- [Crunchy Data — FTS performance](https://www.crunchydata.com/blog/postgres-full-text-search-a-search-engine-in-a-database)
- [Supabase — combining FTS + pgvector](https://supabase.com/blog/openai-embeddings-postgres-vector)

### Best Practice Project
Add full-text search to a blog: stored `tsvector` column, GIN index, `ts_rank` ordering, headline highlights. Then add `pg_trgm` for typo tolerance.

### Recommended Order to Learn
1. `to_tsvector` / `to_tsquery`
2. Stored generated tsvector column
3. GIN index
4. `ts_rank` ordering
5. `ts_headline`
6. `pg_trgm` fuzzy + autocomplete
7. Hybrid with vector search ([[Vector Search]])

## Interview Questions
**Q. Why a stored `tsvector` column over on-the-fly?**
A. Stored gives indexable column + reusable rank; per-query is recomputed every read.

**Q. FTS vs pg_trgm vs vector?**
A. FTS = stemmed keyword. trgm = fuzzy similarity. Vector = semantic. Combine for best results.

## Related
- [[JSONB]] · [[Indexes in PostgreSQL]] · [[Vector Search]] · [[pgvector]]
