import time
import random
import csv
import os
from datetime import datetime

# Point to the CSV in the root directory
LOG_FILE = "../../realtime_logs.csv" 

services = ["auth", "payment", "orders", "search"]
info_msgs = ["Request OK", "User login", "Cache hit"]
error_msgs = ["DB failure", "Timeout", "Null pointer"]

# 1. FIX: Add headers so Streamlit can read the columns correctly
headers = ["timestamp", "level", "service", "message"]

# Ensure the file starts fresh with headers
with open(LOG_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)

print("Real-time log producer started... Writing to realtime_logs.csv")

try:
    while True:
        level = random.choices(
            ["INFO", "WARN", "ERROR"],
            weights=[0.8, 0.1, 0.1],
        )[0]

        # Existing row logic
        row = [
            datetime.now().isoformat(),
            level,
            random.choice(services),
            random.choice(error_msgs if level == "ERROR" else info_msgs)
        ]

        # 1. Write to CSV
        with open(LOG_FILE, "a", newline="") as f:
            csv.writer(f).writerow(row)

        # 2. ADD THIS LINE: Print to terminal so you can see it live
        print(f"[{row[0]}] {row[1]} | {row[2]} | {row[3]}")

        time.sleep(0.5)
        
except KeyboardInterrupt:
    print("\nGenerator stopped.")