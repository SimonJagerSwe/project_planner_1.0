########## Button handler ##########
# Imports
import sys
from loader import load_ui
from interface.ui_everyday import Ui_everydayProjectEditor
from interface.ui_new_project import Ui_addNewProject
from interface.ui_programming import Ui_programmingProjectEditor
from interface.ui_tabs import Ui_Viewer
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QDialog, QMessageBox, QPushButton, QTabWidget

overlay = None

##### Universal buttons #####
# Return to main menu
def return_to_main_clicked(current_dialog, main_window):
    print("Return to main menu clicked")
    if current_dialog is not None:
        current_dialog.close()
    main_window.show()
    main_window.setEnabled(True)


# Exit program
def exit_clicked(parent=None):
    print("Exiting program...")
    close = QMessageBox.question(
        parent, 
        "Confirm exit", 
        "Are you sure you want to quit?",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        QMessageBox.StandardButton.No
        )
    if close == QMessageBox.StandardButton.Yes:
        sys.exit()
    else:
        print("Returning to previous menu")


##### Non-universal buttons #####
# Main menu buttons
def main_menu_buttons(main_window):
    # Regular buttons
    add_project = main_window.findChild(QPushButton, "addProject")
    add_project.clicked.connect(lambda: add_project_clicked(main_window))
    view_projects = main_window.findChild(QPushButton, "viewProjects")
    view_projects.clicked.connect(lambda: view_projects_clicked(main_window))
    view_archive = main_window.findChild(QPushButton, "viewArchive")
    view_archive.clicked.connect(lambda: view_archive_clicked(main_window))
    main_exit = main_window.findChild(QPushButton, "mainExit")
    main_exit.clicked.connect(lambda: exit_clicked(main_window))
    
    # Drop down menu actions
    everyday_action = main_window.findChild(QAction, "actionAddEveryday")
    everyday_action.triggered.connect(lambda: everyday_project_clicked(None, main_window))
    programming_action = main_window.findChild(QAction, "actionAddProgramming")
    programming_action.triggered.connect(lambda: (programming_project_clicked(None, main_window)))
    projects_action = main_window.findChild(QAction, "actionProjects")
    projects_action.triggered.connect(lambda: (view_projects_clicked(main_window)))
    archive_action = main_window.findChild(QAction, "actionArchive")
    archive_action.triggered.connect(lambda: (view_archive_clicked(main_window)))
    exit_action = main_window.findChild(QAction, "actionExit")
    exit_action.triggered.connect(lambda: (exit_clicked(main_window)))


# Add project menu
def add_project_clicked(main_window):
    print("Add project clicked!")
    add_project = QDialog(main_window)
    ui = Ui_addNewProject()
    ui.setupUi(add_project)
    ui.addEveryday.clicked.connect(lambda: everyday_project_clicked(add_project, main_window))
    ui.addProgramming.clicked.connect(lambda: programming_project_clicked(add_project, main_window))
    ui.returnToMainAddProject.clicked.connect(lambda: (return_to_main_clicked(add_project, main_window)))
    ui.exitAddProject.clicked.connect(lambda: exit_clicked(add_project))
    add_project.exec()


# Add everyday project
def everyday_project_clicked(current_dialog, main_window):
    print("Add everyday project clicked")
    if current_dialog is not None:
        current_dialog.close()
    main_window.close()
    everyday_dialog = QDialog(None)
    ui = Ui_everydayProjectEditor()
    ui.setupUi(everyday_dialog)
    ui.saveEveryday.clicked.connect(save_everyday_clicked)
    ui.clearEveryday.clicked.connect(clear_everyday_clicked)
    ui.returnToMainEveryday.clicked.connect(lambda: return_to_main_clicked(everyday_dialog, main_window))
    ui.exitEveryday.clicked.connect(lambda: exit_clicked(everyday_dialog))
    everyday_dialog.exec()
    main_window.show()

def save_everyday_clicked():
    print("Saving everyday project...")

def clear_everyday_clicked():
    print("Clearing all everyday project parameters...")


# Add programming project
def programming_project_clicked(current_dialog, main_window):
    print("Add programming project clicked")
    if current_dialog is not None:
        current_dialog.close()
    main_window.close()
    dialog = QDialog(main_window)
    ui = Ui_programmingProjectEditor()
    ui.setupUi(dialog)
    dialog.exec()
    main_window.show()


# View projects
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


# View archive
def view_archive_clicked(main_window):
    print("View archive clicked")
    main_window.close()
    view_archive = QDialog(main_window)
    ui = Ui_Viewer()
    ui.setupUi(view_archive)
    ui.viewer.setCurrentIndex(1)
    view_archive.exec()
    main_window.show()

