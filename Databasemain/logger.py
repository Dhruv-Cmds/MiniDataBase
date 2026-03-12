from datetime import datetime
import os

def log(message):

    time = datetime.now().strftime("%H:%M:%S")

    os.makedirs("database", exist_ok=True)  # ensures folder exists

    with open("database/logs.txt", "a") as f:
        f.write(f"[{time}] {message}\n")