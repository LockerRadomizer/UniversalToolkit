from PyQt5.QtWidgets import QWidget,QVBoxLayout,QPushButton,QTextEdit
from PyQt5.QtCore import QTimer

from core.ssh import (
    status,
    start,
    stop,
    restart
)

class SSHManager(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.out = QTextEdit()

        b1 = QPushButton("Start")
        b2 = QPushButton("Stop")
        b3 = QPushButton("Restart")

        b1.clicked.connect(start)
        b2.clicked.connect(stop)
        b3.clicked.connect(restart)

        layout.addWidget(b1)
        layout.addWidget(b2)
        layout.addWidget(b3)
        layout.addWidget(self.out)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_status)
        self.timer.start(2000)

        self.update_status()

    def update_status(self):

        self.out.setText(
            f"SSH Service Status\n\n{status()}"
        )