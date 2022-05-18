#!/bin/sh
alembic upgrade head

uvicorn --workers 2 --host 0.0.0.0 --port 5000 app:app --reload --reload-dir=app
