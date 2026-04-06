# detection.py
import random

def generate_random_ip():
    """Generate a random IPv4 address."""
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

def generate_random_port():
    """Generate a random port number for port-based alerts."""
    return random.randint(1, 65535)

def detect_threats():
    """Simulate threat detection with randomized alerts."""
    possible_threats = [
        lambda: f"Unauthorized SSH Login Attempt (IP: {generate_random_ip()})",
        lambda: f"Malicious File Signature 'Trojan.Generic' Detected",
        lambda: f"Potential SQL Injection on Port {generate_random_port()}",
        lambda: f"Port Scan Detected from IP: {generate_random_ip()}",
        lambda: f"Suspicious Brute Force Login Attempt (IP: {generate_random_ip()})"
    ]

    # Randomly pick between 1 and 5 threats per run
    threat_count = random.randint(1, 5)
    selected_threats = random.sample(possible_threats, threat_count)

    # Execute the lambdas to get threat strings
    return [threat() for threat in selected_threats]

# Example usage when running detection.py standalone
if __name__ == "__main__":
    threats = detect_threats()
    for t in threats:
        print("[ALERT]", t)
