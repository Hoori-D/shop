FROM python:3.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
PTRHONUNBUFFERED=1

WORKDIR /APP

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    gettext \
    vim \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml .
COPY uv.lock .
RUN uv sync

COPY . .

EXPOSE 8000

CMD ["uv run manage.py migrate && uv run manage.py runserver 0.0.0.0:8000"]