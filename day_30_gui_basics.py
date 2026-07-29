import sys
from PySide6.QtWidgets import(
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QTextEdit
)
from PySide6.QtCore import Qt
class MediaInspectorWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #============================================================================================
        # 1. Window configuration 
        #============================================================================================
        # set the title string shown on the window title bar
        self.setWindowTitle("Pipeline Core - Media Inspector v1.0")
        # set initial window dimensions(width = 650 pixels, hight = 420 pixels )
        self.resize(650, 420)


        #==========================================================================================
        # Central widget & main layout setup
        #==========================================================================================
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        #==========================================================================
        
        #==========================================================================
        # Header ui section
        # visual banner label placed at the top of interface 
        #==========================================================================
        self.header_label = QLabel("📷Media asset pipeline GUI")
        self.header_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #1E293B;")
        main_layout.addWidget(self.header_label)
        #==========================================================================
                
        #==========================================================================
        # Path selection row
        # places the input box ans button side by side in a horizontal row  
        #==========================================================================
        input_layout = QHBoxLayout()
        self.path_input = QLineEdit()
        self.path_input.setPlaceholderText("Type folder path here.......")
        input_layout.addWidget(self.path_input)
        self.inspect_button = QPushButton("inspect directory")
        
        self.inspect_button.clicked.connect(self.handle_inspect_click)
        input_layout.addWidget(self.inspect_button)

        main_layout.addLayout(input_layout)

        #======================================================================================
        #log/ output text area 
        # multi line read only text area for displaying status logs and messages 
        #=======================================================================================
        self.output_display = QTextEdit()
        self.output_display.setReadOnly(True)
        self.output_display.setPlaceholderText("Execution logs and audit output will appear here...")
        main_layout.addWidget(self.output_display)

    #===============================================================================
    # event handler 
    #===================================================================================
    def handle_inspect_click(self):
        user_path = self.path_input.text().strip()

        if not user_path:
            self.output_display.append("⚠️[Warning]: Please enter a directory path first.")
            return
        self.output_display.append(f"🔍[Info]: Target selected: '{user_path}'")
        self.output_display.append("✅[Success]: GUI interface response successful")

def main():
    app = QApplication(sys.argv)

    window = MediaInspectorWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()