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
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget


def main():
    app = QApplication(sys.argv)
    home_screen = QMainWindow()
    stack = QStackedWidget()
    home_screen.setCentralWidget(stack)
    main_window = load_ui("interface/main.ui")
    main_page = main_window.centralWidget()
    # main_page = (
    #     main_window.centralWidget()
    #     if hasattr(main_window, "centralWidget")
    #     else main_window)
    project_interface = load_ui("interface/newProject.ui")

    stack.addWidget(main_page)
    stack.addWidget(project_interface)
    stack.setCurrentWidget(main_page)
    button_handler.connect_buttons(main_page, stack, project_interface)
    home_screen.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
