import subprocess

def status():

    try:
        r = subprocess.run(
            ["systemctl", "is-active", "ssh"],
            capture_output=True,
            text=True
        )

        return "Running" if "active" in r.stdout else "Stopped"

    except:
        return "Unknown"

def start():
    subprocess.run(["sudo", "systemctl", "start", "ssh"])

def stop():
    subprocess.run(["sudo", "systemctl", "stop", "ssh"])

def restart():
    subprocess.run(["sudo", "systemctl", "restart", "ssh"])