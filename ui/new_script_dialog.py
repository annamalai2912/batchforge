from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox)

class NewScriptDialog(QDialog):
    def __init__(self, existing_categories=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("New Script")
        self.resize(300, 140)
        
        layout = QVBoxLayout(self)
        
        # Name input
        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel("Script Name:"))
        self.name_input = QLineEdit()
        name_layout.addWidget(self.name_input)
        layout.addLayout(name_layout)
        
        # Category input
        cat_layout = QHBoxLayout()
        cat_layout.addWidget(QLabel("Category:"))
        self.category_input = QComboBox()
        self.category_input.setEditable(True)
        if existing_categories:
            self.category_input.addItems(sorted(list(existing_categories)))
        else:
            self.category_input.addItem("Uncategorized")
        cat_layout.addWidget(self.category_input)
        layout.addLayout(cat_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        self.btn_create = QPushButton("Create")
        self.btn_cancel = QPushButton("Cancel")
        button_layout.addStretch()
        button_layout.addWidget(self.btn_create)
        button_layout.addWidget(self.btn_cancel)
        layout.addLayout(button_layout)
        
        # Connections
        self.btn_create.clicked.connect(self.accept)
        self.btn_cancel.clicked.connect(self.reject)
        
    def get_script_name(self):
        return self.name_input.text().strip()
        
    def get_category(self):
        cat = self.category_input.currentText().strip()
        return cat if cat else "Uncategorized"
