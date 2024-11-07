
rm social/migrations/0*.py
rm db.sqlite3





python3 manage.py makemigrations
python3 manage.py migrate



DJANGO_SUPERUSER_PASSWORD=admin \
DJANGO_SUPERUSER_USERNAME=admin \
DJANGO_SUPERUSER_EMAIL=admin@admin.com \
./manage.py createsuperuser \
--no-input