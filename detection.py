import os
import hashlib
import socket
import json

BASELINE_FILE = "checksums.json"

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

    # --- ENGINE 1: SHA-256 INTEGRITY CHECK ---
    # We watch this specific file for any terminal-based 'tampering'
    target_file = "evidence.dat"
    
    if os.path.exists(BASELINE_FILE):
        with open(BASELINE_FILE, "r") as f:
            stored_baseline = json.load(f)
    else:
        stored_baseline = {}

    if os.path.exists(target_file):
        f_hash = get_file_hash(target_file)
        current_baseline[target_file] = f_hash
        
        if target_file in stored_baseline and stored_baseline[target_file] != f_hash:
            detected.append(f"[INTEGRITY] Hash Mismatch! {target_file} was modified.")
    
    # Save the hash for the next run
    with open(BASELINE_FILE, "w") as f:
        json.dump(current_baseline, f)

    # --- ENGINE 2: LOG PARSING (AUTH.LOG) ---
    if os.path.exists("auth.log"):
        with open("auth.log", "r") as f:
            failures = [line for line in f if "Failed password" in line]
            if failures:
                detected.append(f"[LOGS] {len(failures)} Brute Force attempts found in auth.log")

    # --- ENGINE 3: NETWORK PORT SCAN ---
    # Scans standard ports to see what's open in the environment
    for port in [22, 80, 443]:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.01)
            if s.connect_ex(("127.0.0.1", port)) == 0:
                detected.append(f"[NETWORK] Open Service detected on Port {port}")

    return detected if detected else ["System Status: Secure. No anomalies detected."]
