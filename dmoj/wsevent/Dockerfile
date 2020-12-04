FROM node:alpine

WORKDIR /app/
RUN npm install qu ws simplesets

EXPOSE 15100
EXPOSE 15101
EXPOSE 15102

ENTRYPOINT node /app/site/websocket/daemon.js
