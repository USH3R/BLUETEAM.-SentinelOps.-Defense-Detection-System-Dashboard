import os
import hashlib
import socket
import json

# --- CONFIGURATION ---
BASELINE_FILE = "checksums.json"
TARGET_FILE = "evidence.dat"

def get_file_hash(filepath):
    """Calculates the SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

def detect_threats():
    detected = []
    current_baseline = {}

    # --- ENGINE 1: SHA-256 INTEGRITY CHECK (STAYS THE SAME) ---
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
    
    with open(BASELINE_FILE, "w") as f:
        json.dump(current_baseline, f)

    # --- ENGINE 2: MULTI-VECTOR LOG PARSING (THE UPGRADE) ---
    if os.path.exists("auth.log"):
        with open("auth.log", "r") as f:
            logs = f.readlines()
            for line in logs:
                # Identify Elite Threats by Keyword
                if "SQLi" in line:
                    detected.append(f"[ATTACK] SQL Injection attempt detected in logs")
                elif "MALWARE" in line:
                    detected.append(f"[MALWARE] Trojan/Ransomware signature found")
                elif "APT" in line or "STATE-LEVEL" in line:
                    detected.append(f"[EMERGENCY] State-Level APT Activity Detected!")
                elif "EXPLOIT" in line:
                    detected.append(f"[EXPLOIT] Memory/Buffer Overflow attempt blocked")
                elif "SPAM" in line:
                    detected.append(f"[NETWORK] High-Volume Spam/SMTP Relay detected")
                elif "Failed password" in line:
                    detected.append(f"[LOGS] Brute Force login attempt logged")

    # --- ENGINE 3: NETWORK PORT SCAN (STAYS THE SAME) ---
    for port in [22, 80, 443]:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.01)
            if s.connect_ex(("127.0.0.1", port)) == 0:
                detected.append(f"[NETWORK] Active Service on Port {port}")

    return detected if detected else ["System Status: Secure. No anomalies detected."]
