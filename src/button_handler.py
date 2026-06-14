########## Button handler ##########
# Imports
import sys


from interface.ui_everyday import Ui_everydayProjectEditor
from interface.ui_main import Ui_mainMenu
from interface.ui_new_project import Ui_addNewProject
from interface.ui_programming import Ui_programmingProjectEditor
from interface.ui_tabs import Ui_Viewer

from PySide6.QtWidgets import QPushButton

def connect_buttons(window):
    add_project = window.findChild(QPushButton, "addProject")
    add_project.clicked.connect(add_project_clicked)

# Universal buttons
def return_to_main_clicked():
    print("Return to main menu clicked")

def exit_clicked():
    print("Exiting program...")
    close = input("Are you sure you want to quit? y/n").upper()
    if close == "Y":
        sys.exit()
    else:
        print("Returning to previous menu")

# Main menu buttons
def add_project_clicked():
    print("Add project clicked!")
# Ui_mainMenu.addProject.clicked.connect(add_project_clicked)

def view_projects_clicked():
    print("View projects clicked")
# Ui_mainMenu.viewProjects.clicked.connect(view_projects_clicked)

def view_archive_clicked():
    print("View archive clicked")
# Ui_mainMenu.viewArchive.clicked.connect(view_archive_clicked)

# Add project menu buttons
def everyday_project_clicked():
    print("Add everyday project clicked")
# Ui_addNewProject.addEveryday.clicked.connect(everyday_project_clicked)

def programming_project_clicked():
    print("Add programming project clicked")
# Ui_addNewProject.addProgramming.clicked.connect(programming_project_clicked)

