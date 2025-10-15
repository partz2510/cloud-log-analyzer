# Cloud Log Analyzer

Analyze JSON log files and automatically generate alerts and summary charts.

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
cd cloud-log-analyzer

2. **Create a virtual environment and activate it**
python -m venv venv
venv\Scripts\activate

3. **Install dependencies**
pip install -r Logs/Requirements.txt


## Usage
python Cloud_log_analyzer.py --logs Logs/sample_log.json --out output

## Features
**Detect failed loging attempts automatically**
**Highlight high latency requests**
**Generate CSV summaries of alerts**
**Create visual charts for quick analysis**

## Sample Output
alerts_summary.csv
summary_bar.png

## License
**This project is licensed under the MIT License**