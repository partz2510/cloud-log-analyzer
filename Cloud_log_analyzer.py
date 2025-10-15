import json, argparse, os
from collections import defaultdict, Counter
from datetime import datetime
import matplotlib.pyplot as plt

# Thresholds for detection
THRESHOLDS = {
    "failed_login_threshold": 3,
    "high_latency_ms": 1000,
}

def parse_args():
    p = argparse.ArgumentParser(description="Cloud Log Analyzer")
    p.add_argument("--logs", required=True, help="Path to log file (JSON)")
    p.add_argument("--out", default="output", help="Output folder")
    p.add_argument("--plot", action="store_true", help="Generate chart")
    return p.parse_args()

def load_logs(path):
    with open(path, "r") as f:
        data = json.load(f)
    return data

def analyze_logs(logs):
    failed = defaultdict(int)
    high_latency = 0

    for log in logs:
        if log.get("event") == "login_failed":
            failed[log["source_ip"]] += 1
        if log.get("latency_ms", 0) > THRESHOLDS["high_latency_ms"]:
            high_latency += 1

    alerts = []
    for ip, count in failed.items():
        if count >= THRESHOLDS["failed_login_threshold"]:
            alerts.append({"type": "failed_logins", "source_ip": ip, "count": count})

    if high_latency > 0:
        alerts.append({"type": "high_latency", "count": high_latency})

    return alerts

def save_summary(alerts, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "alerts_summary.csv")
    with open(out_path, "w") as f:
        f.write("type,source_ip,count\n")
        for a in alerts:
            f.write(f"{a.get('type','')},{a.get('source_ip','')},{a.get('count','')}\n")
    print(f"[+] Alerts saved to {out_path}")

def plot_alerts(alerts, out_dir):
    if not alerts:
        print("[!] No alerts to plot.")
        return
    counts = Counter(a["type"] for a in alerts)
    plt.bar(counts.keys(), counts.values())
    plt.title("Alert Frequency")
    plt.savefig(os.path.join(out_dir, "summary_bar.png"))
    print(f"[+] Chart saved to {out_dir}/summary_bar.png")

def main():
    args = parse_args()
    logs = load_logs(args.logs)
    alerts = analyze_logs(logs)
    save_summary(alerts, args.out)
    if args.plot:
        plot_alerts(alerts, args.out)
    print("[✓] Analysis complete!")

if __name__ == "__main__":
    main()
