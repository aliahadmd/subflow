#!/bin/bash

# Install dependencies
pip3.12 install -r requirements.txt

# Clear Python cache
find . -type d -name "__pycache__" -exec rm -rf {} +

# Clear Django cache
python3.12 manage.py clear_cache

# Collect static files
python3.12 manage.py collectstatic --no-input --clear

# Optimize Python memory usage
python3.12 -OO -m compileall .

# Clear system memory cache (requires sudo, may not work in all environments)
# sudo sync && sudo echo 3 | sudo tee /proc/sys/vm/drop_caches

# Vacuum SQLite database (if using SQLite)
# python manage.py sqlite3_vacuum

# Run database migrations
python3.12 manage.py migrate --no-input

# Optional: Run tests
# python manage.py test

echo "Build process completed."
