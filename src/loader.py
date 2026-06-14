from PySide6 import QtCore
from PySide6.QtUiTools import QUiLoader


def load_ui(ui_path, parent=None):
    loader = QUiLoader()
    ui_file = QtCore.QFile(ui_path)
    if not ui_file.open(QtCore.QFile.OpenModeFlag.ReadOnly):
        raise RuntimeError(f"Can't open {ui_file}")
    widget = loader.load(ui_file, parent)
    ui_file.close()

    return widget
