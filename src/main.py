########## Main file ##########
##################################################
##################################################
################                  ################
##############                      ##############
############                          ############
##########     PROJECT PLANNER v1.0     ##########
########          (c)Simon Jäger          ########
##########          2026-06-12          ##########
############                          ############
##############                      ##############
################                  ################
##################################################
##################################################


# Imports
import sys

from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

def main():
    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)

    window = loader.load("interface/main.ui")
    window.show()

    app.exec()

if __name__ == "__main__":
    main()
