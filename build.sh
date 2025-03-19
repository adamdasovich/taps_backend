set -o errexit

pip install -r requirements.txt
python taps_rezos/manage.py collectstatic --no-input
python taps_rezos/manage.py migrate