import os
import sys
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QTreeWidget, QTreeWidgetItem,
                             QTextEdit, QPushButton, QLabel, QSplitter, QMessageBox, QWidget, QLineEdit)
from PyQt6.QtCore import Qt
from core.database import add_script
from ui.syntax_highlighter import BatchSyntaxHighlighter

class CollectionBrowserDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Batch Scripts Collection Browser")
        self.resize(800, 500)
        
        if getattr(sys, 'frozen', False):
            base_dir = sys._MEIPASS
        else:
            base_dir = os.path.dirname(os.path.dirname(__file__))
            
        self.scripts_dir = os.path.join(base_dir, "batchforge_scripts")
        self.available_scripts = {} # (filename, category) -> content
        
        self.init_ui()
        self.load_scripts()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # Left side: List of scripts
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0,0,0,0)
        
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search collection...")
        self.search_bar.textChanged.connect(self.on_search_text_changed)
        
        left_layout.addWidget(QLabel("Available Scripts:"))
        left_layout.addWidget(self.search_bar)
        
        self.script_tree = QTreeWidget()
        self.script_tree.setHeaderHidden(True)
        self.script_tree.itemSelectionChanged.connect(self.on_script_selected)
        left_layout.addWidget(self.script_tree)
        
        splitter.addWidget(left_widget)
        
        # Right side: Preview and Add button
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(0,0,0,0)
        
        right_layout.addWidget(QLabel("Description:"))
        self.description_box = QTextEdit()
        self.description_box.setReadOnly(True)
        self.description_box.setMaximumHeight(80)
        self.description_box.setStyleSheet("background-color: #2b2b2b; color: #a9b7c6; border: 1px solid #555;")
        right_layout.addWidget(self.description_box)
        
        right_layout.addWidget(QLabel("Preview:"))
        self.preview_editor = QTextEdit()
        self.preview_editor.setReadOnly(True)
        font = self.preview_editor.font()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.preview_editor.setFont(font)
        self.highlighter = BatchSyntaxHighlighter(self.preview_editor.document())
        right_layout.addWidget(self.preview_editor)
        
        self.btn_add = QPushButton("Add to Library")
        self.btn_add.setEnabled(False)
        self.btn_add.clicked.connect(self.on_add_clicked)
        right_layout.addWidget(self.btn_add)
        
        splitter.addWidget(right_widget)
        
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 2)
        
        layout.addWidget(splitter)
        
        # Bottom: Close button
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        self.btn_close = QPushButton("Close")
        self.btn_close.clicked.connect(self.accept)
        btn_layout.addWidget(self.btn_close)
        layout.addLayout(btn_layout)
        
    def load_scripts(self):
        if not os.path.exists(self.scripts_dir):
            QMessageBox.warning(self, "Error", f"Could not find scripts directory at {self.scripts_dir}")
            return
            
        self.script_tree.clear()
        
        for root, dirs, files in os.walk(self.scripts_dir):
            category = os.path.basename(root)
            if category == "batchforge_scripts":
                continue # Skip root dir files unless we want to put them in "Uncategorized"
                
            cat_item = None
            for filename in files:
                if filename.lower().endswith('.bat'):
                    if cat_item is None:
                        cat_item = QTreeWidgetItem([category])
                        self.script_tree.addTopLevelItem(cat_item)
                        
                    filepath = os.path.join(root, filename)
                    try:
                        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                            content = f.read()
                        
                        # Use tuple of (filename, category) as key in case filenames collide across categories
                        self.available_scripts[(filename, category)] = content
                        
                        script_item = QTreeWidgetItem([filename])
                        script_item.setData(0, Qt.ItemDataRole.UserRole, category) # Store category in data
                        cat_item.addChild(script_item)
                    except Exception as e:
                        print(f"Failed to load {filename}: {e}")
                        
        self.script_tree.expandAll()
        
    def on_search_text_changed(self, text):
        text = text.lower()
        for i in range(self.script_tree.topLevelItemCount()):
            cat_item = self.script_tree.topLevelItem(i)
            cat_match = text in cat_item.text(0).lower()
            
            child_match = False
            for j in range(cat_item.childCount()):
                script_item = cat_item.child(j)
                if text in script_item.text(0).lower() or cat_match:
                    script_item.setHidden(False)
                    child_match = True
                else:
                    script_item.setHidden(True)
                    
            if child_match or cat_match:
                cat_item.setHidden(False)
                if text:
                    cat_item.setExpanded(True)
            else:
                cat_item.setHidden(True)
                    
    def on_script_selected(self):
        selected_items = self.script_tree.selectedItems()
        if not selected_items:
            self.preview_editor.clear()
            self.description_box.clear()
            self.btn_add.setEnabled(False)
            return
            
        item = selected_items[0]
        if item.childCount() > 0:
            # It's a category header
            self.preview_editor.clear()
            self.description_box.clear()
            self.btn_add.setEnabled(False)
            return
            
        filename = item.text(0)
        category = item.data(0, Qt.ItemDataRole.UserRole)
        content = self.available_scripts.get((filename, category), "")
        self.preview_editor.setPlainText(content)
        
        # Extract description (lines starting with :: or REM)
        desc_lines = []
        for line in content.splitlines():
            line_stripped = line.strip()
            if line_stripped.startswith('::') or line_stripped.upper().startswith('REM '):
                # Clean up the prefix
                if line_stripped.startswith('::'):
                    desc_lines.append(line_stripped[2:].strip())
                else:
                    desc_lines.append(line_stripped[4:].strip())
            elif line_stripped and not line_stripped.startswith('@echo'):
                # Stop looking for description after first real command
                break
                
        if desc_lines:
            self.description_box.setPlainText(" ".join(desc_lines))
        else:
            self.description_box.setPlainText("No description provided.")
            
        self.btn_add.setEnabled(True)
        
    def on_add_clicked(self):
        selected_items = self.script_tree.selectedItems()
        if not selected_items:
            return
            
        item = selected_items[0]
        if item.childCount() > 0:
            return
            
        filename = item.text(0)
        category = item.data(0, Qt.ItemDataRole.UserRole)
        content = self.available_scripts.get((filename, category), "")
        
        add_script(filename, content, category)
        QMessageBox.information(self, "Success", f"'{filename}' has been added to your library under '{category}'.")
