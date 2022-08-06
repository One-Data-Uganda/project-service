#!/bin/sh
# Source environment variables
source ./.env.test

# Cleanup old data (could have been a failed test)
dropdb ${POSTGRES_DB} 2> /dev/null 2>&1
createdb ${POSTGRES_DB}

psql -v ON_ERROR_STOP=1 --dbname "$POSTGRES_DB" <<-EOSQL
CREATE SCHEMA IF NOT EXISTS dblink;
CREATE SCHEMA IF NOT EXISTS jobmon;
CREATE SCHEMA IF NOT EXISTS partman;

CREATE EXTENSION supa_audit CASCADE;

CREATE EXTENSION dblink SCHEMA dblink;
CREATE EXTENSION pg_jobmon WITH SCHEMA jobmon;
CREATE EXTENSION pg_partman WITH SCHEMA partman;

CREATE ROLE partman WITH LOGIN;
GRANT ALL ON SCHEMA partman TO partman;
GRANT ALL ON SCHEMA public TO partman;
GRANT ALL ON SCHEMA jobmon TO partman;
GRANT ALL ON SCHEMA dblink TO partman;
GRANT ALL ON ALL TABLES IN SCHEMA partman TO partman;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA partman TO partman;
GRANT EXECUTE ON ALL PROCEDURES IN SCHEMA partman TO partman;

SELECT partman.create_parent('audit.record_version', 'ts', 'native', 'monthly')

EOSQL

# Run DB migrations
alembic upgrade head

# Add initial data
python tests_pre_start.py

# Run tests
python -m pytest -v --cov=app/ --cache-clear --color=yes --cov-report=html app/tests/
