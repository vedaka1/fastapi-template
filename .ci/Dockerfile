FROM python:3.12.4-slim-bullseye

WORKDIR /app

ENV PYTHONPATH=.

RUN pip install --upgrade pip && pip install poetry && poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./

RUN poetry install --without test --no-root --no-interaction --no-ansi

COPY src/ ./src
COPY .env main.py config.py alembic.ini ./
COPY ./.ci/entrypoint.sh /app/.ci/entrypoint.sh

RUN chmod +x /app/.ci/entrypoint.sh

EXPOSE 8000

CMD ["/bin/bash", "/app/.ci/entrypoint.sh"]