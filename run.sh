#!/bin/bash

echo "========================================"
echo "   SENTINEL-OPS: DEFENSIVE SIMULATOR   "
echo "========================================"
echo

# Ensure Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "[ERROR] Docker is not running. Please start the Docker daemon."
    exit 1
fi

# Ensure docker-compose is installed
if ! command -v docker-compose > /dev/null 2>&1; then
    echo "[ERROR] docker-compose is not installed."
    exit 1
fi

# Ensure logs folder exists
mkdir -p logs
chmod 777 logs

# Build and start container
echo "[*] Building and starting SentinelOps container environment..."
docker-compose up --build -d > /dev/null 2>&1

# Follow container logs
echo "[*] Running threat detection and response..."
echo "----------------------------------------"
docker-compose logs -f sentinelops
echo "----------------------------------------"

echo
echo "[SUCCESS] Simulation complete."
echo "[INFO] Check 'logs/' folder for 'alerts.log'."
echo "[INFO] Check repo root for 'incident_report.json'."

# Stop container but keep logs
docker-compose down > /dev/null 2>&1
