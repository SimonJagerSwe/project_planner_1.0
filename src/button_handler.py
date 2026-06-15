########## Button handler ##########
# Imports
import sys
from loader import load_ui
from interface.ui_everyday import Ui_everydayProjectEditor
from interface.ui_new_project import Ui_addNewProject
from interface.ui_programming import Ui_programmingProjectEditor
from interface.ui_tabs import Ui_Viewer
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QPushButton, QTabWidget

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
def add_project_clicked(main_window):
    print("Add project clicked!")
    add_project = QDialog(main_window)
    ui = Ui_addNewProject()
    ui.setupUi(add_project)
    ui.addEveryday.clicked.connect(lambda: everyday_project_clicked(add_project, main_window))
    ui.addProgramming.clicked.connect(lambda: programming_project_clicked(add_project, main_window))
    ui.returnToMainAddProject.clicked.connect(add_project.accept)
    ui.exitAddProject.clicked.connect(exit_clicked)    
    add_project.exec()

def view_projects_clicked(main_window):
    print("View projects clicked")
    main_window.close()
    view_projects = QDialog(main_window)
    ui = Ui_Viewer()
    ui.setupUi(view_projects)
    ui.viewer.setCurrentIndex(0)
    ui.projectTabs.setCurrentIndex(0)
    view_projects.exec()
    main_window.show()


def view_archive_clicked(main_window):
    print("View archive clicked")
    main_window.close()
    view_archive = QDialog(main_window)
    ui = Ui_Viewer()
    ui.setupUi(view_archive)
    ui.viewer.setCurrentIndex(1)
    view_archive.exec()
    main_window.show()

# Add project menu buttons
def everyday_project_clicked(current_dialog, main_window):
    print("Add everyday project clicked")
    current_dialog.close()
    main_window.close()
    everyday_dialog = QDialog(None)
    ui = Ui_everydayProjectEditor()
    ui.setupUi(everyday_dialog)
    everyday_dialog.exec()
    main_window.show()

def programming_project_clicked(current_dialog, main_window):
    print("Add programming project clicked")
    current_dialog.close()
    main_window.close()
    dialog = QDialog(main_window)
    ui = Ui_programmingProjectEditor()
    ui.setupUi(dialog)
    dialog.exec()
    main_window.show()

