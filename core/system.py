import psutil
import time
import subprocess
import re

_last_time = time.time()
_frames = 0
_fps = 0

def update_fps():
    global _last_time, _frames, _fps

    _frames += 1
    current = time.time()

    if current - _last_time >= 1:
        _fps = _frames
        _frames = 0
        _last_time = current

    return _fps

def get_refresh_rate():
    try:
        output = subprocess.check_output(["xrandr"]).decode()
        match = re.search(r'(\d+\.\d+)\*', output)
        if match:
            return float(match.group(1))
    except:
        pass

    return 0

def get_stats():
    disk = psutil.disk_usage('/')

    return {
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent,
        "disk": disk.percent,
        "disk_free": round(disk.free / (1024**3), 1),
        "fps": update_fps(),
        "refresh": get_refresh_rate(),
        "uptime": int(time.time() - psutil.boot_time()),
        "cpu_freq": psutil.cpu_freq().current if psutil.cpu_freq() else 0
    }