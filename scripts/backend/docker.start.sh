#!/bin/sh
if [ "$MIGRATE" = "true" ]; then
  echo 'Running MySQL migrations...'
  flask db upgrade
fi

echo 'Starting Flask Server...'
python /app/run.py