from PyQt5.QtWidgets import QWidget,QVBoxLayout,QPushButton,QTextEdit

from core.network import (
    scan_network,
    get_local_ip
)

class NetworkTools(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.out = QTextEdit()

        btn = QPushButton("Scan Network")

        btn.clicked.connect(self.run)

        layout.addWidget(self.out)
        layout.addWidget(btn)

    def run(self):

        devices = scan_network()

        text = f"Local IP: {get_local_ip()}\n\n"

        text += "\n".join(devices)

        self.out.setText(text)