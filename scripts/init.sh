#!/bin/sh

echo "flask migration initialize..."
flask db init

echo "migrating..."
flask db migrate -m "first migrate"

echo "db schema upgrading..."
flask db upgrade