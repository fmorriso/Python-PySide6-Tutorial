import sys

import PySide6.QtCore
from PySide6.QtWidgets import QApplication
from dialog_form_vertical_layout import DialogFormVerticalLayout


def get_python_version() -> str:
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


def show_dialog_form():
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = DialogFormVerticalLayout()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())


if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    print(f'PySide6 version: {PySide6.__version__}')
    print(f'Qt version: {PySide6.QtCore.__version__}')
    show_dialog_form()
