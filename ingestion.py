import re
import yaml
from typing import List, Dict, Optional


class LogIngestor:
    def __init__(self, config_path: str = "settings.yaml"):
        self.config = self.load_config(config_path)
        self.log_file = self.config.get("log_source", "auth.log")

        # Compile regex patterns once (performance + clarity)
        self.failed_login_pattern = re.compile(
            r"(?P<timestamp>\w+\s+\d+\s[\d:]+).*Failed password for (invalid user )?(?P<user>\w+) from (?P<ip>[\d\.]+)"
        )

        self.success_login_pattern = re.compile(
            r"(?P<timestamp>\w+\s+\d+\s[\d:]+).*Accepted password for (?P<user>\w+) from (?P<ip>[\d\.]+)"
        )

    def load_config(self, path: str) -> Dict:
        try:
            with open(path, "r") as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print(f"[WARN] Config file {path} not found. Using defaults.")
            return {}

    def parse_line(self, line: str) -> Optional[Dict]:
        line = line.strip()

        # Match failed login
        match = self.failed_login_pattern.search(line)
        if match:
            return {
                "timestamp": match.group("timestamp"),
                "event_type": "failed_login",
                "user": match.group("user"),
                "ip": match.group("ip"),
                "source": self.log_file,
                "raw": line
            }

        # Match successful login
        match = self.success_login_pattern.search(line)
        if match:
            return {
                "timestamp": match.group("timestamp"),
                "event_type": "successful_login",
                "user": match.group("user"),
                "ip": match.group("ip"),
                "source": self.log_file,
                "raw": line
            }

        # Unknown / unparsed log
        return {
            "timestamp": None,
            "event_type": "unknown",
            "user": None,
            "ip": None,
            "source": self.log_file,
            "raw": line
        }

    def collect_logs(self) -> List[Dict]:
        events = []

        try:
            with open(self.log_file, "r") as f:
                for line in f:
                    parsed = self.parse_line(line)
                    if parsed:
                        events.append(parsed)

        except FileNotFoundError:
            print(f"[ERROR] Log file {self.log_file} not found.")
            return []

        return events


# Standalone execution for testing
if __name__ == "__main__":
    ingestor = LogIngestor()
    logs = ingestor.collect_logs()

    print(f"\n[INFO] Parsed {len(logs)} log entries:\n")

    for log in logs[:10]:  # show first 10 entries
        print(log)
