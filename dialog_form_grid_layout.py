from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QHBoxLayout, \
    QRadioButton

from settings import Settings


class DialogFormGridLayout(QDialog):

    def __init__(self, parent=None):
        super(DialogFormGridLayout, self).__init__(parent)

        self.setWindowTitle("Example PySide6 Dialog Form with grid layout")

        # use scaled size via PyAutoGUI:
        settings = Settings(pct=0.45)
        dialog_width = settings.screen_width
        dialog_height = settings.screen_height

        # set dialog width and height
        self.setFixedSize(QSize(dialog_width, dialog_height))

        self.form_layout = QFormLayout()

        # Section 1 Name label and text box
        self.name_area_layout = QHBoxLayout()

        self.name_label = QLabel('Name')
        self.name_input = QLineEdit()

        self.name_area_layout.addWidget(self.name_label)
        self.name_area_layout.addWidget(self.name_input)

        self.form_layout.addRow(self.name_area_layout)

        # Section 2 Address and Age input area
        self.address_age_area_layout = QVBoxLayout()

        self.address_label = QLabel('Address')
        self.address_input = QLineEdit()

        self.age_label = QLabel('Age')
        self.age_input = QLineEdit()

        # add labels and corresponding input areas in the correct order
        for item in [self.address_label, self.address_input, self.age_label, self.age_input]:
            self.address_age_area_layout.addWidget(item)

        self.form_layout.addRow(self.address_age_area_layout)

        # Section 3 Add radio buttons
        self.gender_area_layout = QHBoxLayout()
        self.gender_area_layout.setAlignment(Qt.AlignLeft)

        self.radio1 = QRadioButton('Male')
        self.radio2 = QRadioButton('Female')

        for item in [self.radio1, self.radio2]:
            self.gender_area_layout.addWidget(item)

        self.form_layout.addRow(QLabel('Gender: '), self.gender_area_layout)

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
