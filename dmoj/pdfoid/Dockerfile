FROM python:3.14-slim-trixie

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl gnupg git unzip xvfb libxi6 exiftool wget && \
    mkdir -p /etc/apt/keyrings && \
    curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | \
        gpg --dearmor --yes -o /etc/apt/keyrings/google-chrome.gpg && \
    echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/google-chrome.gpg] https://dl.google.com/linux/chrome/deb/ stable main" \
        >> /etc/apt/sources.list.d/google-chrome.list && \
    sed -i 's/^Components: main$/& contrib non-free/' /etc/apt/sources.list.d/debian.sources && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        google-chrome-stable fonts-noto ttf-mscorefonts-installer && \
    rm -rf /var/lib/apt/lists/* && \
    wget https://chromedriver.storage.googleapis.com/$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver && \
    rm chromedriver_linux64.zip && \
    useradd -m pdfoid

RUN git clone https://github.com/DMOJ/pdfoid.git pdfoid
WORKDIR /pdfoid/
RUN pip3 install -e .

ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver
ENV EXIFTOOL_PATH=/usr/bin/exiftool

EXPOSE 8888
USER pdfoid
ENTRYPOINT pdfoid --address=pdfoid --port=8888
