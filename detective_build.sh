#!/usr/bin/env bash
# exit on error
set -o errexit

# Print directory structure
echo "=== DIRECTORY STRUCTURE ==="
find . -type f -name "*.py" | sort

# Print content of manage.py
echo -e "\n=== MANAGE.PY CONTENT ==="
cat manage.py

# Print content of wsgi.py
echo -e "\n=== WSGI.PY CONTENT ==="
cat taps_backend/wsgi.py

# Print the first part of settings.py
echo -e "\n=== SETTINGS.PY CONTENT (first 50 lines) ==="
head -n 50 taps_backend/settings.py

# Print all import statements in Python files
echo -e "\n=== ALL IMPORT STATEMENTS ==="
grep -r "^import\|^from" --include="*.py" .

# Print all references to taps_rezos
echo -e "\n=== ALL REFERENCES TO TAPS_REZOS ==="
grep -r "taps_rezos" --include="*.py" .

# Install requirements
echo -e "\n=== INSTALLING REQUIREMENTS ==="
pip install -r requirements.txt

# Try to run Django with verbosity
echo -e "\n=== TRYING TO START DJANGO ==="
python -c "
import sys
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taps_backend.settings')
try:
    import django
    django.setup()
    print('Django setup successful')
except Exception as e:
    print('Error setting up Django:', e)
"