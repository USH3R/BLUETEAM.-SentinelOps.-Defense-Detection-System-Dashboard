# main.py — SentinelOps: THE TOTAL CHAOS ENGINE (v3.1)
import random
import os
import time
from detection import detect_threats
from response import execute_response

def chaos_monkey():
    # 1. CLEAN SLATE: Wipe old logs so each scan is fresh
    if os.path.exists("auth.log"):
        os.remove("auth.log")

    intensity = random.randint(1, 12)
    print(f"\n[!] INITIATING SCAN - INTENSITY LEVEL: {intensity}/12")

    # 2. THE THREAT ARSENAL
    noise = ["Failed password for root", "Unauthorized sudo attempt", "Port scan detected on 0-1024"]
    exploits = ["Buffer Overflow blocked", "SQL Injection: UNION SELECT", "Remote Code Execution (RCE) attempt"]
    state_level = ["APT-28: Lateral Movement", "Rootkit 'BeaverTail' hook", "Exfiltration to unknown IP"]
    paranoid = ["FBI Surveillance Van SSID: 'NETGEAR_FBI'", "Most Wanted: Connection from Interpol #09", "Hardware: Unauthorized USB device"]

    deck = noise + exploits + state_level + paranoid
    
    # Pick unique items
    sample_size = min(intensity + 1, len(deck))
    current_attack = random.sample(deck, k=sample_size)

    # 3. WRITE FRESH LOGS
    with open("auth.log", "w") as f: # Use "w" to overwrite, not "a" to append
        for threat in current_attack:
            ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.10"
            f.write(f"Apr 06 05:45:00 sentinel-ops [{threat}] from {ip}\n")
            
    # 4. INTEGRITY TAMPERING (Intensity 8+)
    if intensity >= 8:
        print("[*] Chaos Monkey: High Intensity detected. Injecting file corruption...")
        with open("evidence.dat", "a") as ev:
            ev.write(f"MALICIOUS_HASH_BREAK_{random.randint(1000, 9999)}\n")

def run_simulator():
    if not os.path.exists("evidence.dat"):
        with open("evidence.dat", "w") as f:
            f.write("BASELINE: SECURE\n")

    chaos_monkey()
    time.sleep(0.5)
    findings = detect_threats()
    execute_response(findings)

if __name__ == "__main__":
    run_simulator()# main.py — SentinelOps: THE TOTAL CHAOS ENGINE (v3.0)
import random
import os
import time
from detection import detect_threats
from response import execute_response

def chaos_monkey():
    """
    The Automated Chaos Monkey.
    Uses unique sampling to prevent repetitive 'Hard Pull' logs.
    """
    # 1. THE INTENSITY DIAL (1 to 12)
    intensity = random.randint(1, 12)
    print(f"\n[!] INITIATING SCAN - INTENSITY LEVEL: {intensity}/12")

    # 2. THE THREAT ARSENAL (Unique Categories)
    noise = [
        "Failed password for root", 
        "Unauthorized sudo attempt", 
        "SSH Brute Force: 50+ attempts",
        "Port scan detected on 0-1024"
    ]
    exploits = [
        "Buffer Overflow blocked in memory", 
        "SQL Injection: UNION SELECT detected", 
        "Remote Code Execution (RCE) attempt",
        "Cross-Site Scripting (XSS) payload found"
    ]
    state_level = [
        "APT-28: Lateral Movement detected", 
        "Rootkit 'BeaverTail' hook on syscall", 
        "Data Exfiltration: 2GB to unknown IP",
        "Zero-Day Exploit: CVE-2026-X unknown"
    ]
    paranoid = [
        "FBI Surveillance Van SSID: 'NETGEAR_FBI'", 
        "Most Wanted: Connection from Interpol #09",
        "Hardware: Unauthorized USB device mounted",
        "Microphone: Background audio spike detected"
    ]

    # Combine all into a single deck
    deck = noise + exploits + state_level + paranoid
    
    # 3. DIVERSITY CHECK (The Fix)
    # This ensures we pick UNIQUE items. No more repeating the same log 10 times.
    sample_size = min(intensity + 1, len(deck))
    current_attack = random.sample(deck, k=sample_size)

    # 4. EXECUTE ATTACK (Write to Logs and Files)
    with open("auth.log", "a") as f:
        for threat in current_attack:
            # Randomize the IP to make the SOC look busy
            ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.10"
            f.write(f"Apr 06 05:45:00 sentinel-ops [{threat}] from {ip}\n")
            
    # 5. INTEGRITY TAMPERING (Trigger the SHA-256 Alert)
    if intensity >= 8:
        print("[*] Chaos Monkey: High Intensity detected. Injecting file corruption...")
        with open("evidence.dat", "a") as ev:
            ev.write(f"MALICIOUS_HASH_BREAK_{random.randint(1000, 9999)}\n")

def run_simulator():
    """
    The Full Automated Loop: Chaos -> Detection -> Response
    """
    # Ensure baseline files exist
    if not os.path.exists("evidence.dat"):
        with open("evidence.dat", "w") as f:
            f.write("BASELINE: SECURE\n")

    # Run the Chaos Engine
    chaos_monkey()
    
    # Pause for "Processing" feel
    time.sleep(0.5)

    # Run the Detection Engine (Logic is in detection.py)
    findings = detect_threats()

    # Output the Final JSON Dashboard (Logic is in response.py)
    execute_response(findings)

if __name__ == "__main__":
    run_simulator()
