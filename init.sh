sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
cd /home/box/web/ask
python3 manage.py runserver 0.0.0.0:8000


#gunicorn --bind=0.0.0.0:8000 --workers=2 --timeout=15 --log-level=debug ask.wsgi:application
