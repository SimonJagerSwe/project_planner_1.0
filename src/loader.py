from PySide6 import QtCore, QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

class Loader(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("interface/main.ui", None)
    
    def show(self):
        self.ui.show()
