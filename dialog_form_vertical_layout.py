from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout


class DialogFormVerticalLayout(QDialog):

    def __init__(self, parent=None):
        super(DialogFormVerticalLayout, self).__init__(parent)
        self.setWindowTitle("Example PySide6 Dialog Form")
        # set width and height
        self.setFixedSize(512, 384)
        # Create widgets
        self.edit = QLineEdit("Write my name here..")
        self.button = QPushButton("Show Greetings")
        # Create vertical layout and add widgets to it
        self.vertical_layout = QVBoxLayout(self)
        self.vertical_layout.addWidget(self.edit)
        self.vertical_layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(self.vertical_layout)
        # Add button signal (i.g., event listener) to greetings slot
        self.button.clicked.connect(self.greetings)

# Greets the user
    def greetings(self):
        print(f"Hello {self.edit.text()}")
