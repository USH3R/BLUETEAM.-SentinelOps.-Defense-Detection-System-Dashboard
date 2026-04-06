# response.py
def execute_response(threats):
    """Print alerts and incident report directly to the terminal."""
    if not threats:
        print("[INFO] No threats detected.")
        return [], {"status": "No threats detected", "threat_count": 0, "details": []}
    
    # Print alerts
    print("\n=== ALERTS ===")
    for t in threats:
        alert = f"[ALERT] Threat detected: {t}"
        print(alert)
    
    # Print report summary
    report_summary = {
        "status": "Success",
        "threat_count": len(threats),
        "details": threats
    }
    
    print("\n=== INCIDENT REPORT ===")
    print(report_summary)
    
    return threats, report_summary
