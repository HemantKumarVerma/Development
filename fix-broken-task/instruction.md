# Log Report Task

## Objective

Write a program that reads the Apache access log located at:

```
/app/access.log
```

and generates a JSON report at:

```
/app/report.json
```

## Output Format

The output file must be valid JSON containing exactly these fields:

- `total_requests` – Total number of requests in the log.
- `unique_ips` – Number of unique client IP addresses.
- `top_path` – The request path that appears most frequently.

Example:

```json
{
  "total_requests": 8,
  "unique_ips": 4,
  "top_path": "/index.html"
}
```

## Success Criteria

Your solution is considered correct if:

1. It creates `/app/report.json`.
2. The file contains valid JSON.
3. The JSON contains the keys:
   - `total_requests`
   - `unique_ips`
   - `top_path`
4. The values for these keys exactly match the contents of `/app/access.log`.