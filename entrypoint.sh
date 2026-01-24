#!/bin/bash
set -e

echo "Migrations"
uv run python manage.py migrate

echo "Runserver"
exec uv run python manage.py runserver 0.0.0.0:8000

