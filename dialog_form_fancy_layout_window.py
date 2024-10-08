# https://www.pythonguis.com/tutorials/pyside6-layouts/

from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QColor, QColorConstants
from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout

from coloredwidget import ColoredWidget
from settings import Settings


class DialogFormFancyLayout(QMainWindow):

    def __init__(self, title):
        super(DialogFormFancyLayout, self).__init__()

        self.setWindowTitle(f"Fancy PySide6 Layout Example - {title}")

        # use scaled size via PyAutoGUI:
        settings = Settings(pct=0.45)
        dialog_width = settings.screen_width
        dialog_height = settings.screen_height

        default_font = QFont('Monospace')
        default_font.setPointSize(dialog_height * 0.05)
        self.setFont(default_font)

        # set dialog width and height
        self.setFixedSize(QSize(dialog_width, dialog_height))

        outer_horizontal_layout = QHBoxLayout()
        inner_left_layout = QVBoxLayout()
        inner_middle_layout = QVBoxLayout()
        inner_right_layout = QVBoxLayout()

        outer_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        outer_horizontal_layout.setSpacing(int(20 * settings.screenPct))

        for item in [ColoredWidget(QColorConstants.Red),
                     ColoredWidget(QColorConstants.Yellow),
                     ColoredWidget(QColorConstants.DarkMagenta)]:
            inner_left_layout.addWidget(item)

        # left
        outer_horizontal_layout.addLayout(inner_left_layout)

        # middle
        inner_middle_layout.addWidget(ColoredWidget(QColorConstants.DarkGreen))
        outer_horizontal_layout.addLayout(inner_middle_layout)

        # right
        inner_right_layout.addWidget(ColoredWidget(QColorConstants.DarkCyan))
        lphs_orange = QColor(233, 119, 23)
        inner_right_layout.addWidget(ColoredWidget(lphs_orange))  # Lewis-Palmer High School Orange
        inner_right_layout.addWidget(ColoredWidget(QColorConstants.Magenta))

        outer_horizontal_layout.addLayout(inner_right_layout)

        widget = QWidget()
        widget.setLayout(outer_horizontal_layout)
        self.setCentralWidget(widget)
