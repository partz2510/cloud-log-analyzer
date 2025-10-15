# Cloud Log Analyzer

Analyze JSON log files and automatically generate alerts and summary charts.  
This project simulates a lightweight **log analysis and monitoring tool** — ideal for cloud and SOC (Security Operations Center) environments. It detects failed logins, high latency requests and generates visual summaries.

![Summary Chart](output/summary_bar.png)

---

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Sample Output](#sample-output)
- [License](#license)

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/partz2510/cloud-log-analyzer.git
   cd cloud-log-analyser
   ```


2. **Create a virtual environment and activate it**
 ```bash
python -m venv venv
venv\Scripts\activate
```


3. **Install dependencies**
 ```bash
pip install -r Logs/Requirements.txt
```

## Usage

**To analyze your log files and generate summary reports**
 ```bash
python Cloud_log_analyzer.py --logs Logs/sample_log.json --out output
```


This will:

Parse the JSON log file

Detect failed logins and high-latency events

Export alerts to **output/alerts_summary.csv**

Generate a visualization chart in **output/summary_bar.png**



## Features

🚨 Detect failed login attempts automatically

⚡ Highlight high-latency requests

📊 Generate CSV summaries of alerts

📈 Create visual charts for quick analysis

💾 Fully automated log parsing and reporting



## Sample Output

After running the script, you’ll find the following files in your output folder:	
Detailed summary of detected alerts **alerts_summary.csv**
Visualization of log categories and event counts **summary_bar.png**	



## License
This project is licensed under the MIT License.


💡 Author
Parthiban Ganesan
GitHub: partz2510
Project: Cloud Log Analyzer