docker system prune -a --volumes
docker rmi $(docker images -aq)
docker volume rm $(docker volume ls -q)

rm -rf dmoj/database