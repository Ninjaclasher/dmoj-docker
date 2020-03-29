FROM dmoj-site-base:latest

# puppeteer dependencies
RUN apt-get update && \
    apt-get install -y \
        libx11-xcb-dev libxcomposite1 libxcursor1 libxdamage1 libxi6 \
        libxtst6 libnss3 libcups2 libxss1 libxrandr2 libasound2 libatk1.0-0 \
        libatk-bridge2.0-0 libpangocairo-1.0-0 libgtk-3-0 && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /node_modules/
RUN npm install puppeteer

EXPOSE 8000

ENTRYPOINT uwsgi --ini uwsgi.ini \
            >> /logs/site.stdout.log 2>> /logs/site.stderr.log
