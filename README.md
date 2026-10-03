# Security-Vault: Security Microservice Pipeline

A containerized Python (FastAPI) microservice protected by an Nginx Reverse Proxy and an automated GitHub Actions SAST pipeline.

## Architecture & Security Features

1. **Container Hardening (`Dockerfile`)**:
   - Runs on a lightweight `python:3.11-slim` image.
   - Enforces the principle the least privilege by running the application under a non-root user (`appuser`).
2. **Network Isolation & Rate Limiting (`docker-compose.yml` & `nginx.conf`)**:
   - The FastAPI backend is isolated within an internal Docker bridge network (`internal_net`) and is not exposed directly to the host.
   - **Nginx** acts as a reverse proxy and security shield, enforcing **Rate Limiting** (`1 req/sec` per IP with a burst of 2) to mitigate Brute-Force and DoS attacks.
3. **Application Security (`main.py`)**:
   - Eliminates **SQL Injection (SQLi)** vulnerabilities by utilizing parameterized queries.
   - Prevents hardcoded credentials by injecting secrets via environment variables (`os.getenv`).
4. **Automated SAST Pipeline (`.github/workflows/security-scan.yml`)**:
   - Every push and pull request to `main` triggers an automated security audit using **Bandit** to catch medium/high severity vulnerabilities before deployment.

## Quick start

```bash
docker compose up --build