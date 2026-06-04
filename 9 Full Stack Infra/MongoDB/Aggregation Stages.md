---
tags: [mongodb, intermediate, syntax]
---

# Aggregation Stages

| Stage         | Purpose                                    |
| ------------- | ------------------------------------------ |
| `$match`      | Filter docs (push as early as possible)    |
| `$project`    | Reshape — include/exclude/compute fields   |
| `$group`      | Aggregate by `_id`                         |
| `$sort`       | Sort                                       |
| `$skip`/`$limit` | Pagination                              |
| `$unwind`     | Explode array into multiple docs            |
| `$lookup`     | Join — see [[Lookup and Joins]]            |
| `$facet`      | Run sub-pipelines in parallel              |
| `$addFields`  | Add computed fields                        |
| `$count`      | Count docs                                  |
| `$out` / `$merge` | Write results to a collection           |

## Common mistakes
- `$match` after expensive stages (loses index)
- `$project` removing `_id` then `$lookup` joining on it
- Heavy aggregations on the request path — schedule offline

## Related
- [[Aggregation Pipeline]]

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

## Best Learning Resources

### Official Documentation
- https://www.mongodb.com/docs/ — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. Hussein Nasser, MongoDB official

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
