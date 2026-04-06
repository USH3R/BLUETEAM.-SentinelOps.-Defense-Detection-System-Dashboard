# main.py - The SentinelOps Entry Point
from response import execute_response

def run_simulator():
    # Act 1: The Simulation Data
    # (In a real run, this would come from ingestion.py and detection.py)
    detected_threats = [
        "Unauthorized SSH Login Attempt (IP: 192.168.1.105)",
        "Malicious File Signature 'Trojan.Generic' Detected",
        "Potential SQL Injection on Port 80"
    ]

    # Act 2: The Readout
    # This calls your response.py logic and blasts it to the terminal
    execute_response(detected_threats)

if __name__ == "__main__":
    run_simulator()
