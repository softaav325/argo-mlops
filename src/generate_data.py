import pandas as pd
import random

def generate_logs(n=1000):
    info_patterns = [
        "User logged in successfully",
        "Connection established to database",
        "Request processed in 20ms",
        "Heartbeat signal received",
        "Cache refreshed successfully",
        "API call returned 200 OK"
    ]
    error_patterns = [
        "Critical system failure: memory leak detected",
        "Connection timeout: unable to reach server",
        "Permission denied: access to /etc/config rejected",
        "NullPointerException at line 452 in main.py",
        "Database connection lost: unexpected shutdown",
        "Disk space critically low on /dev/sda1"
    ]
    
    data = []
    for _ in range(n):
        label = random.choice(['info', 'error'])
        text = random.choice(info_patterns if label == 'info' else error_patterns)
        data.append({'text': text, 'label': label})
        
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = generate_logs()
    df.to_csv('data/dataset.csv', index=False)
    print(f"Dataset generated with {len(df)} samples and saved to data/dataset.csv")
