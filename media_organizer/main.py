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
    QFileDialog # allows to open window picker.
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📷Media Asset Manager.    email: asad.sajjad.codes@gmail.com") # tital of the tool 
        self.resize(650, 420)  # size for the window 

        # Main canvas setup 
        main_canvas = QWidget()
        self.setCentralWidget(main_canvas)

        # main layout (vertical top to bottom)
        main_layout = QVBoxLayout()
        main_canvas.setLayout(main_layout)

        # title label
        self.title_label = QLabel("Media Asset Manager")
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;") # style for the title label
        main_layout.addWidget(self.title_label)

        # input row (horizontal)
        input_layout = QHBoxLayout()
        main_layout.addLayout(input_layout) # add input layout inside the main layout
        
        self.path_box = QLineEdit() # add a text input box 
        self.path_box.setPlaceholderText("Click 'Browse...' to select the folder.")
        input_layout.addWidget(self.path_box)

        # adding buttons 
        # browse button
        self.browse_button = QPushButton("Browse Directory")
        self.browse_button.clicked.connect(self.folder_dialog)
        input_layout.addWidget(self.browse_button)
        # inspect button
        self.inspect_button = QPushButton("Run Audit")
        self.inspect_button.clicked.connect(self.run_Audit)
        input_layout.addWidget(self.inspect_button)
        # auto arrange button
        self.auto_arrange_button = QPushButton("Run Manager")
        self.auto_arrange_button.clicked.connect(self.run_manager)
        input_layout.addWidget(self.auto_arrange_button)

        # screen to show output
        self.display_screen = QTextEdit()
        self.display_screen.setReadOnly(True) # makes the output read only
        main_layout.addWidget(self.display_screen)





    def folder_dialog(self):
        selected_folder = QFileDialog.getExistingDirectory( # opens the standard OS folder
            self,
            "Select Asset Directory",
            "" # starts at default directory
        )
        # if the user selected a folder 
        if selected_folder:
            self.path_box.setText(selected_folder) # write the selected path in path box 
            self.display_screen.append(f"📁Folder selected: '{selected_folder}'")

        
    def run_Audit(self):
        folder = self.path_box.text()

        if not folder:
            self.display_screen.append("⚠️ Warning: No folder selected! Click 'Browse...' first .")
        else:
            self.display_screen.append(f"🚀 Starting audit on: '{folder}'")
    def run_manager(self):
        folder = self.path_box.text()

        if not folder:
            self.display_screen.append("⚠️ Warning: No folder selected! Click 'Browse...' first .")
        else:
            self.display_screen.append(f"🚀 Starting auto organizing on: '{folder}'")
        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())