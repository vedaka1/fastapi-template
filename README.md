## How to run

Set variables in `.env` like in `.env.example`:

```python
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=test
```
### Development

Run `docker compose up -d --build` or `make dev`

### What's next?

Now you can check API docs at the address `http://localhost:8000/docs` 