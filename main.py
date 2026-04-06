# main.py — SentinelOps: ELITE THREAT SIMULATOR
import random
import os
from detection import detect_threats
from response import execute_response

def inject_chaos():
    """
    Simulates high-fidelity, elite-level cyber threats.
    This library contains 20+ 'hardcore' signatures ranging from
    State-Level APTs to Brute Force and Malicious Payloads.
    """
    
    threat_library = [
        # --- BRUTE FORCE & CREDENTIAL HARVESTING ---
        "Failed password for root from 192.168.1.50 port 22 ssh2",
        "Failed password for admin from 45.33.12.161 port 22 ssh2",
        "CRITICAL: Multiple failed sudo attempts for user 'sysadmin' from LOCAL",
        "ALERT: Credential Stuffing detected - 500 attempts in 2 seconds from IP 103.21.244.0",
        
        # --- WEB & INJECTION ATTACKS ---
        "SQLi: Payload detected in GET request: ' OR 1=1 --",
        "SQLi: Blind-injection attempt on /api/v1/users/login",
        "XSS: Script tag detected in User-Agent header: <script>alert('XSS')</script>",
        "LFI: Directory traversal attempted: ../../../../etc/passwd",
        
        # --- MALWARE & EXPLOITS ---
        "MALWARE: Signature 'Trojan.Generic.VBA' found in /tmp/installer.sh",
        "MALWARE: Ransomware 'WannaCry.v2' file-header match in /home/user/docs",
        "EXPLOIT: Buffer Overflow attempt in system memory at offset 0x41414141",
        "EXPLOIT: Log4Shell (CVE-2021-44228) JNDI lookup detected in log stream",
        
        # --- STATE-LEVEL / APT ACTIVITY (The Hardcore Stuff) ---
        "APT: Lateral movement detected - Unauthorized psexec from 10.0.0.5",
        "APT: Golden Ticket Kerberos attack signature identified in Auth logs",
        "STATE-LEVEL: Encrypted Exfiltration tunnel opened to C2 server at 185.122.x.x",
        "STATE-LEVEL: Rootkit 'BeaverTail' hook detected on syscall 0x80",
        "STUXNET-STYLE: Industrial PLC command override attempt on port 502",
        
        # --- NETWORK & SPAM ---
        "SPAM: SMTP Relay attack - 50,000 outbound emails queued for delivery",
        "DDOS: Syn-Flood incoming from 2,000 unique source IPs",
        "SCAN: Advanced NMAP 'Stealth Scan' detected on all restricted ports",
        "DNS: Tunneling detected - suspicious TXT records on subdomain 'exfil.bad.com'"
    ]

    # 1. Inject a random number of threats (between 4 and 8) into auth.log
    with open("auth.log", "a") as f:
        # Pick random threats without repeating in the same run
        current_attack = random.sample(threat_library, k=random.randint(4, 8))
        for entry in current_attack:
            # We add a timestamp to make it look like a real log
            f.write(f"Apr 06 04:20:01 sentinel-ops {entry}\n")

    # 2. Hardcore Integrity Trigger (Always modify the file to show detection)
    with open("evidence.dat", "w") as f:
        f.write(f"SYSTEM_COMPROMISED_ID: {random.randint(100000, 999999)}\n")
        f.write("WARNING: FILE INTEGRITY ENGINE TRIGGERED - HASH MISMATCH\n")

def run_simulator():
    """Main execution loop."""
    # Safety check for the baseline file
    if not os.path.exists("evidence.dat"):
        with open("evidence.dat", "w") as f:
            f.write("Initial Security Baseline - System Clean\n")

    # ACT 0: Generate the Elite Chaos
    inject_chaos()

    # ACT 1: Run the Detection Engine (Logs, Hash, Ports)
    findings = detect_threats()

    # ACT 2: Output the Dynamic JSON Dashboard
    execute_response(findings)

if __name__ == "__main__":
    run_simulator()
