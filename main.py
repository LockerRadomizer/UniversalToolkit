#!/usr/bin/env python3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget
import sys

from ui.system_monitor import SystemMonitor
from ui.network_tools import NetworkTools
from ui.ssh_manager import SSHManager
from ui.file_tools import FileTools

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Universal Toolkit v0.3")

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tabs.addTab(SystemMonitor(), "System")
        self.tabs.addTab(NetworkTools(), "Network")
        self.tabs.addTab(SSHManager(), "SSH")
        self.tabs.addTab(FileTools(), "Files")

app = QApplication(sys.argv)
w = Main()
w.show()
sys.exit(app.exec_())
