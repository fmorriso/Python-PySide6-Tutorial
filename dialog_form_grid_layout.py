from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QHBoxLayout, \
    QRadioButton

from settings import Settings


class DialogFormGridLayout(QDialog):

    def __init__(self, parent=None):
        super(DialogFormGridLayout, self).__init__(parent)

        self.setWindowTitle("Example PySide6 Dialog Form with grid layout")

        # use scaled size via PyAutoGUI:
        settings = Settings()
        dialog_width = settings.screen_width  # 512
        dialog_height = settings.screen_height  # 384

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

        # add labels and corresponding input areas in the correct order
        for item in [self.address_label, self.address_input, self.age_label, self.age_input]:
            self.vertical_layout2.addWidget(item)

        self.form_layout.addRow(self.vertical_layout2)

        # Section 3 Add radio buttons
        self.horizontal_layout2 = QHBoxLayout()
        self.horizontal_layout2.setAlignment(Qt.AlignLeft)

        self.radio1 = QRadioButton('Male')
        self.radio2 = QRadioButton('Female')

        for item in [self.radio1, self.radio2]:
            self.horizontal_layout2.addWidget(item)

        self.form_layout.addRow(QLabel('Gender: '), self.horizontal_layout2)

        # Section 4 - OK and Cancel buttons
        self.button_row_layout = QHBoxLayout()
        self.button_row_layout.setContentsMargins(0, dialog_height / 3, 0, 0)

        self.Ok_button = QPushButton('Ok')
        self.Cancel_button = QPushButton('Cancel')

        for item in [self.Ok_button, self.Cancel_button]:
            self.button_row_layout.addWidget(item)

        self.form_layout.addRow(self.button_row_layout)

        # Set dialog layout
        self.setLayout(self.form_layout)
