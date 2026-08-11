import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow, 
    QWidget, 
    QVBoxLayout,
    QHBoxLayout, 
    QLabel, 
    QPushButton, 
    QLineEdit, 
    QTextEdit, 
    QFileDialog,
    QProgressBar
)
from scanner import path_test
from logger import log_info, log_warning, log_error, gui_handler
from organizer import organize_folder

# Styling configuration
DARK_THEME = """
QMainWindow {
    background-color: #1E1E2E;
}
QLabel {
    color: #CDD6F4;
    font-weight: bold;
}
QLineEdit {
    background-color: #313244;
    color: #F5E0DC;
    border: 1px solid #45475A;
    border-radius: 5px;
    padding: 6px;
}
QPushButton {
    background-color: #89B4FA;
    color: #11111B;
    border: none;
    border-radius: 5px;
    padding: 8px 12px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #B4BEFE;
}
QTextEdit {
    background-color: #11111B;
    color: #A6E3A1;
    border: 1px solid #45475A;
    border-radius: 5px;
    font-family: Consolas, monospace;
}
QProgressBar {
    border: 1px solid #45475A;
    border-radius: 5px;
    text-align: center;
    color: #FFFFFF;
    background-color: #313244;
    font-weight: bold;
}
QProgressBar::chunk {
    background-color: #89B4FA;
    border-radius: 4px;
}
"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📷 Media Asset Manager | asad.sajjad.codes@gmail.com")
        self.resize(700, 480)

        # Canvas layout setup
        main_canvas = QWidget()
        self.setCentralWidget(main_canvas)

        main_layout = QVBoxLayout()
        main_canvas.setLayout(main_layout)

        # Title Header
        self.title_label = QLabel("⚡ Pro Media Asset Manager")
        self.title_label.setStyleSheet("font-size: 22px; color: #89B4FA;")
        main_layout.addWidget(self.title_label)

        # Directory selection controls
        input_layout = QHBoxLayout()
        main_layout.addLayout(input_layout)
        
        self.path_box = QLineEdit()
        self.path_box.setPlaceholderText("Click 'Browse Directory' to pick a folder...")
        input_layout.addWidget(self.path_box)

        self.browse_button = QPushButton("Browse Directory")
        self.browse_button.clicked.connect(self.folder_dialog)
        input_layout.addWidget(self.browse_button)

        # Processing trigger buttons
        button_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)

        self.inspect_button = QPushButton("Run Audit")
        self.inspect_button.clicked.connect(self.run_audit)
        button_layout.addWidget(self.inspect_button)

        self.auto_arrange_button = QPushButton("Run Organizer")
        self.auto_arrange_button.clicked.connect(self.run_organizer)
        button_layout.addWidget(self.auto_arrange_button)

        # Live Progress Display
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        main_layout.addWidget(self.progress_bar)

        # Log Text Area
        self.display_screen = QTextEdit()
        self.display_screen.setReadOnly(True)
        main_layout.addWidget(self.display_screen)

        # Connect shared GUI handler signal to display_screen writer method
        gui_handler.log_message.connect(self.show_message)
        log_info("GUI triple-logging system initialized successfully.")

    def show_message(self, message: str) -> None:
        """Appends formatted messages directly to the UI screen."""
        self.display_screen.append(message)

    def folder_dialog(self) -> None:
        """Opens folder picker dialog and sets selected directory path."""
        selected_folder = QFileDialog.getExistingDirectory(self, "Select Asset Directory", "")
        if selected_folder:
            self.path_box.setText(selected_folder)
            log_info(f"📁 Folder selected: '{selected_folder}'")

    def run_audit(self) -> None:
        """Scans folder items and tracks status via live logs and progress."""
        folder = self.path_box.text().strip()
        if not folder:
            log_warning("⚠️ Warning: No folder selected! Click 'Browse Directory' first.")
            return

        log_info(f"🔍 Starting audit on: '{folder}'...")
        self.progress_bar.setValue(0)

        data = path_test(folder)

        if isinstance(data, str):
            log_warning(data)
            return

        total_files = len(data)
        if total_files == 0:
            self.progress_bar.setValue(100)
            return

        for index, file_msg in enumerate(data, start=1):
            progress = int((index / total_files) * 100)
            self.progress_bar.setValue(progress)
            QApplication.processEvents()

        log_info("✅ Audit complete!")

    def run_organizer(self) -> None:
        """Executes auto-organizer logic and updates GUI components."""
        folder = self.path_box.text().strip()
        if not folder:
            log_warning("⚠️ Warning: No folder selected! Click 'Browse Directory' first.")
            return

        log_info(f"🚀 Starting auto organizing on: '{folder}'...")
        self.progress_bar.setValue(10)
        QApplication.processEvents()

        result = organize_folder(folder)

        self.progress_bar.setValue(80)
        QApplication.processEvents()

        if "error" in result:
            log_error(result["error"])
        elif "info" in result:
            log_info(result["info"])
        else:
            for category, count in result["categories"].items():
                log_info(f"📁 {category}: {count} file(s) moved")
            if result["skipped"] > 0:
                log_warning(f"⚠️ Skipped {result['skipped']} file(s) due to destination conflicts.")

        self.progress_bar.setValue(100)
        log_info("✅ Auto-Organizer process completed.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(DARK_THEME)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())