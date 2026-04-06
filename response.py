import json

def execute_response(threats):
    print("\n" + "="*40)
    print("   SENTINEL-OPS: DEFENSIVE DASHBOARD")
    print("="*40)

    for t in threats:
        print(f"[*] {t}")

    report = {
        "engine_status": "Active",
        "alerts_found": len(threats) if "Secure" not in threats[0] else 0,
        "raw_data": threats
    }

    print("\n--- JSON INCIDENT SUMMARY ---")
    print(json.dumps(report, indent=4))
    print("="*40 + "\n")
