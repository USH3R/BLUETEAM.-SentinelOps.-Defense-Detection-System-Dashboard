# main.py — SentinelOps: ELITE (AND SLIGHTLY PARANOID) THREAT SIMULATOR
import random
import os
from detection import detect_threats
from response import execute_response

def inject_chaos():
    """
    Simulates high-fidelity threats mixed with 
    'Most Wanted' and 'Surveillance' easter eggs.
    """
    
    threat_library = [
        # --- THE FUNNY / PARANOID STUFF ---
        "WIFI_ALERT: SSID 'FBI_MOBILE_SURVEILLANCE_TRUCK_04' detected with 99% signal strength",
        "FBI_MOST_WANTED: Connection attempt from Cyber-Criminal #35 (Alias: 'Zero-Day-Zack')",
        "SURVEILLANCE: Packet capture detected from 'White_Panel_Van_WiFi'",
        "HYPER-THREAT: State-level 'Mega-Siphon' protocol initiated by Unknown Actor",
        "MEME_VULN: Logic bomb found in 'all_your_base.sh' script",
        
        # --- STATE-LEVEL / APT ACTIVITY ---
        "APT: Lateral movement detected - Unauthorized psexec from 10.0.0.5",
        "STATE-LEVEL: Encrypted Exfiltration tunnel opened to C2 server at 185.122.x.x",
        "STATE-LEVEL: Rootkit 'BeaverTail' hook detected on syscall 0x80",
        "STUXNET-STYLE: Industrial PLC command override attempt on port 502",
        
        # --- CLASSIC HARDCORE THREATS ---
        "SQLi: Payload detected in GET request: ' OR 1=1 --",
        "XSS: Script tag detected in User-Agent header: <script>alert('pwned')</script>",
        "MALWARE: Signature 'Trojan.Generic.VBA' found in /tmp/installer.sh",
        "EXPLOIT: Buffer Overflow attempt in system memory at offset 0x41414141",
        "SPAM: SMTP Relay attack - 50,000 outbound emails queued for delivery",
        "Failed password for root from 192.168.1.50 port 22 ssh2",
        "Failed password for admin from 45.33.12.161 port 22 ssh2"
    ]

    # Inject 5-10 random threats into the log
    with open("auth.log", "a") as f:
        current_attack = random.sample(threat_library, k=random.randint(5, 10))
        for entry in current_attack:
            f.write(f"Apr 06 04:30:15 sentinel-ops {entry}\n")

    # Hardcore Integrity Trigger
    with open("evidence.dat", "w") as f:
        f.write(f"SYSTEM_COMPROMISED_ID: {random.randint(100000, 999999)}\n")
        f.write("WARNING: FBI_MOST_WANTED_LIST_SYNC_COMPLETE\n")

def run_simulator():
    if not os.path.exists("evidence.dat"):
        with open("evidence.dat", "w") as f:
            f.write("Initial Security Baseline - System Clean\n")

    inject_chaos()
    findings = detect_threats()
    execute_response(findings)

if __name__ == "__main__":
    run_simulator()
