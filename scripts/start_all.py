import subprocess
import threading

def run_bot():
    subprocess.run(["python", "scripts/vip_access_bot.py"])

def run_ai():
    subprocess.run(["python", "run_ai.py"])

threading.Thread(target=run_bot).start()
threading.Thread(target=run_ai).start()