from collections import defaultdict
from typing import List, Dict
import yaml


class ThreatEngine:
    def __init__(self, config_path: str = "settings.yaml"):
        self.config = self.load_config(config_path)

        # Load thresholds from config
        self.brute_force_threshold = (
            self.config.get("thresholds", {}).get("brute_force", 5)
        )

        # Internal state tracking
        self.failed_attempts = defaultdict(int)

    def load_config(self, path: str) -> Dict:
        try:
            with open(path, "r") as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print(f"[WARN] Config file {path} not found. Using defaults.")
            return {}

    def detect_brute_force(self, events: List[Dict]) -> List[Dict]:
        alerts = []

        for event in events:
            if event["event_type"] == "failed_login":
                ip = event.get("ip")

                if not ip:
                    continue

                self.failed_attempts[ip] += 1

                if self.failed_attempts[ip] == self.brute_force_threshold:
                    alerts.append({
                        "alert_type": "brute_force",
                        "ip": ip,
                        "count": self.failed_attempts[ip],
                        "severity": "high",
                        "description": f"Detected {self.failed_attempts[ip]} failed login attempts from {ip}",
                        "source": event.get("source"),
                    })

        return alerts

    def detect_suspicious_keywords(self, events: List[Dict]) -> List[Dict]:
        alerts = []

        suspicious_keywords = ["sudo", "root", "admin"]

        for event in events:
            raw = event.get("raw", "").lower()

            if any(keyword in raw for keyword in suspicious_keywords):
                alerts.append({
                    "alert_type": "suspicious_activity",
                    "ip": event.get("ip"),
                    "severity": "medium",
                    "description": f"Suspicious keyword detected in log: {event.get('raw')}",
                    "source": event.get("source"),
                })

        return alerts

    def run_detection(self, events: List[Dict]) -> List[Dict]:
        all_alerts = []

        # Run all detection modules
        all_alerts.extend(self.detect_brute_force(events))
        all_alerts.extend(self.detect_suspicious_keywords(events))

        return all_alerts


# Standalone test
if __name__ == "__main__":
    from ingestion import LogIngestor

    ingestor = LogIngestor()
    logs = ingestor.collect_logs()

    engine = ThreatEngine()
    alerts = engine.run_detection(logs)

    print(f"\n[INFO] Generated {len(alerts)} alerts:\n")

    for alert in alerts:
        print(alert)
