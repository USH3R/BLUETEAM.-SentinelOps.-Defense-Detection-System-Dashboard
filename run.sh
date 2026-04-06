#!/bin/bash

# --- SentinelOps: Automated Deployment Script via Docker Compose ---

echo "========================================"
echo "   SENTINEL-OPS: DEFENSIVE SIMULATOR   "
echo "========================================"
echo

# 1. Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "[ERROR] Docker is not running. Please start the Docker daemon."
    exit 1
fi

# 2. Check if docker-compose is installed
if ! command -v docker-compose > /dev/null 2>&1; then
    echo "[ERROR] docker-compose is not installed."
    exit 1
fi

# 3. Build and start containers
echo "[*] Building and starting SentinelOps container environment..."
docker-compose up --build -d

# 4. Wait for container to finish main.py execution
#    (Optional: remove -d for live output)
echo "[*] Running threat detection and response..."
echo "----------------------------------------"

docker-compose logs -f sentinelops

echo "----------------------------------------"
echo
echo "[SUCCESS] Simulation complete."
echo "[INFO] Check 'logs/' folder for alerts and mitigation actions."
echo "[INFO] Container can be stopped with: docker-compose down"
