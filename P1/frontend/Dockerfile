FROM node:20-buster-slim

RUN mkdir /frontend 

WORKDIR /frontend

COPY package.json /frontend

RUN npm install

COPY . .

EXPOSE 3000 

CMD node server.js

