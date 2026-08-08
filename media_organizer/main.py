import sys
import time
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
from logger import log_info, log_warning, log_error
from organizer import organize_folder

# ==============================================================================
# 1. THE DARK MODE PAINT JOB (QSS)
# ==============================================================================
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

        # Main canvas layout
        main_canvas = QWidget()
        self.setCentralWidget(main_canvas)

        main_layout = QVBoxLayout()
        main_canvas.setLayout(main_layout)

        # Title Header
        self.title_label = QLabel("⚡ Pro Media Asset Manager")
        self.title_label.setStyleSheet("font-size: 22px; color: #89B4FA;")
        main_layout.addWidget(self.title_label)

        # Folder Input Row
        input_layout = QHBoxLayout()
        main_layout.addLayout(input_layout)
        
        self.path_box = QLineEdit() 
        self.path_box.setPlaceholderText("Click 'Browse Directory' to pick a folder...")
        input_layout.addWidget(self.path_box)

        self.browse_button = QPushButton("Browse Directory")
        self.browse_button.clicked.connect(self.folder_dialog)
        input_layout.addWidget(self.browse_button)

        # Action Buttons Row
        button_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)

        self.inspect_button = QPushButton("Run Audit")
        self.inspect_button.clicked.connect(self.run_audit)
        button_layout.addWidget(self.inspect_button)

        self.auto_arrange_button = QPushButton("Run Organizer")
        self.auto_arrange_button.clicked.connect(self.run_organizer)
        button_layout.addWidget(self.auto_arrange_button)

        # Live Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        main_layout.addWidget(self.progress_bar)

        # Output Log Screen
        self.display_screen = QTextEdit()
        self.display_screen.setReadOnly(True)
        main_layout.addWidget(self.display_screen)



    # Centralized GUI messaging helper.
    # All user-facing messages pass through this method,
    # making future logging integration much easier.
    
    def show_message(self, message: str) -> None: # takes a string and returns None
        self.display_screen.append(message)
        


    def folder_dialog(self):
        selected_folder = QFileDialog.getExistingDirectory(self, "Select Asset Directory", "")
        if selected_folder:
            self.path_box.setText(selected_folder)
            self.show_message(f"📁 Folder selected: '{selected_folder}'")
            log_info(f"📁 Folder selected: '{selected_folder}'")

    def run_audit(self):
        folder = self.path_box.text().strip()
        if not folder:
            self.show_message("⚠️ Warning: No folder selected! Click 'Browse Directory' first.")
            log_warning("⚠️ Warning: No folder selected! Click 'Browse Directory' first.")
            return

        self.show_message(f"🔍 Starting audit on: '{folder}'...")
        log_info(f"🔍 Starting audit on: '{folder}'...")
        self.progress_bar.setValue(0) # Reset progress bar

        data = path_test(folder)

        # If path_test returned an error message string instead of a list
        if isinstance(data, str):
            self.show_message(data)
            return

        total_files = len(data)
        if total_files == 0:
            self.progress_bar.setValue(100)
            return

        # Loop through files and dynamically update progress
        for index, file in enumerate(data, start=1):
            self.show_message(file)

            # Calculate completion percentage
            progress = int((index / total_files) * 100)
            self.progress_bar.setValue(progress)

            # Force PySide to refresh the UI screen live
            QApplication.processEvents()

        self.show_message("✅ Audit complete!")
        log_info("✅ Audit complete!")
            
    def run_organizer(self):
        folder = self.path_box.text().strip()
        if not folder:
            self.show_message("⚠️ Warning: No folder selected! Click 'Browse Directory' first.")
            log_warning("⚠️ Warning: No folder selected! Click 'Browse Directory' first.")
            return

        self.show_message(f"🚀 Starting auto organizing on: '{folder}'...")
        log_info(f"🚀 Starting auto organizing on: '{folder}'...")
        self.progress_bar.setValue(10)
        QApplication.processEvents()

        # Execute file organization logic 
        result = organize_folder(folder)

        self.progress_bar.setValue(80)
        QApplication.processEvents()

        if "error" in result:
            self.show_message(f"❌error: {result['error']}")
        elif "info" in result:
            self.show_message(f"ℹ️ {result['info']}")
        else:
            self.show_message(f"✅Organization completed! moved {result['moved']} file(s).")
            for category, count in result["categories"].items():
                self.show_message(f"📁{category} : {count} file(s)")
                if result["skipped"] > 0:
                    self.show_message(f" ⚠️Skipped {result['skipped']} duplicate file(s)")
        self.progress_bar.setValue(100)
        log_info(f"✅Auto-Organizer process completed.")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(DARK_THEME)  # Apply global styling
    window = MainWindow()
    window.show()
    sys.exit(app.exec())