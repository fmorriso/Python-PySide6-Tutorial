from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        if color is QColor:
            palette.setColor(QPalette.Window, color)
        else:
            palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)