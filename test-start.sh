#!/bin/sh
export CONFIG_TYPE="dev"

alembic upgrade head

python tests_pre_start.py

python -m pytest -v --cov=app/ --cache-clear --color=yes --cov-report=html app/tests/

# python tests_post.py
