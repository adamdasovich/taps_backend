#!/usr/bin/env bash
# exit on error
set -o errexit

# Debug: Print current directory and environment
echo "Current directory: $(pwd)"
echo "Listing directory contents:"
ls -la
echo "Python version:"
python --version

# Install requirements with verbose output
echo "Installing requirements..."
pip install -r requirements.txt

# Check for module imports before running Django commands
echo "Checking Python imports..."
python -c "import sys; print('Python path:'); print(sys.path)"
python -c "import django; print('Django version:', django.get_version())"

# Try importing your project modules
echo "Trying to import project modules..."
python -c "
try:
    import taps_backend.settings
    print('Successfully imported taps_backend.settings')
except ImportError as e:
    print('Error importing taps_backend.settings:', e)

try:
    import taps_backend.wsgi
    print('Successfully imported taps_backend.wsgi')
except ImportError as e:
    print('Error importing taps_backend.wsgi:', e)
"

# Now run Django commands with verbose output
echo "Running collectstatic..."
python manage.py collectstatic --no-input -v 2
echo "Running migrations..."
python manage.py