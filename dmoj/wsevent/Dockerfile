FROM node:buster

ENV NODE_PATH /node_modules/
WORKDIR /node_modules/
RUN npm install qu ws simplesets

EXPOSE 15100
EXPOSE 15101
EXPOSE 15102

ENTRYPOINT node /site/websocket/daemon.js
