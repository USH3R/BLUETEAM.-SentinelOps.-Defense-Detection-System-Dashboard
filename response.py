import os
import json

# Paths inside the container
ALERTS_FILE = "/app/logs/alerts.log"
REPORT_FILE = "/app/incident_report.json"  # Root of repo so 'cat incident_report.json' works

def write_alerts(alerts):
    """Writes each alert string to the alerts.log file."""
    os.makedirs(os.path.dirname(ALERTS_FILE), exist_ok=True)
    try:
        with open(ALERTS_FILE, "a") as f:
            for alert in alerts:
                f.write(alert + "\n")
        print(f"[INFO] Alerts written to {ALERTS_FILE}")
    except Exception as e:
        print(f"[ERROR] Could not write alerts: {e}")

def write_report(report_data):
    """Writes the final summary to the incident_report.json file."""
    os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)
    try:
        with open(REPORT_FILE, "w") as f:
            json.dump(report_data, f, indent=4)
        print(f"[INFO] Incident report written to {REPORT_FILE}")
    except Exception as e:
        print(f"[ERROR] Could not write report: {e}")

def execute_response(threats):
    """Bridge function for main.py to trigger the logging logic."""
    if not threats:
        return
    
    formatted_alerts = [f"[ALERT] Threat detected: {t}" for t in threats]
    write_alerts(formatted_alerts)
    
    report_summary = {
        "status": "Success",
        "threat_count": len(threats),
        "details": threats
    }
    write_report(report_summary)

if __name__ == "__main__":
    sample_alerts = ["Failed login from 192.168.1.10", "Suspicious sudo attempt"]
    execute_response(sample_alerts)import os
import json

ALERTS_FILE = "/app/logs/alerts.log"
REPORT_FILE = "/app/incident_report.json"

def write_alerts(alerts):
    os.makedirs(os.path.dirname(ALERTS_FILE), exist_ok=True)
    try:
        with open(ALERTS_FILE, "a") as f:
            for alert in alerts:
                f.write(alert + "\n")
        print(f"[INFO] Alerts written to {ALERTS_FILE}")
    except Exception as e:
        print(f"[ERROR] Could not write alerts: {e}")

def write_report(report_data):
    # Ensure parent directory exists
    os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)
    try:
        with open(REPORT_FILE, "w") as f:
            json.dump(report_data, f, indent=4)
        print(f"[INFO] Incident report written to {REPORT_FILE}")
    except Exception as e:
        print(f"[ERROR] Could not write report: {e}")

def execute_response(threats):
    if not threats:
        return
    
    formatted_alerts = [f"[ALERT] Threat detected: {t}" for t in threats]
    write_alerts(formatted_alerts)
    
    report_summary = {
        "status": "Success",
        "threat_count": len(threats),
        "details": threats
    }
    write_report(report_summary)

if __name__ == "__main__":
    sample_alerts = ["Failed login from 192.168.1.10", "Suspicious sudo attempt"]
    execute_response(sample_alerts)import os
import json

ALERTS_FILE = "/app/logs/alerts.log"
REPORT_FILE = "/app/incident_report.json"

def write_alerts(alerts):
    os.makedirs(os.path.dirname(ALERTS_FILE), exist_ok=True)
    try:
        with open(ALERTS_FILE, "a") as f:
            for alert in alerts:
                f.write(alert + "\n")
        print(f"[INFO] Alerts written to {ALERTS_FILE}")
    except Exception as e:
        print(f"[ERROR] Could not write alerts: {e}")

def write_report(report_data):
    # Ensure parent directory exists
    os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)
    try:
        with open(REPORT_FILE, "w") as f:
            json.dump(report_data, f, indent=4)
        print(f"[INFO] Incident report written to {REPORT_FILE}")
    except Exception as e:
        print(f"[ERROR] Could not write report: {e}")

def execute_response(threats):
    if not threats:
        return
    
    formatted_alerts = [f"[ALERT] Threat detected: {t}" for t in threats]
    write_alerts(formatted_alerts)
    
    report_summary = {
        "status": "Success",
        "threat_count": len(threats),
        "details": threats
    }
    write_report(report_summary)

if __name__ == "__main__":
    sample_alerts = ["Failed login from 192.168.1.10", "Suspicious sudo attempt"]
    execute_response(sample_alerts)
