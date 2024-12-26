web: gunicorn wiki.wsgi --log-file -
release: python manage.py collectstatic --noinput web: gunicorn wiki.wsgi