# frontend/Dockerfile - dev-friendly
FROM node:18-alpine

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY . .
# expose Vite dev port
EXPOSE 5173
CMD ["npm", "run", "dev"]
