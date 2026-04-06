def execute_response(threats):
    if not threats:
        print("No threats detected this run.")
        return

    print("\n=== ALERTS ===")
    for t in threats:
        print(f"[ALERT] Threat detected: {t}")

    print("\n=== INCIDENT REPORT ===")
    report_summary = {
        "status": "Success",
        "threat_count": len(threats),
        "details": threats
    }
    print(report_summary)

if __name__ == "__main__":
    from detection import detect_threats
    detected = detect_threats()
    execute_response(detected)
