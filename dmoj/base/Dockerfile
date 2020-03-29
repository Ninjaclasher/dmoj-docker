FROM debian:buster-slim

RUN apt-get update && \
    apt-get install -y \
        git gcc g++ make curl gettext wget \
        libxml2-dev libxslt1-dev zlib1g-dev \
        mariadb-client libmariadbclient-dev \
        debconf-utils python3-pip python3-dev python3 && \
    wget -q --no-check-certificate -O- https://bootstrap.pypa.io/get-pip.py | python3 && \
    curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt-get install -y nodejs && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

RUN npm install -g sass postcss-cli autoprefixer
RUN pip install \
        pymysql mysqlclient websocket-client uwsgi python-memcached redis

COPY repo/requirements.txt .
RUN pip install -r requirements.txt
