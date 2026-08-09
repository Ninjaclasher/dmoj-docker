The site was down after unexpected machine shutdown by azure. 
the troubleshooting surfaced following issues
- bridged sites was not able to connect to db 
  - the db user was getting access denied
  - required resetting user password and grant of permissions 
- nginx was unable to access site 
  - the docker compose networking needed netwrosk entry site for nginx
- the site was not accessible 
  - ngnix host was auto-running after reboot of vm 
     - required disabling host nginx 
  - ngnix docekr was being sticky 
     - required ```sudo killall nginx```
  - the certs were expired
     renewed certs with ```sudo certbot renew```


here are some of the commands

docker compose exec -it db healthcheck.sh --connect
docker compose exec -it db bash
 healthcheck.sh --connect
 mariadb-admin ping -u root -p"NervouseNational#4"
 mariadb -u root -p"NervouseNational#4" -e "SELECT 1;"

ALTER USER 'dmoj'@'%' IDENTIFIED BY 'NervousNewton#4'
ALTER USER 'dmoj'@'localhost' IDENTIFIED BY 'NervousNewton#4';


--------
sudo systemctl status nginx
docker compose up -d --force-recreate nginx
sudo killall nginx

sudo certbot renew
docker compose exec nginx nginx -s reload