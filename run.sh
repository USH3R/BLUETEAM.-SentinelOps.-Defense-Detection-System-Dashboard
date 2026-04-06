#!/bin/bash
echo "========================================"
echo "   SENTINEL-OPS: DEFENSIVE SIMULATOR"
echo "========================================"

# Clear any old container state
docker-compose down --remove-orphans > /dev/null 2>&1

echo "[*] Building and starting SentinelOps container environment..."
# This command runs the container and shows the output live
docker-compose up --build

echo "----------------------------------------"
echo "[SUCCESS] Simulation complete."
