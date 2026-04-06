# Dockerfile — Terminal-only SentinelOps
FROM python:3.11-slim

# 1. Set working directory inside container
WORKDIR /app

# 2. Copy EVERYTHING from the repo to the container
# This avoids the "file not found" errors if names are slightly different
COPY . .

# 3. Ensure terminal-friendly output (unbuffered)
# This forces the alerts to hit your screen immediately
ENV PYTHONUNBUFFERED=1

# 4. Default command to run the simulator
# IMPORTANT: Ensure your primary script is actually named 'main.py'
CMD ["python", "main.py"]
