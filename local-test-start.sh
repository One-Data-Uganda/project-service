#!/bin/sh
# Source environment variables
source ./.env.test

# Cleanup old data (could have been a failed test)
dropdb ${POSTGRES_DB} 2> /dev/null 2>&1
createdb ${POSTGRES_DB}

# Run DB migrations
alembic upgrade head

# Add initial data
python tests_pre_start.py

# Run tests
python -m pytest -v --cov=app/ --cache-clear --color=yes --cov-report=html app/tests/
