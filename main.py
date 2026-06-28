import sys
from PyQt6.QtWidgets import QApplication
from core.database import init_db
from ui.main_window import MainWindow


def main():
    # Initialize the database
    init_db()

    app = QApplication(sys.argv)

    # Initialize main window
    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
