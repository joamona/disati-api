#!/bin/bash
set -e

# Wait for PostgreSQL to be ready
until pg_isready; do
  echo ${POSTGRES_USER}
  echo "Waiting for PostgreSQL to start..."
  sleep 2
done

echo "PostgreSQL is ready. Starting restore."

# Create the user vagrant
echo "Creating the user vagrant."
psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} < /usr/local/app/init-users.sql

# Restore the database
pg_restore -v -U ${POSTGRES_USER} -d ${POSTGRES_DB} /usr/local/app/disati.backup

echo "Database restore completed."