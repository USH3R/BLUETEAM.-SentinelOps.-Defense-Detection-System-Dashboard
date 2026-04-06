import random

THREATS = [
    "Unauthorized SSH Login Attempt",
    "Malicious File Signature 'Trojan.Generic'",
    "Potential SQL Injection",
    "Suspicious sudo attempt",
    "Unusual outbound traffic",
    "Brute Force Login Attempt",
    "Unexpected Port Scan",
    "Privilege Escalation Attempt"
]

def generate_random_ip():
    return f"{random.randint(10, 200)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"

def detect_threats():
    threat_count = random.randint(1, min(5, len(THREATS)))
    detected = []
    for threat in random.sample(THREATS, threat_count):
        if "SSH" in threat or "Brute Force" in threat:
            detected.append(f"{threat} (IP: {generate_random_ip()})")
        elif "SQL Injection" in threat:
            detected.append(f"{threat} on Port {random.randint(20, 1024)}")
        elif "Port Scan" in threat:
            detected.append(f"{threat} on Ports {random.randint(20, 1024)}-{random.randint(1025, 65535)}")
        else:
            detected.append(threat)
    return detected

if __name__ == "__main__":
    sample = detect_threats()
    print(sample)
