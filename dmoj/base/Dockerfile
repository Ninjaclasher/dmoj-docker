FROM debian:buster

RUN apt-get update && apt-get install -y git gcc g++ make python3-dev \
    libxml2-dev libxslt1-dev zlib1g-dev gettext curl \
    mariadb-client libmariadbclient-dev gnupg wget ruby ruby-dev \
    libx11-xcb-dev libxcomposite1 libxcursor1 libxdamage1 libxi6 \
    libxtst6 libnss3 libcups2 libxss1 libxrandr2 libasound2 libatk1.0-0 \
    libatk-bridge2.0-0 libpangocairo-1.0-0 libgtk-3-0 \
    debconf-utils openssl python3-pip python3

RUN wget -q --no-check-certificate -O- https://bootstrap.pypa.io/get-pip.py | python3 && \
    curl -sL https://deb.nodesource.com/setup_12.x | bash -

RUN apt-get install -y nodejs
RUN apt-get autoremove -y
RUN npm install -g sass postcss-cli autoprefixer
RUN pip install pymysql mysqlclient websocket-client uwsgi python-memcached \
    redis

COPY repo/requirements.txt .
RUN pip install -r requirements.txt
