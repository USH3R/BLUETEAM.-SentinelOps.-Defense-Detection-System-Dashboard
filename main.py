import random
import os
import time
from detection import detect_threats
from response import execute_response

def chaos_monkey():
    # 1. CLEAN SLATE
    if os.path.exists("auth.log"):
        os.remove("auth.log")

    intensity = random.randint(1, 12)
    print(f"\n[!] INITIATING SCAN - INTENSITY LEVEL: {intensity}/12")

    # 2. BENIGN NOISE
    benign = [
        "DHCP lease renewed for workstation-04",
        "Routine backup completed: srv-01",
        "Update-manager: checking for security patches",
        "Inbound connection blocked: Port 445 (SMB)",
        "NTP synchronization successful"
    ]

    # 3. AMBIGUOUS / ANALYST WORKLOAD
    ambiguous = [
        "Unusual login time: User 'admin' at 03:15 AM",
        "Multiple failed pings from internal gateway",
        "High outbound traffic spike to AWS-East-1",
        "Policy: Personal storage device (USB) detected",
        "User Training Required: Phishing link clicked"
    ]

    # 4. ACTUAL THREATS
    actual_threats = [
        "Unauthorized sudo attempt: User 'guest'",
        "SQL Injection: UNION SELECT",
        "Remote Code Execution (RCE) attempt",
        "Rootkit 'BeaverTail' hook on syscall",
        "APT-28: Lateral Movement"
    ]

    # 5. THE UPDATED "CHAOS" LIBRARY (Cleaned & Separated)
    chaos_library = [
        "Send hard drive to forensics.",
        "Launch endpoint into orbit. Start fresh",
        "Wake up, Neo...",
        "The Matrix has you... Follow the white rabbit.",
        "FBI Mobile Truck: 'NETGEAR_FBI'",
        "Most Wanted: Connection from Interpol #09",
        "Microphone: Background audio spike"
    ]

    # 6. LOGIC: SAMPLE THE DECK
    if intensity == 1 and random.random() > 0.5:
        current_attack = [] 
    else:
        deck = benign + ambiguous + actual_threats + chaos_library
        sample_size = min(intensity + 1, len(deck))
        current_attack = random.sample(deck, k=sample_size)

    # 7. WRITE TO LOGS
    with open("auth.log", "w") as f:
        if not current_attack:
            f.write("Apr 06 05:45:00 sentinel-ops [SYSTEM NOMINAL] No alerts detected.\n")
        else:
            for threat in current_attack:
                ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.10"
                f.write(f"Apr 06 05:45:00 sentinel-ops [{threat}] from {ip}\n")
            
    # 8. INTEGRITY TAMPERING (Intensity 8+)
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
