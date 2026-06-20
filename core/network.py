import socket
import subprocess
import ipaddress
from concurrent.futures import ThreadPoolExecutor

def get_local_ip():

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "Unknown"

def ping(host):

    return subprocess.run(
        ["ping", "-c", "1", "-W", "1", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    ).returncode == 0

def scan_network():

    ip = get_local_ip()

    net = ipaddress.IPv4Network(
        ip + "/24",
        strict=False
    )

    alive = []

    def check(h):
        if ping(str(h)):
            alive.append(str(h))

    with ThreadPoolExecutor(max_workers=50) as ex:
        ex.map(check, net.hosts())

    return sorted(alive)