FROM dmoj-site-base:latest

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

EXPOSE 8000

ENTRYPOINT uwsgi --ini uwsgi.ini \
           >> /logs/site.stdout.log 2>> /logs/site.stderr.log
