# Universal Toolkit v0.3

Universal Toolkit is a Linux/Chromebook (Crostini) system utility suite built with Python and PyQt5. It provides real-time system monitoring, network tools, SSH management, and file utilities — plus a GitHub-based auto-update system.

---

## 🚀 Features

### 🖥 System Monitor

* Live CPU usage
* RAM usage
* Disk usage
* CPU frequency
* System uptime
* FPS counter (UI refresh performance)
* Monitor refresh rate detection

### 🌐 Network Tools

* Local IP detection
* LAN device scanner
* Active host discovery

### 🔐 SSH Manager

* SSH service status
* Start / Stop / Restart SSH
* Live status updates

### 📁 File Tools

* Clean temporary files
* Large file finder
* File size viewer

### 🔄 Auto Updater (GitHub)

* Checks latest GitHub release
* Detects new versions
* Downloads update ZIP
* Ready for auto-install upgrade system (v0.4+)

---

## 📦 Installation

### Clone repository

```bash
git clone https://github.com/LockerRadomizer/UniversalToolkit.git
cd UniversalToolkit
```

### Install dependencies

```bash
pip install PyQt5 psutil requests
```

---

## ▶ Run

```bash
python3 main.py
```

---

## 🔄 Updating

Universal Toolkit uses GitHub Releases for updates.

### How it works:

* App checks GitHub API for latest version
* If a newer version exists:

  * User can download update
  * Future versions will support full auto-install

---

## 🧠 GitHub Releases

Create a new release:

```bash
git tag v0.3
git push origin v0.3
```

Then go to:
https://github.com/LockerRadomizer/UniversalToolkit/releases

Upload your build ZIP or release files.

---

## ⚙ Dependencies

* Python 3.9+
* PyQt5
* psutil
* requests

Install all:

```bash
pip install PyQt5 psutil requests
```

---

## 🧪 Supported Platforms

* ChromeOS (Linux / Crostini)
* Debian Linux
* Ubuntu
* Other Linux distros

---

## 🧭 Roadmap

### v0.4 (Next Update)

* Full auto-installer (replace files automatically)
* Progress bar UI
* Restart-after-update system
* File Explorer module
* Dark mode UI
* System tray integration

### v0.5

* Process manager
* Network port scanner
* Performance graphs
* Plugin system

### v1.0

* Fully modular system toolkit
* Stable auto-updater
* Cross-platform builds

---

## 👨‍💻 Author

Created by LockerRadomizer/KitsuVibe/PowerfulElixir
SocialMedia: [My Twitch Channel KitsuVibe](https://www.twitch.tv/KitsuVibe)
[My YouTube Channel](https://www.youtube.com/@KitsuVibes)
Universal Toolkit v0.3
