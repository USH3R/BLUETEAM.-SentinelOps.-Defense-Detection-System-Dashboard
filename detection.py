import os
import hashlib
import socket
import json

# --- CONFIGURATION ---
# This tracks file changes for the integrity engine
BASELINE_FILE = "checksums.json"
TARGET_FILE = "evidence.dat"

def get_file_hash(filepath):
    """Calculates the SHA-256 hash of a file for integrity monitoring."""
    hasher = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

def detect_threats():
    """
    SentinelOps Detection Engine:
    Parses logs for elite threats, checks file integrity, and scans ports.
    """
    detected = []
    current_baseline = {}

    # --- ENGINE 1: SHA-256 INTEGRITY CHECK ---
    # Detects if an attacker (or a mobile van) tampered with system files
    if os.path.exists(BASELINE_FILE):
        with open(BASELINE_FILE, "r") as f:
            stored_baseline = json.load(f)
    else:
        stored_baseline = {}

    if os.path.exists(TARGET_FILE):
        f_hash = get_file_hash(TARGET_FILE)
        current_baseline[TARGET_FILE] = f_hash
        
        if TARGET_FILE in stored_baseline and stored_baseline[TARGET_FILE] != f_hash:
            detected.append(f"[CRITICAL] Hash Mismatch! {TARGET_FILE} tampered by attacker.")
    
    # Save the hash for the next run comparison
    with open(BASELINE_FILE, "w") as f:
        json.dump(current_baseline, f)

    # --- ENGINE 2: ELITE LOG PARSING (WITH EASTER EGGS) ---
    # This loop reads every line in auth.log and categorizes the 'flavor' of the s***
    if os.path.exists("auth.log"):
        with open("auth.log", "r") as f:
            logs = f.readlines()
            for line in logs:
                # 1. The 'Hardcore' Threats
                if "SQLi" in line:
                    detected.append("[ATTACK] SQL Injection attempt detected in logs")
                elif "MALWARE" in line:
                    detected.append("[MALWARE] Trojan/Ransomware signature found")
                elif "APT" in line or "STATE-LEVEL" in line:
                    detected.append("[EMERGENCY] State-Level APT Activity Detected!")
                elif "EXPLOIT" in line:
                    detected.append("[EXPLOIT] Memory/Buffer Overflow attempt blocked")
                
                # 2. The 'Funny/Paranoid' Threats
                elif "FBI_MOBILE" in line:
                    detected.append("[PARANOID] Surveillance Van Detected: Hide the servers!")
                elif "MOST_WANTED" in line:
                    detected.append("[HIGH_PRIORITY] FBI Most Wanted Cyber-Criminal Activity!")
                elif "HYPER-THREAT" in line:
                    detected.append("[CRITICAL] Hyper-Threat Attack in Progress!")
                elif "WIFI_ALERT" in line:
                    detected.append("[WIFI] Rogue Access Point / Surveillance Signal detected")
                
                # 3. Standard Noise
                elif "Failed password" in line:
                    detected.append("[LOGS] Brute Force login attempt logged")

    # --- ENGINE 3: NETWORK PORT SCAN ---
    # Verifies if common service ports are exposed to the 'neighborhood'
    for port in [22, 80, 443]:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.01)
            if s.connect_ex(("127.0.0.1", port)) == 0:
                detected.append(f"[NETWORK] Active Service on Port {port}")

    # Return the list of findings, or a 'Secure' message if all is quiet
    return detected if detected else ["System Status: Secure. No anomalies detected."]
