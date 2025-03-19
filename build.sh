#!/usr/bin/env bash
# exit on error
set -o errexit

# Debug: Print current directory
echo "Current directory: $(pwd)"
echo "Listing directory contents:"
ls -la

# Install requirements
pip install -r requirements.txt

# Run Django commands
python manage.py collectstatic --no-input
python manage.py migrate