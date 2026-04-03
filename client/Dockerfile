# Build stage
FROM node:20-alpine AS build

WORKDIR /app

ARG VITE_APP_SIGNALING_URL
ARG VITE_APP_BACKEND_URL
ENV VITE_APP_SIGNALING_URL=$VITE_APP_SIGNALING_URL
ENV VITE_APP_BACKEND_URL=$VITE_APP_BACKEND_URL

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# Production stage
FROM nginx:stable-alpine

COPY --from=build /app/dist /usr/share/nginx/html

# Default nginx config (optional: add a custom one if routing needs it)
# EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
