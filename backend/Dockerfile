FROM python:3.11-slim

RUN pip install poetry==2.0.1

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock /app/src/
WORKDIR /app/src

RUN poetry install --no-interaction --no-ansi

COPY ./alembic.ini /app/src/alembic.ini
COPY . /app/src/
COPY ./start.sh /app/src/start.sh

CMD ["sh", "/app/src/start.sh"]
