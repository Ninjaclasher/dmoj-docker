FROM ninjaclasher/dmoj-base:latest

ENTRYPOINT celery -A dmoj_celery worker -l info --concurrency=2 \
           >> /logs/celery.stdout.log 2>> /logs/celery.stderr.log
