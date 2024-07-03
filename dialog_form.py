from PySide6.QtWidgets import QDialog


class DialogForm(QDialog):

    def __init__(self, parent=None):
        super(DialogForm, self).__init__(parent)
        self.setWindowTitle("Example PySide6 Dialog Form")
