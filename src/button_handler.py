########## Button handler ##########
# Imports
import sys
from loader import load_ui
from interface.ui_new_project import Ui_addNewProject
from PySide6.QtWidgets import QDialog, QPushButton, QVBoxLayout

overlay = None

# def connect_buttons(main_page, stack, new_project_page):
def connect_buttons(main_window):
    # Top menu buttons

    # Universal buttons
    main_exit = main_window.findChild(QPushButton, "mainExit")
    main_exit.clicked.connect(exit_clicked)


    # Main menu buttons
    add_project = main_window.findChild(QPushButton, "addProject")
    add_project.clicked.connect(lambda: add_project_clicked(main_window))
    view_projects = main_window.findChild(QPushButton, "viewProjects")
    view_projects.clicked.connect(lambda: view_projects_clicked(main_window))
    view_archive = main_window.findChild(QPushButton, "viewArchive")
    view_archive.clicked.connect(lambda: view_archive_clicked(main_window))

    # Add project menu buttons
    add_everyday = main_window.findChild(QPushButton, "addEveryday")
    # add_everyday.clicked.connect(everyday_project_clicked)
    add_programming = main_window.findChild(QPushButton, "addProgramming")
    # add_programming.clicked.connect(programming_project_clicked)

    # View projects/archive buttons


# Universal buttons
def return_to_main_clicked():
    print("Return to main menu clicked")

def exit_clicked():
    print("Exiting program...")
    close = input("Are you sure you want to quit? y/n: ").upper()
    if close == "Y":
        sys.exit()
    else:
        print("Returning to previous menu")


# Main menu buttons
def add_project_clicked(parent_window):
    print("Add project clicked!")
    dialog = QDialog(parent_window)
    ui = Ui_addNewProject()
    ui.setupUi(dialog)
    ui.addEveryday.clicked.connect(lambda: everyday_project_clicked(dialog))
    ui.addProgramming.clicked.connect(lambda: programming_project_clicked(dialog))
    ui.returnToMainAddProject.clicked.connect(dialog.accept)
    ui.exitAddProject.clicked.connect(exit_clicked)
    
    
    dialog.exec()

def view_projects_clicked():
    print("View projects clicked")

def view_archive_clicked():
    print("View archive clicked")

# Add project menu buttons
def everyday_project_clicked(dialog):
    print("Add everyday project clicked")

def programming_project_clicked(dialog):
    print("Add programming project clicked")

