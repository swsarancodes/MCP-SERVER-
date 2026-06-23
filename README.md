# mcp-arithmetic-server

Minimal MCP server exposing basic arithmetic tools using the official Python MCP SDK + FastMCP.

## Tools

- `add(a, b)` → `{ "result": a + b }`
- `subtract(a, b)` → `{ "result": a - b }`
- `multiply(a, b)` → `{ "result": a * b }`
- `divide(a, b)` → `{ "result": a / b }` or `{ "error": "Division by zero is not allowed." }`

## Run / Dev

```bash
uv run fastmcp dev server.py
```

## Requirements

- Python >= 3.10
- `mcp[cli]` (managed by uv)

## Notes

- Single file implementation.
- STDIO transport (works directly with Inspector).
- Input validation via type hints (Pydantic under the hood).
- No database, no extras.
