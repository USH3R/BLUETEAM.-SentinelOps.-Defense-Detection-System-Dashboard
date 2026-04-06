# **BLUE TEAM. SentinelOps – Defensive Security Simulator**  
![Role – Defender](https://img.shields.io/badge/Role-Defender-blue?style=for-the-badge&logo=hackthebox)
![Skill – Threat Detection Automation](https://img.shields.io/badge/Skill-Threat_Detection_Automation-yellow?style=for-the-badge&logo=python)
![Output – Incident Report Dashboard](https://img.shields.io/badge/Output-Incident_Report_Dashboard-green?style=for-the-badge)
![Compliance – NIST_800-53/FISMA](https://img.shields.io/badge/Compliance-NIST_800--53%2FFISMA-blueviolet?style=for-the-badge)
![Simulation – Real-Time SOC Lab](https://img.shields.io/badge/Simulation-Real_Time_SOC_Lab-lightgrey?style=for-the-badge&logo=flask&logoColor=white)
![Detection – Brute Force & Anomaly Alerts](https://img.shields.io/badge/Detection-Brute_Force_&_Anomaly_Alerts-orange?style=for-the-badge)  
A controlled, defensive security platform that simulates monitoring, detecting, and responding to suspicious activity in a protected environment.  
✅ Simulates real-world defensive actions  
Detects brute-force login attempts  
Identifies anomalous logins and suspicious behavior  
Monitors system and network events for misuse  
✅ Follows defender workflow  
  
**Chain:**  
Log collection (system, network, application logs)  
Analysis & correlation (detect anomalies)  
Alerting & response (generate actionable alerts)  
Reporting (structured incident summaries)  
  
**Stack:**  
Python (automation & analysis)  
Docker (log collection/testing environments)  
Bash scripts  
Optional: lightweight web UI or CLI dashboard  
  
**Features:**  
Centralized log ingestion from multiple sources  
Real-time detection of suspicious activity  
Rule-based alerting for brute-force, impossible-travel, and process anomalies  
Visualization of events and attack timelines  
  
**Detection modules:**  
Brute-force login detection  
Anomalous behavior correlation  
Suspicious process monitoring  
  
**Reporting engine:**  
Generates PDF or HTML “incident reports”  
Logs actionable alerts for security operations teams  
  
# **Blue Team SentinelOps Structure**  
**Primary Files / Structure**  
blueteam-sentinelops/  
├── main.py  
├── ingestion.py  
├── detection.py  
├── response.py   
├── reporting.py  
├── settings.yaml  
└── Dockerfile  
  
**Blue Team Workflow**  
[Detection] → [Analysis] → [Response] → [Reporting]  

Future Files / Structure  
blueteam-sentinelops/  
├── orchestrator/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# controls detection + response flow  
├── ingestion/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   # log collection + normalization  
├── detection_modules/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# detection rules + analytics  
├── correlation/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# event linking + anomaly logic  
├── response/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# automated responses / playbooks  
├── reporting/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# incident reports + dashboards  
├── lab_env/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# simulated log sources (attack traffic)  
└── rules_of_engagement/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# safety + compliance  
  
Potential / Future Files / Structure  
blueteam-sentinelops/  
│  
├── README.md  
├── LICENSE  
├── requirements.txt  
├── docker-compose.yml  
├── docs/  
│ ├── architecture.md  
│ ├── detection_workflow.md  
│ ├── nist_mapping.md  
│ └── rules_of_engagement.md  
├── config/  
│ ├── settings.yaml  
│ ├── detection_rules.yaml  
│ └── log_sources.yaml  
├── lab_env/  
│ ├── attacker_sim/  
│ │ ├── brute_force.py  
│ │ └── traffic_gen.py  
│ ├── web_logs/  
│ │ ├── Dockerfile  
│ │ └── access.log  
│ ├── auth_logs/  
│ │ ├── Dockerfile  
│ │ └── auth.log  
│ └── system_logs/  
│ ├── Dockerfile  
│ └── syslog.log  
├── orchestrator/  
│ ├── main.py  
│ ├── pipeline.py  
│ └── scheduler.py  
├── ingestion/  
│ ├── log_collector.py  
│ ├── parser.py  
│ └── utils.py  
├── detection_modules/  
│ ├── brute_force/  
│ │ ├── detector.py  
│ │ └── thresholds.yaml  
│ ├── anomaly/  
│ │ ├── impossible_travel.py  
│ │ └── behavior_model.py  
│ └── process_monitor/  
│ └── suspicious_process.py  
├── correlation/  
│ ├── event_linker.py  
│ ├── timeline_builder.py  
│ └── logic.py  
├── response/  
│ ├── alert_manager.py  
│ ├── playbooks/  
│ │ ├── brute_force_response.py  
│ │ ├── anomaly_response.py  
│ │ └── containment.py  
│ └── notifier.py  
├── reporting/  
│ ├── report_generator.py  
│ ├── templates/  
│ │ ├── incident.html  
│ │ └── timeline.html  
│ └── output/  
│ └── (generated reports here)  
├── dashboard/  
│ ├── app.py  
│ └── templates/  
│ └── index.html  
├── logs/  
│ ├── events.log  
│ ├── alerts.log  
│ └── incidents.log  
└── tests/  
├── test_ingestion.py  
├── test_detection.py  
├── test_correlation.py  
└── test_pipeline.py  
  
**Prove or show the following:**  
Understanding of defensive workflows and SOC operations  
Automation and analysis skills  
Real-time alerting and reporting  
  
**👉 Bonus:**  
“Rules of engagement” section for safe testing and ethical handling of simulated attacks  

# **Portfolio Context**  
  
This project is part of a full-spectrum cybersecurity portfolio that demonstrates end-to-end capability in offensive, defensive, and secure system design workflows:  
**Red Team (OffSec Simulator):** Simulates attacker workflows and penetration testing.  
https://github.com/USH3R/REDTEAM.-Offensive-Security-Simulator  
**Blue Team (SentinelOps):** Detects threats and generates actionable incident reports.  
**Zero Trust (Federal File Sharing System):** Builds secure, auditable, zero trust-compliant systems.  
https://github.com/USH3R/ZEROTRUSTFS.-Security-Toolkit.-NPM-Containers.-Federal-File-Sharing-System./tree/main  
Together, these projects showcase full-spectrum cybersecurity capability, illustrating that the author can attack, defend, and build secure systems across the complete security lifecycle.  

# **Instructions to Run BLUE TEAM SentinelOps Defense Detection System Dashboard**  
Using GitHub Codespaces (Recommended)
1. Click the green '<> Code' button on this repo, then
2. Select the tab called Codespaces, then
3. Select (click on) 'Create codespace on main'.
2. Once the Terminal loads, simply type: python3 main.py

# **Notes**
This app mimics a professional DevSecOps workflow where security policies are 'Infrastructure as Code' (IaC). You don't just 'click a button' to block IPs; you update a policy file for auditability.
**🔍 Logic Check**
In the handle_alerts loop:  
  
if self.mode == "alert_only":  
    alert["action_taken"] = "none"  
    alert["status"] = "logged"  
elif self.mode == "simulate_block":  
    # ... logic ...  
  
in the settings.yaml, the mode is currently set to  
  
alert_only.  
  
If the user wants to test the blocking logic the settings.yaml file must be updated to:  
  
simulate_block  
  
(matching the elif statement). It’s a clean way to toggle the "defensive posture" of the app.  
