from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, 
                             QLabel, QComboBox, QTimeEdit, QPushButton, QMessageBox)
from PyQt6.QtCore import QTime

class ScheduleDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Schedule Script")
        self.resize(300, 150)
        
        layout = QVBoxLayout(self)
        
        # Trigger type
        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("Trigger Type:"))
        self.type_combo = QComboBox()
        self.type_combo.addItems(["ONCE", "DAILY", "WEEKLY", "MONTHLY", "ONLOGON", "ONIDLE"])
        self.type_combo.currentTextChanged.connect(self.on_type_changed)
        type_layout.addWidget(self.type_combo)
        layout.addLayout(type_layout)
        
        # Trigger time
        self.time_layout = QHBoxLayout()
        self.time_layout.addWidget(QLabel("Trigger Time:"))
        self.time_input = QTimeEdit()
        self.time_input.setDisplayFormat("HH:mm")
        self.time_input.setTime(QTime.currentTime())
        self.time_layout.addWidget(self.time_input)
        layout.addLayout(self.time_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        self.btn_schedule = QPushButton("Schedule")
        self.btn_cancel = QPushButton("Cancel")
        button_layout.addStretch()
        button_layout.addWidget(self.btn_schedule)
        button_layout.addWidget(self.btn_cancel)
        layout.addLayout(button_layout)
        
        # Connections
        self.btn_schedule.clicked.connect(self.accept)
        self.btn_cancel.clicked.connect(self.reject)
        
    def on_type_changed(self, text):
        if text in ["ONLOGON", "ONIDLE"]:
            self.time_input.setEnabled(False)
        else:
            self.time_input.setEnabled(True)
            
    def get_schedule_details(self):
        trigger_type = self.type_combo.currentText()
        trigger_time = self.time_input.time().toString("HH:mm")
        return trigger_type, trigger_time
