from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QPushButton,
                             QLabel, QMessageBox, QLineEdit)
from PyQt6.QtCore import Qt, pyqtSlot, QEvent
from ui.syntax_highlighter import BatchSyntaxHighlighter
from core.execution import ScriptExecutionThread
from core.database import get_all_scripts, add_script, get_script, update_script, delete_script, delete_all_scripts
from ui.new_script_dialog import NewScriptDialog
from ui.collection_browser import CollectionBrowserDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BatchForge")
        self.resize(1000, 700)
        self.setAcceptDrops(True)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Splitter for left and right panels
        splitter = QSplitter(Qt.Orientation.Horizontal)

        # Left Panel (Library)
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(0, 0, 0, 0)

        self.script_list = QTreeWidget()
        self.script_list.setHeaderHidden(True)
        
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search scripts...")
        
        left_layout.addWidget(QLabel("Script Library"))
        left_layout.addWidget(self.search_bar)
        left_layout.addWidget(self.script_list)

        button_layout = QHBoxLayout()
        self.btn_new = QPushButton("New Script")
        self.btn_browse = QPushButton("Browse Collection")
        self.btn_import = QPushButton("Import")
        self.btn_delete = QPushButton("Delete")
        self.btn_delete_all = QPushButton("Delete All")
        button_layout.addWidget(self.btn_new)
        button_layout.addWidget(self.btn_browse)
        button_layout.addWidget(self.btn_import)
        button_layout.addWidget(self.btn_delete)
        button_layout.addWidget(self.btn_delete_all)
        left_layout.addLayout(button_layout)

        splitter.addWidget(left_panel)

        # Right Panel (Editor and Output)
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(0, 0, 0, 0)

        right_splitter = QSplitter(Qt.Orientation.Vertical)

        # Editor Section
        editor_widget = QWidget()
        editor_layout = QVBoxLayout(editor_widget)
        editor_layout.setContentsMargins(0, 0, 0, 0)

        editor_layout.addWidget(QLabel("Editor"))
        self.editor = QTextEdit()
        # Set mono font for editor
        font = self.editor.font()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.editor.setFont(font)

        # Apply syntax highlighting
        self.highlighter = BatchSyntaxHighlighter(self.editor.document())

        editor_layout.addWidget(self.editor)

        editor_actions = QHBoxLayout()
        self.btn_save = QPushButton("Save")
        self.btn_run = QPushButton("Run")
        self.btn_stop = QPushButton("Stop")
        self.btn_stop.setEnabled(False)
        self.btn_schedule = QPushButton("Schedule")
        editor_actions.addWidget(self.btn_save)
        editor_actions.addWidget(self.btn_run)
        editor_actions.addWidget(self.btn_stop)
        editor_actions.addWidget(self.btn_schedule)
        editor_actions.addStretch()
        editor_layout.addLayout(editor_actions)

        right_splitter.addWidget(editor_widget)

        # Output Section
        output_widget = QWidget()
        output_layout = QVBoxLayout(output_widget)
        output_layout.setContentsMargins(0, 0, 0, 0)

        output_layout.addWidget(QLabel("Output"))
        self.output_console = QTextEdit()
        self.output_console.setReadOnly(True)
        self.output_console.setStyleSheet(
            "background-color: #1e1e1e; color: #d4d4d4;")
        self.output_console.setFont(font)
        output_layout.addWidget(self.output_console)

        right_splitter.addWidget(output_widget)

        # Add to main splitter
        right_layout.addWidget(right_splitter)
        splitter.addWidget(right_panel)

        # Set stretch factor so editor takes more space
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 3)

        main_layout.addWidget(splitter)

        # Connect signals
        self.search_bar.textChanged.connect(self.on_search_text_changed)
        self.btn_new.clicked.connect(self.on_new_script)
        self.btn_browse.clicked.connect(self.on_browse_collection)
        self.btn_import.clicked.connect(self.on_import_script)
        self.btn_delete.clicked.connect(self.on_delete_script)
        self.btn_delete_all.clicked.connect(self.on_delete_all_scripts)
        self.btn_run.clicked.connect(self.on_run_script)
        self.btn_stop.clicked.connect(self.on_stop_script)
        self.btn_schedule.clicked.connect(self.on_schedule_script)
        self.btn_save.clicked.connect(self.on_save_script)
        self.script_list.itemClicked.connect(self.on_script_selected)

        self.execution_thread = None
        self.current_script_id = None
        
        # Disable drop on child widgets so events bubble up to MainWindow
        self.editor.setAcceptDrops(False)
        self.editor.viewport().setAcceptDrops(False)
        self.script_list.setAcceptDrops(False)
        self.script_list.viewport().setAcceptDrops(False)
        
        self.load_scripts_to_list()
        
    def load_scripts_to_list(self):
        self.script_list.clear()
        scripts = get_all_scripts()
        
        categories = {}
        for script_id, name, category in scripts:
            if category not in categories:
                cat_item = QTreeWidgetItem([category])
                categories[category] = cat_item
                self.script_list.addTopLevelItem(cat_item)
                
            script_item = QTreeWidgetItem([name])
            script_item.setData(0, Qt.ItemDataRole.UserRole, script_id)
            categories[category].addChild(script_item)
            
        self.script_list.expandAll()
            
    def on_search_text_changed(self, text):
        text = text.lower()
        for i in range(self.script_list.topLevelItemCount()):
            cat_item = self.script_list.topLevelItem(i)
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
            
    def on_script_selected(self, item, column=0):
        script_id = item.data(0, Qt.ItemDataRole.UserRole)
        script = get_script(script_id)
        if script:
            self.current_script_id = script_id
            self.editor.setPlainText(script[1])

    def on_save_script(self):
        if self.current_script_id is None:
            QMessageBox.warning(self, "Warning", "No script selected to save.")
            return
        content = self.editor.toPlainText()
        update_script(self.current_script_id, content)
        self.output_console.append("Script saved successfully.")
        
    def on_delete_script(self):
        item = self.script_list.currentItem()
        if not item:
            return
        script_id = item.data(0, Qt.ItemDataRole.UserRole)
        if not script_id:
            QMessageBox.warning(self, "Warning", "Please select a script to delete, not a category.")
            return
            
        reply = QMessageBox.question(self, 'Confirm Delete', 
                                     f"Are you sure you want to delete '{item.text(0)}'?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            delete_script(script_id)
            if self.current_script_id == script_id:
                self.current_script_id = None
                self.editor.clear()
            self.load_scripts_to_list()

    def on_delete_all_scripts(self):
        reply = QMessageBox.question(self, 'Confirm Delete All', 
                                     "Are you sure you want to delete ALL scripts? This action cannot be undone.",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            delete_all_scripts()
            self.current_script_id = None
            self.editor.clear()
            self.load_scripts_to_list()
            self.output_console.append("All scripts have been deleted.")

    def on_new_script(self):
        existing_categories = set()
        for i in range(self.script_list.topLevelItemCount()):
            existing_categories.add(self.script_list.topLevelItem(i).text(0))
            
        dialog = NewScriptDialog(existing_categories, self)
        if dialog.exec():
            name = dialog.get_script_name()
            category = dialog.get_category()
            if not name:
                QMessageBox.warning(self, "Warning", "Script name cannot be empty.")
                return
            
            # Default empty script content
            content = "@echo off\n:: Write your script here\n"
            script_id = add_script(name, content, category)
            self.load_scripts_to_list()
            
            # Select the newly created script
            for i in range(self.script_list.topLevelItemCount()):
                cat_item = self.script_list.topLevelItem(i)
                for j in range(cat_item.childCount()):
                    item = cat_item.child(j)
                    if item.data(0, Qt.ItemDataRole.UserRole) == script_id:
                        self.script_list.setCurrentItem(item)
                        self.on_script_selected(item, 0)
                        return

    def on_browse_collection(self):
        dialog = CollectionBrowserDialog(self)
        dialog.exec()
        self.load_scripts_to_list()

    def on_import_script(self):
        from PyQt6.QtWidgets import QFileDialog
        import os
        
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "Import Scripts",
            "",
            "Batch Scripts (*.bat *.cmd);;Text Files (*.txt);;All Files (*)"
        )
        
        if not file_paths:
            return
            
        imported_count = 0
        for file_path in file_paths:
            try:
                name = os.path.basename(file_path)
                with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                    content = f.read()
                
                add_script(name, content, "Imported")
                imported_count += 1
            except Exception as e:
                QMessageBox.warning(self, "Import Error", f"Failed to import {file_path}:\n{str(e)}")
                
        if imported_count > 0:
            self.load_scripts_to_list()
            self.output_console.append(f"Imported {imported_count} script(s) via file browser.")

    def on_schedule_script(self):
        QMessageBox.information(
            self, "Schedule", "Scheduling interface would open here.")

    def on_run_script(self):
        script_content = self.editor.toPlainText()
        if not script_content.strip():
            QMessageBox.warning(self, "Warning", "Cannot run an empty script.")
            return

        self.output_console.clear()
        self.output_console.append("Starting execution...\n" + "-" * 40)

        self.execution_thread = ScriptExecutionThread(script_content)
        self.execution_thread.output_signal.connect(self.on_execution_output)
        self.execution_thread.finished_signal.connect(
            self.on_execution_finished)
        self.execution_thread.start()

        self.btn_run.setEnabled(False)
        self.btn_run.setText("Running...")
        self.btn_stop.setEnabled(True)

    def on_stop_script(self):
        if self.execution_thread and self.execution_thread.isRunning():
            self.execution_thread.stop()
            self.output_console.append("Stopping execution...")
            self.btn_stop.setEnabled(False)

    @pyqtSlot(str)
    def on_execution_output(self, line):
        self.output_console.append(line)

    @pyqtSlot(int)
    def on_execution_finished(self, returncode):
        self.output_console.append("-" * 40)
        self.output_console.append(
            f"Execution finished with return code: {returncode}")
        self.btn_run.setEnabled(True)
        self.btn_run.setText("Run")
        self.btn_stop.setEnabled(False)



    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            # Check if at least one URL is a supported script file
            if any(url.toLocalFile().lower().endswith(('.bat', '.cmd', '.txt')) for url in urls):
                event.acceptProposedAction()
                return
        event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if any(url.toLocalFile().lower().endswith(('.bat', '.cmd', '.txt')) for url in urls):
                event.acceptProposedAction()
                return
        event.ignore()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        imported_count = 0
        import os
        
        for url in urls:
            file_path = url.toLocalFile()
            if file_path.lower().endswith(('.bat', '.cmd', '.txt')):
                try:
                    name = os.path.basename(file_path)
                    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                        content = f.read()
                    
                    add_script(name, content, "Imported")
                    imported_count += 1
                except Exception as e:
                    QMessageBox.warning(self, "Import Error", f"Failed to import {file_path}:\n{str(e)}")
                    
        if imported_count > 0:
            self.load_scripts_to_list()
            self.output_console.append(f"Imported {imported_count} script(s) via drag-and-drop.")
            
        event.acceptProposedAction()
