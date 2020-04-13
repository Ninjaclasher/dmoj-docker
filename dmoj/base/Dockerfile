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

RUN apt-get update && \
    apt-get install -y unzip xvfb libxi6 libgconf-2-4 && \
    curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
    echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get -y update && \
    apt-get -y install google-chrome-stable && \
    wget https://chromedriver.storage.googleapis.com/81.0.4044.69/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver && \
    rm chromedriver_linux64.zip && \
    rm -rf /var/lib/apt/lists/* && \
    pip install selenium

COPY repo/requirements.txt .
RUN pip install -r requirements.txt
