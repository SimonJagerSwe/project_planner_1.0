################### Main file ####################
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

import button_handler

from loader import Loader

from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

# loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)
window = Loader()

button_handler.connect_buttons(window.ui)

def main():
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
