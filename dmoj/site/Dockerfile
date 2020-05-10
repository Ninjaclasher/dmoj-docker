FROM ninjaclasher/dmoj-base:latest

EXPOSE 8000

ENTRYPOINT uwsgi --ini uwsgi.ini \
           >> /logs/site.stdout.log 2>> /logs/site.stderr.log
