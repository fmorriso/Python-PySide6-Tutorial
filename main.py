import sys

import PySide6.QtCore
from PySide6.QtWidgets import QApplication
import pyautogui as pg

from dialog_form_grid_layout import DialogFormGridLayout
from dialog_form_vertical_layout import DialogFormVerticalLayout
from dialog_form_fancy_layout_window import DialogFormFancyLayout


def get_python_version() -> str:
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


def show_vertical_dialog_form():
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = DialogFormVerticalLayout()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())


def show_grid_dialog_form():
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = DialogFormGridLayout()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())


def show_fancy_layout_window(title: str):
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    window = DialogFormFancyLayout(title)
    window.show()
    # Run the main Qt loop
    sys.exit(app.exec())


if __name__ == '__main__':
    msg = f'Python version: {get_python_version()}'
    print(msg)
    print(f'PySide6 version: {PySide6.__version__}')
    print(f'Qt version: {PySide6.QtCore.__version__}')
    print(f'PyAutoGUI version: {pg.__version__}')

    # uncomment one of the following at a time to see different layout examples:
    # show_vertical_dialog_form()
    # show_grid_dialog_form()
    show_fancy_layout_window(msg)
