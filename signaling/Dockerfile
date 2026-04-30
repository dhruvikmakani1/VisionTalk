FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Koyeb uses PORT env var (default 8000); signaling reads process.env.PORT
EXPOSE 8000

CMD ["npm", "start"]
