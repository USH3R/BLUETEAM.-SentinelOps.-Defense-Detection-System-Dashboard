# main.py — SentinelOps Chaos Engine & Entry Point
import random
import os
from detection import detect_threats
from response import execute_response

def inject_chaos():
    """
    Simulates real-world background noise and threats.
    This ensures the 'detection.py' engine has fresh data to find.
    """
    
    # 1. Inject 1-5 new Brute Force attempts into the log file
    log_file = "auth.log"
    with open(log_file, "a") as f:
        count = random.randint(1, 5)
        for _ in range(count):
            fake_ip = f"{random.randint(10, 200)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
            f.write(f"Apr 06 04:20:01 sentinel sshd[123]: Failed password for root from {fake_ip} port 22 ssh2\n")

    # 2. Randomly Tamper with Evidence (50% chance of an Integrity Alert)
    target_file = "evidence.dat"
    if random.choice([True, False]):
        with open(target_file, "w") as f:
            # Writing a random timestamp changes the SHA-256 hash
            f.write(f"Modification Detected at: {random.uniform(0, 1000)}\n")

def run_simulator():
    """Main execution loop for the Defensive Dashboard."""
    
    # Ensure our target file exists for the first run
    if not os.path.exists("evidence.dat"):
        with open("evidence.dat", "w") as f:
            f.write("Initial Security Baseline\n")

    # ACT 0: Create the chaos (Terminal-Only Automation)
    inject_chaos()

    # ACT 1: Run the real triple-engine detection (Logs, Hash, Ports)
    findings = detect_threats()

    # ACT 2: Output the dynamic findings to the dashboard
    execute_response(findings)

if __name__ == "__main__":
    run_simulator()
