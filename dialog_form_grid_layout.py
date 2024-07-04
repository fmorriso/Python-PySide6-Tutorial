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
        self.horizontal_layout1 = QHBoxLayout()

        self.label1 = QLabel('Name')
        self.input1 = QLineEdit()

        self.horizontal_layout1.addWidget(self.label1)
        self.horizontal_layout1.addWidget(self.input1)

        self.form_layout.addRow(self.horizontal_layout1)
