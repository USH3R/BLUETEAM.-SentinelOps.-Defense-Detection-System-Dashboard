import os

def detect_threats():
    """
    Scans the simulated environment (auth.log and evidence.dat) 
    to identify and categorize security anomalies.
    """
    alerts = []
    
    # 1. PARSE SIMULATED LOGS
    if os.path.exists("auth.log"):
        with open("auth.log", "r") as f:
            for line in f:
                # Extracts the string between the brackets [THREAT_NAME]
                if "[" in line and "]" in line:
                    try:
                        threat_content = line.split("[")[1].split("]")[0]
                        # Ignore the "SYSTEM NOMINAL" message for the alerts list
                        if "SYSTEM NOMINAL" not in threat_content:
                            alerts.append(f"[LOGS] {threat_content} detected")
                        else:
                            alerts.append(f"[*] [LOGS] {threat_content}")
                    except IndexError:
                        continue

    # 2. FILE INTEGRITY MONITORING (FIM)
    # Checks the "computer guts" of our enclosed .dat file
    if os.path.exists("evidence.dat"):
        with open("evidence.dat", "r") as f:
            content = f.read()
            if "MALICIOUS_HASH_BREAK" in content:
                alerts.append("[EMERGENCY] File Integrity Violation: evidence.dat tampered!")

    return alerts
