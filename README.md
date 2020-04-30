# DMOJ Docker

This repository contains the Docker files to run a clone of the [DMOJ site](https://github.com/DMOJ/online-judge). It configures some additional services, such as mathoid and texoid.

## Installation

First, [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) must be installed. Installation instructions can be found on their respective websites.

Clone the repository:
```sh
$ git clone https://github.com/Ninjaclasher/dmoj-docker
$ cd dmoj-docker
$ git submodule init
$ git submodule update --recursive
$ cd dmoj
```
From now on, it is assumed you are in the `dmoj` directory.

Initialize the setup by moving the configuration files into the submodule and by creating the necessary directories:
```sh
$ ./scripts/initialize
```

Configure the environment variables in the files in `dmoj/environment/`. In particular, set the MYSQL passwords in `mysql.env` and `mysql-admin.env`, and the host and secret key in `site.env`. Also, configure the `server_name` directive in `dmoj/nginx/conf.d/nginx.conf`.

Next, build the images:
```sh
$ docker-compose build
```

Start up the site, so you can perform the initial migrations:
```sh
$ docker-compose up -d site
```

You will need to generate the schema for the database, since it is currently empty:
```sh
$ ./scripts/migrate
```

Finally, the DMOJ comes with fixtures so that the initial install is not blank. They can be loaded with the following commands:
```sh
$ docker-compose exec site python3 loaddata navbar
$ docker-compose exec site python3 loaddata language_small
$ docker-compose exec site python3 loaddata demo
```

## Usage
```
$ docker-compose up -d
```

## Notes

### Migrating
As the DMOJ site is a Django app, you may need to migrate whenever you update. Assuming the site container is running, running the following command should suffice:
```sh
$ ./scripts/migrate
```

### Managing Static Files
Static files are built in a separate image than the site. If there are any changes to the static files, you will need to rebuild that image:
```sh
$ docker-compose build static
```

To update the static files in the other containers, you will need to repopulate the volume by forcefully recreating the volume. A quick way to do this is:
```sh
$ docker-compose stop site nginx
$ docker-compose rm site nginx static
$ docker volume rm dmoj_assets
$ docker-compose up -d
```

Having a separate image for static files is useful when developing, as you do not need to rebuild the static files every time. If you do not need this flexibility, feel free to combine the static image with the site image.

### Updating The Site
Updating various sections of the site requires different images to be rebuilt.

If any prerequisites were modified, you will need to rebuild most of the images:
```sh
$ docker-compose up -d --build base static site celery bridged wsevent
```
If the static files are modified, read the section on [Managing Static Files](#managing-static-files).

If only the source code is modified, a restart is sufficient:
```sh
$ docker-compose restart site celery bridged wsevent
```

### Multiple Nginx Instances

The `docker-compose.yml` configures Nginx to publish to port 80. If you have another Nginx instance on your host machine, you may want to change the port and proxy pass instead.

For example, a possible Nginx configuration file on your host machine would be:
```
server {
    listen 80;
    listen [::]:80;

    add_header X-UA-Compatible "IE=Edge,chrome=1";
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";

    location / {
        proxy_http_version 1.1;
        proxy_buffering off;
        proxy_set_header Host $http_host;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_pass http://127.0.0.1:10080/;
    }
}
```

In this case, the port that the Nginx instance in the Docker container is published to would need to be modified to `10080`.
