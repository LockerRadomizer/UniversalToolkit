from PyQt5.QtWidgets import QWidget,QVBoxLayout,QPushButton,QTextEdit

from core.files import (
    clean_temp,
    large_files
)

class FileTools(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.out = QTextEdit()

        b1 = QPushButton("Clean Temp")

        b2 = QPushButton("Find Large Files")

        b1.clicked.connect(self.clean)

        b2.clicked.connect(self.find)

        layout.addWidget(b1)
        layout.addWidget(b2)
        layout.addWidget(self.out)

    def clean(self):

        removed = clean_temp()

        self.out.setText(
            f"Removed {removed} temp files"
        )

    def find(self):

        files = large_files()

        text = ""

        for path,size in files:

            text += (
                f"{size} MB\n"
                f"{path}\n\n"
            )

        self.out.setText(text)