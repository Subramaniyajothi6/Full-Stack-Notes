---
tags: [mern, deployment, intermediate]
---

# Dockerized MERN

> A `docker compose` stack that brings up Mongo, Express, and the React build behind nginx — same shape from laptop to VPS.

## The compose file
```yaml
# docker-compose.yml
services:
  mongo:
    image: mongo:7
    volumes: [mongo-data:/data/db]
    environment:
      MONGO_INITDB_ROOT_USERNAME: ${MONGO_USER}
      MONGO_INITDB_ROOT_PASSWORD: ${MONGO_PASSWORD}
    healthcheck:
      test: ["CMD", "mongosh", "--eval", "db.adminCommand('ping')"]
      interval: 10s

  api:
    build: ./apps/api
    environment:
      MONGO_URI: mongodb://${MONGO_USER}:${MONGO_PASSWORD}@mongo:27017
      NODE_ENV: production
      JWT_SECRET: ${JWT_SECRET}
    depends_on:
      mongo: { condition: service_healthy }
    expose: ["3001"]

  web:
    build: ./apps/web
    expose: ["80"]
    depends_on: [api]

  nginx:
    image: nginx:alpine
    ports: ["80:80", "443:443"]
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./certs:/etc/letsencrypt:ro
    depends_on: [web, api]

volumes:
  mongo-data:
```

## API Dockerfile (multi-stage)
```dockerfile
FROM node:20-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev

FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
COPY --from=deps /app/node_modules ./node_modules
COPY . .
USER node
EXPOSE 3001
HEALTHCHECK --interval=30s CMD wget -qO- http://localhost:3001/health || exit 1
CMD ["node", "src/index.js"]
```

## Web Dockerfile (build → nginx static)
```dockerfile
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.web.conf /etc/nginx/conf.d/default.conf
```

## nginx.conf (TLS + reverse proxy)
```nginx
http {
  upstream api { server api:3001; }
  upstream web { server web:80; }

  server {
    listen 443 ssl http2;
    server_name app.example.com;
    ssl_certificate     /etc/letsencrypt/live/app.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/app.example.com/privkey.pem;

    location /api/ { proxy_pass http://api/; proxy_set_header Host $host; }
    location /     { proxy_pass http://web/; }
  }

  server { listen 80; return 301 https://$host$request_uri; }
}
```

## Real World Usage
- Local dev parity (`docker compose up` brings up everything)
- Single-VPS production for hobby/MVP projects
- CI test stages (one compose file = identical env in tests)
- Demo sandboxes for clients

## Common Mistakes
- Running as root in containers
- Mounting host `node_modules` (platform mismatch)
- No `.dockerignore` → secrets baked into image
- Single-stage build → 1GB images
- No `restart: unless-stopped` → containers don't recover after host reboot
- Mongo exposed on the public internet (no firewall)
- Storing uploads inside containers (lost on redeploy — use S3)

## Prerequisites
- [[Docker]] · [[Linux Basics]] · [[Deployment Architecture]] · [[Environment Management]]

## What To Learn Next
- [[Full-Stack CI CD]] · [[Logging Across Services]]

## Best Learning Resources

### Official Documentation
- [Docker Compose docs](https://docs.docker.com/compose/)
- [Nginx Reverse Proxy guide](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/)
- [Let's Encrypt + nginx (certbot)](https://eff-certbot.readthedocs.io/en/latest/)

### Best YouTube Resource
- [TechWorld with Nana — Docker Compose](https://www.youtube.com/c/TechWorldwithNana)
- [Bret Fisher — Docker for devs](https://www.youtube.com/c/BretFisherDockerCaptain)

### Best Free Course
- [Play with Docker labs](https://labs.play-with-docker.com/)
- [Docker — Get Started](https://docs.docker.com/get-started/)

### Best Advanced Resource
- [BuildKit + multi-platform builds](https://docs.docker.com/build/buildkit/)
- [Trivy / Snyk — image vulnerability scanning](https://aquasecurity.github.io/trivy/)

### Best Practice Project
Containerize an existing MERN app of yours. Bring up the full stack with a single command. Add healthchecks, set up Traefik or nginx with Let's Encrypt, deploy to a $5 VPS, then write a one-page operations runbook (deploy / rollback / view logs).

### Recommended Order to Learn
1. Single Dockerfile for the API
2. Multi-stage build (smaller images)
3. Compose for local dev
4. Healthchecks + restart policies
5. Reverse proxy + TLS
6. Volumes + backups
7. Production deploy + rollback strategy

## Interview Questions
**Q. Why multi-stage builds?**
A. Build deps + sources stay in builder stage; only the runtime artifact ships → 10–100× smaller images, smaller attack surface.

**Q. Why nginx in front of Node and React?**
A. TLS termination, gzip/brotli, static caching, request buffering, and a single port (443) for both apps.

**Q. Why healthchecks matter?**
A. Compose / orchestrators use them to gate startup ordering and to remove unhealthy instances from rotation.

## Related
- [[Docker]] · [[Deployment Architecture]] · [[Full-Stack CI CD]] · [[Environment Management]]
