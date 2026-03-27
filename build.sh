#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Create a Superuser automatically
# Replace 'admin', 'admin@example.com', and 'yourpassword' with your desired credentials
python manage.py shell <<EOF
from userprofile.models import AppUser
if not AppUser.objects.filter(email='admin@example.com').exists():
    AppUser.objects.create_superuser('admin@example.com', 'yourpassword')
    print("Superuser created.")
else:
    print("Superuser already exists.")
EOF
