import time
import subprocess

def get_percentage():
    with open("/sys/class/power_supply/BAT0/capacity", "r") as file:
        percentage = file.read().strip()

    return percentage

def get_status():
    with open("/sys/class/power_supply/BAT0/status", "r") as file:
        status = file.read().strip()

    return status

def notify(percentage):
    subprocess.run(["notify-send", f"Battery remaining: {percentage}%. Please charge!"])

def main():
    percentage = int(get_percentage())
    status = get_status()

    if percentage < 20 and status == "Discharging":
        notify(percentage)
        time.sleep(300)
    else:
        time.sleep(60)

while True:
    main()