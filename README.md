## How to run

Set variables in `.env` like in `.env.example`:

```python
POSTGRES_HOST=localhost
...
```

Set variables in `.env.production` in the same way, but specify `POSTGRES_HOST` with the hostname of your db container:

```python
POSTGRES_HOST=postgres
...
```

### Development

Run `docker compose up -d --build` or `make dev`

### What's next?

Now you can check API docs at the address `http://localhost:8000/api/v1/docs` 