FROM node:8.17.0

RUN apt-get update && \
    apt-get install --no-install-recommends -y -o Dpkg::Options::="--force-confold" librsvg2-dev mocha && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN npm install mathoid && \
    ln -sfv /node_modules/mathoid/app.js /node_modules/app.js

EXPOSE 10044
WORKDIR /node_modules/mathoid
CMD /node_modules/mathoid/server.js
