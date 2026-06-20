from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer

from core.system import get_stats

class SystemMonitor(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel()
        layout.addWidget(self.label)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)

        self.update_stats()

    def update_stats(self):

        s = get_stats()

        self.label.setText(
            f"CPU: {s['cpu']}%\n"
            f"CPU Freq: {int(s['cpu_freq'])} MHz\n\n"
            f"RAM: {s['ram']}%\n"
            f"Disk: {s['disk']}%\n"
            f"Free Disk: {s['disk_free']} GB\n\n"
            f"Refresh Rate: {s['refresh']} Hz\n"
            f"FPS: {s['fps']}\n"
            f"Uptime: {s['uptime']} sec"
        )