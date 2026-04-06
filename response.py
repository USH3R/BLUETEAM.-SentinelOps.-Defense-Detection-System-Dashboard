import yaml
from typing import List, Dict
from datetime import datetime


class ResponseEngine:
    def __init__(self, config_path: str = "settings.yaml"):
        self.config = self.load_config(config_path)

        # Load response mode
        self.mode = self.config.get("response", {}).get("mode", "alert_only")

        # Output log files
        self.alert_log_file = "alerts.log"
        self.action_log_file = "mitigation_actions.log"

    def load_config(self, path: str) -> Dict:
        try:
            with open(path, "r") as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print(f"[WARN] Config file {path} not found. Using defaults.")
            return {}

    def handle_alerts(self, alerts: List[Dict]) -> List[Dict]:
        processed_alerts = []

        for alert in alerts:
            self.log_alert(alert)

            if self.mode == "alert_only":
                alert["action_taken"] = "none"
                alert["status"] = "logged"

            elif self.mode == "simulate_block":
                action_result = self.simulate_block(alert)
                alert["action_taken"] = action_result
                alert["status"] = "mitigated"

            else:
                alert["action_taken"] = "unknown_mode"
                alert["status"] = "error"

            processed_alerts.append(alert)

        return processed_alerts

    def log_alert(self, alert: Dict):
        timestamp = datetime.now().isoformat()

        log_entry = (
            f"{timestamp} | ALERT | {alert.get('alert_type')} | "
            f"IP: {alert.get('ip')} | Severity: {alert.get('severity')} | "
            f"{alert.get('description')}\n"
        )

        with open(self.alert_log_file, "a") as f:
            f.write(log_entry)

        print(f"[ALERT] {alert.get('description')}")

    def simulate_block(self, alert: Dict) -> str:
        ip = alert.get("ip")
        timestamp = datetime.now().isoformat()

        action_entry = f"{timestamp} | ACTION | Blocked IP: {ip}\n"

        with open(self.action_log_file, "a") as f:
            f.write(action_entry)

        print(f"[ACTION] Simulated block for IP: {ip}")

        return "simulated_block"


# Standalone test
if __name__ == "__main__":
    from ingestion import LogIngestor
    from detection import ThreatEngine

    ingestor = LogIngestor()
    logs = ingestor.collect_logs()

    engine = ThreatEngine()
    alerts = engine.run_detection(logs)

    responder = ResponseEngine()
    results = responder.handle_alerts(alerts)

    print(f"\n[INFO] Processed {len(results)} alerts:\n")

    for result in results:
        print(result)
