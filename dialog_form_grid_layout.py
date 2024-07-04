from PySide6.QtCore import QSize
from PySide6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QHBoxLayout


class DialogFormGridLayout(QDialog):

    def __init__(self, parent=None):
        super(DialogFormGridLayout, self).__init__(parent)

        self.setWindowTitle("Example PySide6 Dialog Form with grid layout")
        # used fixed size for dialog (will use PyAutoGUI later on to scale to percent of device size)
        dialog_width = 512
        dialog_height = 384

        # set dialog width and height
        self.setFixedSize(QSize(dialog_width, dialog_height))

        self.form_layout = QFormLayout()

        # Section 1 Name label and text box
        self.horizontal_layout1 = QHBoxLayout()

        self.name_label = QLabel('Name')
        self.name_input = QLineEdit()

        self.horizontal_layout1.addWidget(self.name_label)
        self.horizontal_layout1.addWidget(self.name_input)

        self.form_layout.addRow(self.horizontal_layout1)

        # Section 2 Address and Age input
        self.vertical_layout2 = QVBoxLayout()

        self.address_label = QLabel('Address')
        self.address_input = QLineEdit()

        self.age_label = QLabel('Age')
        self.age_input = QLineEdit()

        # add lables and corresponding input areas in the correct order
        for item in [self.address_label, self.address_input, self.age_label, self.age_input]:
            self.vertical_layout2.addWidget(item)

        self.form_layout.addRow(self.vertical_layout2)

        # Set dialog layout
        self.setLayout(self.form_layout)
