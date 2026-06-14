########## Button handler ##########
# Imports
import sys
from loader import load_ui

from PySide6.QtWidgets import QDialog, QPushButton, QVBoxLayout

overlay = None

# def connect_buttons(main_page, stack, new_project_page):
def connect_buttons(main_window):
    # Top menu buttons

    # Universal buttons
    main_exit = main_window.findChild(QPushButton, "mainExit")
    # main_exit.clicked.connect(exit_clicked)


    # Main menu buttons
    add_project = main_window.findChild(QPushButton, "addProject")
    if add_project is None:
        raise RuntimeError("Could not find reqested ui file")
    # add_project.clicked.connect(lambda: add_project_clicked(new_project_page))
    # add_project.clicked.connect(lambda: stack.setCurrentWidget(new_project_page))
    add_project.clicked.connect(lambda: add_project_clicked(main_window))
    
    
    view_projects = main_window.findChild(QPushButton, "viewProjects")
    view_projects.clicked.connect(view_projects_clicked)
    view_archive = main_window.findChild(QPushButton, "viewArchive")
    view_archive.clicked.connect(view_archive_clicked)

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
    # project_interface = load_ui("interface/newProject.ui", parent=window)
    # project_interface.show()
    dialog = QDialog(parent_window)
    dialog.setModal(True)
    dialog.setWindowTitle("Project Planner 1.0 - Add new project")
    dialog.setLayout(QVBoxLayout())

    project_selector = load_ui("interface/newProject.ui", parent=dialog)
    dialog.layout().addWidget(project_selector)
    dialog.exec()



def view_projects_clicked():
    print("View projects clicked")

def view_archive_clicked():
    print("View archive clicked")

# Add project menu buttons
def everyday_project_clicked():
    print("Add everyday project clicked")

def programming_project_clicked():
    print("Add programming project clicked")

