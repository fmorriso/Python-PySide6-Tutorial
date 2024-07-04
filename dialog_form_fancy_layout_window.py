# https://www.pythonguis.com/tutorials/pyside6-layouts/

from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QColor, QColorConstants
from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout

from coloredwidget import ColoredWidget
from settings import Settings


class DialogFormFancyLayout(QMainWindow):

    def __init__(self):
        super(DialogFormFancyLayout, self).__init__()

        self.setWindowTitle("Fancy PySide6 Layout Example")

        # use scaled size via PyAutoGUI:
        settings = Settings(pct=0.45)
        dialog_width = settings.screen_width
        dialog_height = settings.screen_height

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

        layout2.addWidget(ColoredWidget(QColorConstants.Red))
        layout2.addWidget(ColoredWidget(QColorConstants.Yellow))
        layout2.addWidget(ColoredWidget(QColorConstants.DarkMagenta)) # 'purple

        layout1.addLayout( layout2 )

        layout1.addWidget(ColoredWidget(QColorConstants.DarkGreen))

        layout3.addWidget(ColoredWidget(QColorConstants.Red))
        lphs_orange = QColor(233,119,23)
        layout3.addWidget(ColoredWidget(lphs_orange))  # Lewis-Palmer High School Orange
        layout3.addWidget(ColoredWidget(QColorConstants.Magenta))

        layout1.addLayout( layout3 )

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)