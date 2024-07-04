# https://www.pythonguis.com/tutorials/pyside6-layouts/

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PySide6.QtGui import QPalette, QColor, QFont

from color import Color


class FancyLayoutMainWindow(QMainWindow):

    def __init__(self):
        super(FancyLayoutMainWindow, self).__init__()

        self.setWindowTitle("Fancy Layout Example")

        # used fixed size for dialog (will use PyAutoGUI later on to scale to percent of device size)
        dialog_width = 512
        dialog_height = 384

        default_font = QFont('Monospace')
        default_font.setPointSize(dialog_height * 0.05)
        self.setFont(default_font)

        # set dialog width and height
        self.setFixedSize(QSize(dialog_width, dialog_height))

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout1.setContentsMargins(0,0,0,0)
        layout1.setSpacing(20)

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))

        layout1.addLayout( layout2 )

        layout1.addWidget(Color('green'))

        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))

        layout1.addLayout( layout3 )

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)