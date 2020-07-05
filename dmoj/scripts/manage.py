#!/bin/bash
cd `dirname $0` && cd ..

docker-compose exec $COMPOSE_EXEC_FLAGS site python3 manage.py $@
