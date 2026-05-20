FROM node:18

# Create app directory
WORKDIR /app

# Initialize a minimal package.json (avoids npm bug)
RUN npm init -y

# Install mathoid locally
RUN npm install mathoid

# Link entry point
RUN ln -sfv /app/node_modules/mathoid/app.js /app/app.js

EXPOSE 10044

WORKDIR /app/node_modules/mathoid

CMD ["node", "server.js"]
