# main.py — SentinelOps: THE TOTAL CHAOS ENGINE (v3.3 - Scorched Earth Edition)
import random
import os
import time
from detection import detect_threats
from response import execute_response

def chaos_monkey():
    # 1. CLEAN SLATE: Wipe old logs so each scan is fresh and professional
    if os.path.exists("auth.log"):
        os.remove("auth.log")

    intensity = random.randint(1, 12)
    print(f"\n[!] INITIATING SCAN - INTENSITY LEVEL: {intensity}/12")

    # 2. THE REALISTIC ARSENAL
    benign = [
        "DHCP lease renewed for workstation-04",
        "Routine backup completed: srv-01",
        "Update-manager: checking for security patches",
        "Inbound connection blocked: Port 445 (SMB)",
        "NTP synchronization successful with pool.ntp.org"
    ]

    ambiguous = [
        "Unusual login time: User 'admin' at 03:15 AM",
        "Multiple failed pings from internal gateway",
        "High outbound traffic spike to AWS-East-1",
        "Policy: Personal storage device (USB) detected",
        "Internal SSH connection from unexpected subnet"
    ]

    actual_threats = [
        "Unauthorized sudo attempt: User 'guest'",
        "SQL Injection: UNION SELECT detected",
        "Remote Code Execution (RCE) attempt",
        "Rootkit 'BeaverTail' hook on syscall",
        "APT-28: Lateral Movement detected"
    ]

    # 3. THE "SCORCHED EARTH" & EASTER EGGS
    # Added your specific requests here
    paranoid = [
        "Send hard drive to forensics. Nuke endpoint from orbit. Scorched Earth, start fresh.",
        "Wake up, Neo... The Matrix has you... Follow the white rabbit.",
        "FBI Surveillance Van SSID: 'NETGEAR_FBI'",
        "Most Wanted: Connection from Interpol #09",
        "Microphone: Background audio spike detected"
    ]

    # 4. SELECTING THE LOADOUT
    # If intensity is 1, we might just have a totally clean report
    if intensity == 1 and random.random() > 0.5:
        current_attack = [] 
    else:
        # Build the full deck
        deck = benign + ambiguous + actual_threats + paranoid
        sample_size = min(intensity + 1, len(deck))
        current_attack = random.sample(deck, k=sample_size)

    # 5. WRITE FRESH LOGS
    with open("auth.log", "w") as f:
        if not current_attack:
            f.write("Apr 06 05:45:00 sentinel-ops [SYSTEM NOMINAL] No alerts detected.\n")
        else:
            for threat in current_attack:
                ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.10"
                f.write(f"Apr 06 05:45:00 sentinel-ops [{threat}] from {ip}\n")
            
    # 6. INTEGRITY TAMPERING (Intensity 8+)
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
    run_simulator()
