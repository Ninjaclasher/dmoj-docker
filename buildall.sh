#!/bin/sh
set -e
git submodule update --init --recursive

cd dmoj

mkdir -p problems media

cp ../config.js repo/websocket/
cp ../local_settings.py repo/dmoj/
cp ../uwsgi.ini repo/

docker compose build 
docker compose up -d db 
docker compose up -d redis
docker compose up -d site

docker compose exec $COMPOSE_EXEC_FLAGS site python3 manage.py migrate $@

docker compose exec $COMPOSE_EXEC_FLAGS site /bin/bash -c "\
    bash make_style.sh && \
    python3 manage.py collectstatic --noinput && \
    python3 manage.py compilemessages && \
    python3 manage.py compilejsi18n && \
    cp -r resources/ /assets/ && \
    rm resources/style.css resources/martor-description.css resources/select2-dmoj.css resources/ace-dmoj.css && \
    rm resources/dark/style.css resources/dark/martor-description.css resources/dark/select2-dmoj.css resources/dark/ace-dmoj.css && \
    rm -r sass_processed && \
    cp 502.html /assets/ && \
    cp logo.png /assets/ && \
    cp robots.txt /assets/"

docker compose up -d