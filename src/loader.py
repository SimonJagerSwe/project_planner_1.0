########## Loader ##########
# Imports
from PySide6 import QtCore
from PySide6.QtUiTools import QUiLoader


# Loader function, to save load at runtime
def load_ui(ui_path, parent=None):
    loader = QUiLoader()
    ui_file = QtCore.QFile(ui_path)

    if not ui_file.open(QtCore.QFile.OpenModeFlag.ReadOnly):
        raise RuntimeError(f"Can't open {ui_path}")
    
    widget = loader.load(ui_file, parent)
    ui_file.close()

    if widget is None:
        raise RuntimeError(f"Failed to read {ui_path}")
    
    return widget
