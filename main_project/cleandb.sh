rm -f main_app/migrations/0001_initial.py
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
