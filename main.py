import sys
import PySide6.QtCore


def get_python_version() -> str:
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    print(f'PySide6 version: {PySide6.__version__}')
    print(f'Qt version: {PySide6.QtCore.__version__}')
