from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QStackedWidget, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class WelcomeWizardDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Welcome to BatchForge")
        self.setFixedSize(600, 400)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        # Header
        header = QLabel("BatchForge Interactive Tour")
        font = header.font()
        font.setPointSize(16)
        font.setBold(True)
        header.setFont(font)
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(header)

        # Stacked Widget for pages
        self.stack = QStackedWidget()
        self.stack.addWidget(self.create_page(
            "1. Introduction",
            "Welcome to BatchForge, the Ultimate Windows Automation Manager!\n\nThis brief tour will guide you through the core features of the application, so you can start organizing, editing, and executing your Batch Scripts with confidence."
        ))
        self.stack.addWidget(self.create_page(
            "2. Script Library",
            "On the left panel, you'll find the Script Library.\n\n- It automatically categorizes your scripts into a tree view.\n- You can use the search bar to instantly find any script.\n- Use the 'Browse Collection' button to discover over 30 built-in safe and practical automation scripts!"
        ))
        self.stack.addWidget(self.create_page(
            "3. Code Editor",
            "The top right panel features a built-in code editor.\n\n- It includes custom CMD/Batch syntax highlighting.\n- You can write and edit scripts safely on the fly without leaving the application.\n- Don't forget to hit 'Save'!"
        ))
        self.stack.addWidget(self.create_page(
            "4. Safe Execution Engine",
            "The bottom right panel is the Output Console.\n\n- Click 'Run' to execute a script asynchronously (it won't freeze the app!).\n- The output streams directly into the console in real-time.\n- If a script goes rogue, just click 'Stop' to safely terminate the process tree."
        ))
        self.stack.addWidget(self.create_page(
            "5. Ready to Automate",
            "You are all set!\n\nIf you want to learn more about writing Batch Scripts, check out the 'Help' -> 'Learn Batch Scripting' menu for a bundled PDF guide and useful links.\n\nHappy Automating!"
        ))
        
        layout.addWidget(self.stack)

        # Navigation Buttons
        nav_layout = QHBoxLayout()
        self.btn_prev = QPushButton("Previous")
        self.btn_next = QPushButton("Next")
        
        self.btn_prev.clicked.connect(self.prev_page)
        self.btn_next.clicked.connect(self.next_page)
        
        self.btn_prev.setEnabled(False)
        
        nav_layout.addWidget(self.btn_prev)
        nav_layout.addStretch()
        nav_layout.addWidget(self.btn_next)
        
        layout.addLayout(nav_layout)

    def create_page(self, title, content):
        page = QWidget()
        page_layout = QVBoxLayout(page)
        
        title_label = QLabel(title)
        font = title_label.font()
        font.setPointSize(14)
        title_label.setFont(font)
        
        content_label = QLabel(content)
        content_label.setWordWrap(True)
        content_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        content_label.setStyleSheet("font-size: 14px; margin-top: 20px; line-height: 1.5;")
        
        page_layout.addWidget(title_label)
        page_layout.addWidget(content_label)
        page_layout.addStretch()
        return page

    def prev_page(self):
        current = self.stack.currentIndex()
        if current > 0:
            self.stack.setCurrentIndex(current - 1)
        self.update_buttons()

    def next_page(self):
        current = self.stack.currentIndex()
        if current < self.stack.count() - 1:
            self.stack.setCurrentIndex(current + 1)
        else:
            self.accept()
        self.update_buttons()

    def update_buttons(self):
        current = self.stack.currentIndex()
        self.btn_prev.setEnabled(current > 0)
        
        if current == self.stack.count() - 1:
            self.btn_next.setText("Finish")
        else:
            self.btn_next.setText("Next")
