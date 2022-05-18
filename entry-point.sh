#!/bin/sh
alembic upgrade head

python initial_data.py

gunicorn -w ${NUM_WORKERS:-5} -k uvicorn.workers.UvicornWorker app:app --bind 0.0.0.0:5000
