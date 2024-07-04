from PySide6.QtGui import QFont
from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout


class DialogFormVerticalLayout(QDialog):

    def __init__(self, parent=None):
        super(DialogFormVerticalLayout, self).__init__(parent)
        self.setWindowTitle("Example PySide6 Dialog Form")
        # used fixed size for dialog (will use PyAutoGUI later on to scale to percent of device size)
        dialog_width = 512
        dialog_height = 384

        # set dialog width and height
        self.setFixedSize(dialog_width, dialog_height)

        # Create widgets
        self.edit = QLineEdit("")
        self.edit.setFixedSize(dialog_width * 0.9, dialog_height * 0.1)
        self.edit.setToolTip('Type your name here')

        button_font = QFont('Monospace')
        button_font.setBold(True)
        button_font.setPointSize(dialog_height * 0.05)
        # button_font.setStyleHint(QFont.StyleHint.Monospace)

        self.button = QPushButton("Show Greetings")
        self.button.setFont(button_font)
        self.button.setFixedSize(dialog_width * 0.9, dialog_height * 0.1)

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
