from detection import detect_threats
from response import execute_response

def run_simulator():
    # Trigger the real detection logic
    findings = detect_threats()

    # Pass the real findings to the response readout
    execute_response(findings)

if __name__ == "__main__":
    run_simulator()
