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
from loader import load_ui
from PySide6 import QtWidgets


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = load_ui("interface/main.ui")
    button_handler.connect_buttons(window)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
