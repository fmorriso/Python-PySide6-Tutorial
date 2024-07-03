from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout


class DialogForm(QDialog):

    def __init__(self, parent=None):
        super(DialogForm, self).__init__(parent)
        self.setWindowTitle("Example PySide6 Dialog Form")
        # Create widgets
        self.edit = QLineEdit("Write my name here..")
        self.button = QPushButton("Show Greetings")
        # Create layout and add widgets
        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal (i.g., event listener) to greetings slot
        self.button.clicked.connect(self.greetings)

# Greets the user
    def greetings(self):
        print(f"Hello {self.edit.text()}")
