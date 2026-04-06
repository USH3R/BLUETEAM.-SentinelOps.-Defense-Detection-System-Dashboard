#!/bin/bash

# --- SentinelOps: Automated Deployment Script (Repair Version) ---

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

# 3. REPAIR STEP: Ensure the local logs folder exists for the Volume Mount
# This prevents Docker from creating the folder as 'root'
mkdir -p logs
chmod 777 logs

# 4. Build and start containers (Silent Build)
echo "[*] Building and starting SentinelOps container environment..."
docker-compose up --build -d > /dev/null 2>&1

# 5. Run the detection and follow the logs
echo "[*] Running threat detection and response..."
echo "----------------------------------------"

# This pulls the actual Python output to your screen
docker-compose logs -f sentinelops

echo "----------------------------------------"
echo
echo "[SUCCESS] Simulation complete."
echo "[INFO] Check the 'logs/' folder for 'alerts.log'."
echo "[INFO] Check the root folder for 'incident_report.json'."

# 6. Cleanup: Stop the container but keep the logs
docker-compose down > /dev/null 2>&1
