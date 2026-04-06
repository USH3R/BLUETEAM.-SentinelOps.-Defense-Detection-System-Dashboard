# main.py — SentinelOps: THE CHAOS MONKEY (v2.0)
import random
import os
import time
from detection import detect_threats
from response import execute_response

def chaos_monkey():
    """
    The Intensity Dial: 1 (Bored) to 12 (Nuke it from Orbit).
    Higher intensity means more log noise and actual file tampering.
    """
    intensity = random.randint(1, 12)
    print(f"[*] Current Threat Intensity: {intensity}/12")
    
    # --- THE THREAT LIBRARY ---
    common_noise = [
        "Failed password for root from 192.168.1.50 port 22 ssh2",
        "Failed password for admin from 45.33.12.161 port 22 ssh2",
        "CRITICAL: Multiple failed sudo attempts for user 'sysadmin'",
        "WIFI_ALERT: SSID 'FBI_MOBILE_SURVEILLANCE_TRUCK_04' detected"
    ]
    
    elite_threats = [
        "STATE-LEVEL: Rootkit 'BeaverTail' hook detected on syscall 0x80",
        "EXPLOIT: Buffer Overflow attempt in system memory at offset 0x41414141",
        "APT: Lateral movement detected - Unauthorized psexec from 10.0.0.5",
        "HYPER-THREAT: State-level 'Mega-Siphon' protocol initiated",
        "FBI_MOST_WANTED: Connection attempt from Cyber-Criminal #35"
    ]

    # --- PHASE 1: LOG INJECTION ---
    with open("auth.log", "a") as f:
        # Scale the amount of 'noise' based on intensity
        num_logs = intensity * 2
        for _ in range(num_logs):
            entry = random.choice(common_noise)
            f.write(f"Apr 06 05:10:01 sentinel-ops {entry}\n")
        
        # --- PHASE 2: ELITE ATTACK (Only triggers at high intensity) ---
        if intensity >= 8:
            big_threat = random.choice(elite_threats)
            f.write(f"Apr 06 05:12:45 sentinel-ops [CRITICAL] {big_threat}\n")
            
            # PHYSICAL CHANGE: Tamper with the evidence file
            # This forces the SHA-256 engine in detection.py to actually TRIGGER.
            with open("evidence.dat", "a") as ev:
                ev.write(f"\nMALICIOUS_INJECTION_DATA_INTENSITY_{intensity}\n")
            print("[!] Chaos Monkey: System file 'evidence.dat' has been tampered with.")

def run_simulator():
    """
    Main loop that simulates the SOC lifecycle:
    Chaos -> Detection -> Response
    """
    # Ensure evidence file exists for the integrity check to work
    if not os.path.exists("evidence.dat"):
        with open("evidence.dat", "w") as f:
            f.write("System Integrity Baseline: SECURE\n")

    # Step 1: Let the Monkey loose
    chaos_monkey()
    
    # Brief pause to simulate processing time
    time.sleep(1)

    # Step 2: Run the actual Detection Engine (Logs + Hashes + Ports)
    findings = detect_threats()

    # Step 3: Print the JSON Dashboard
    execute_response(findings)

if __name__ == "__main__":
    run_simulator()
