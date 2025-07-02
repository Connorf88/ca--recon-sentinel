# 🔍 CAI Recon Sentinel

An autonomous AI agent for passive reconnaissance, powered by the [Cybersecurity AI (CAI) Framework](https://github.com/aliasrobotics/cai) by Alias Robotics. This project demonstrates how agentic workflows can enhance threat intelligence and reconnaissance by automating domain and IP analysis tasks.

---

## 🚀 Features

- 🧠 Agentic architecture using CAI’s Reasoning + Acting model (ReAct)
- 🌐 Passive recon via:
  - WHOIS domain lookups
  - Shodan API scanning
  - DNS-based subdomain enumeration
- 🧾 Transparent logging of every task + reasoning step (HITL-friendly)
- 🧩 Modular task design — easy to extend or swap
- 💻 CLI-compatible — runs in local VMs or cloud shells

---

## 📂 Project Structure

cai-recon-sentinel/ ├── agents/ │ └── recon_agent.py # Core agent that orchestrates tasks ├── tasks/ │ ├── whois_lookup.py # WHOIS lookups │ ├── shodan_scan.py # Passive Shodan scan │ └── subdomain_enum.py # DNS-based subdomain sweep ├── config/ │ └── agent_config.yaml # YAML to register tasks & agent ├── results/ │ └── logs.json # Output logs + AI reasoning ├── examples/ │ └── demo_run.md # Example walkthrough or usage output ├── requirements.txt ├── .gitignore └── README.md


---

## ⚙️ Setup Instructions

### 1. Set up a virtual environment

```bash
python3 -m venv cai_env
source cai_env/bin/activate
2. Install dependencies
bash
pip install cai-framework shodan python-whois dnspython
Update requirements.txt if necessary.

3. Add your Shodan API Key
Get one at https://account.shodan.io, then add it to shodan_scan.py.

🧪 Running the Agent
bash
cai run --config config/agent_config.yaml --input "example.com"
The agent will run tasks in sequence and output results and logs to the results/ directory.

🛠️ Customization Ideas
Add VirusTotal or OTX integrations

Create a Slack or Discord bot interface

Hook into GitHub Actions for CI-based recon jobs

Deploy with Docker or as a microservice

💡 Use Cases
🕵️ Recon automation for red teams and CTF pre-enum

👨‍🏫 Teaching AI + cybersecurity in hands-on labs

🧠 Experimenting with autonomous agents and HITL design

📜 License
This project is licensed under the MIT License.

👤 Author
Connor DevOps | Cloud Infrastructure | Cybersecurity AI | Free-tier Lab Architect GitHub Profile Featured in: Zero-Budget GitOps Lab
