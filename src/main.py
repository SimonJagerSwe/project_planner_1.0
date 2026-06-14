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
    main_window = load_ui("interface/main.ui")
    button_handler.connect_buttons(main_window)
    main_window.show()
    sys.exit(app.exec())
    '''stack = QStackedWidget()
    home_screen = load_ui("interface/main.ui")
    main_page = home_screen.takeCentralWidget()    
    stack = QStackedWidget()
    stack.addWidget(main_page)
    project_interface = load_ui("interface/newProject.ui")
    stack.addWidget(project_interface)
    stack.setCurrentWidget(main_page)
    home_screen.setCentralWidget(stack)
    button_handler.connect_buttons(main_page, stack, project_interface)
    home_screen.show()
    sys.exit(app.exec())'''

if __name__ == "__main__":
    main()
