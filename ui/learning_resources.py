import sys
import os
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QDesktopServices

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class LearningDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Learn Batch Scripting")
        self.setFixedSize(400, 300)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        title = QLabel("Learning Resources")
        font = title.font()
        font.setPointSize(14)
        font.setBold(True)
        title.setFont(font)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        desc = QLabel("Want to learn how to write your own Batch Scripts? We've compiled some resources to help you get started.")
        desc.setWordWrap(True)
        layout.addWidget(desc)
        layout.addSpacing(10)

        # PDF Button
        btn_pdf = QPushButton("Open Built-in Beginner's Guide (PDF)")
        btn_pdf.setStyleSheet("padding: 10px; font-weight: bold;")
        btn_pdf.clicked.connect(self.open_pdf)
        layout.addWidget(btn_pdf)

        layout.addSpacing(10)
        layout.addWidget(QLabel("<b>External Resources:</b>"))

        # Links
        btn_ss64 = QPushButton("SS64 - Command Line Reference")
        btn_ss64.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://ss64.com/nt/")))
        layout.addWidget(btn_ss64)

        btn_ms = QPushButton("Microsoft Docs - Windows Commands")
        btn_ms.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands")))
        layout.addWidget(btn_ms)

        layout.addStretch()
        
        btn_close = QPushButton("Close")
        btn_close.clicked.connect(self.accept)
        layout.addWidget(btn_close)

    def open_pdf(self):
        pdf_path = resource_path("Batch_Scripting_Guide.pdf")
        if os.path.exists(pdf_path):
            QDesktopServices.openUrl(QUrl.fromLocalFile(pdf_path))
        else:
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Error", "Could not find the bundled PDF guide.")
