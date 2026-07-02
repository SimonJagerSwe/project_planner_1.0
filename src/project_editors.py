########## Project editors ##########
# Imports
import resources, writers

from interface.ui_everyday import Ui_everydayProjectEditor
from interface.ui_programming import Ui_programmingProjectEditor 
from interface.ui_recurring import Ui_recurringProjectEditor
from loader import load_file as loader

from PySide6.QtWidgets import QDialog

# Function to determine which ui to use for editing
def edit_parser(project):
    print(f"Project to edit:\n{project.text()}")
    if "Language(s)" in project.text():
        ui = Ui_programmingProjectEditor()
        edit_programming(ui, project)
    elif "Task frequency" in project.text():
        ui = Ui_recurringProjectEditor()
        edit_recurring(ui, project)
    else:
        ui = Ui_everydayProjectEditor()
        edit_everyday(ui, project)


# Get the correct projects file to delete old version of project
def project_parser(project, type):
    # Find project name
    for var in project.text().split("\n"):
        if "name" in var:
            print(var)
            project_name = var.split(":")[1].strip()
            print(project_name)
    
    # Load everyday file
    if type == "everyday":
        e_projects = loader(resources.EVERYDAY_FILE)
        for project in e_projects:
            if project["Project name"] == project_name:
                print(f"Project found:\n{project}")
    elif type == "programming":
        p_projects = loader(resources.PROGRAMING_FILE)
        for project in p_projects:
            if project["Project name"] == project_name:
                print(f"Project found:\n{project}")
        
    else:
        r_tasks = loader(resources.RECURRING_FILE)
        for task in r_tasks:
            if task["Task name"] == project_name:
                print(f"Task found:\n{project_name}")


def edit_everyday(ui, project):
    print("Editing everyday...")
    project_parser(project, "everyday")
    dialog = QDialog()
    ui.setupUi(dialog)
    dialog.exec()


def edit_programming(ui, project):
    print("Editing programming...")
    project_parser(project, "programming")
    dialog = QDialog()
    ui.setupUi(dialog)
    dialog.exec()


def edit_recurring(ui, project):
    print("Editing recurring project...")
    project_parser(project, "recurring")
    dialog = QDialog()
    ui.setupUi(dialog)
    dialog.exec()

'''
def connect_editor_buttons(ui, dialog, main_window, project_type):
    if project_type == "everyday":
        ui.everydaySave.clicked.connect(
            lambda: writers.writer(ui, resources.EVERYDAY_FILE, dialog, main_window)
        )
        ui.everydayClear.clicked.connect(lambda: writers.clear_input(ui))
        ui.everydayReturn.clicked.connect(
            lambda: resources.return_to_main_clicked(dialog, main_window)
        )
        ui.everydayExit.clicked.connect(lambda: resources.exit_clicked(dialog))

    elif project_type == "programming":
        ui.programmingSave.clicked.connect(
            lambda: writers.writer(ui, resources.PROGRAMMING_FILE, dialog, main_window)
        )
        ui.programmingClear.clicked.connect(lambda: writers.clear_input(ui))
        ui.programmingReturn.clicked.connect(
            lambda: resources.return_to_main_clicked(dialog, main_window)
        )
        ui.programmingExit.clicked.connect(lambda: resources.exit_clicked(dialog))

    elif project_type == "recurring":
        ui.saveRecurring.clicked.connect(
            lambda: writers.writer(ui, resources.RECURRING_FILE, dialog, main_window)
        )
        ui.clearRecurring.clicked.connect(lambda: writers.clear_input(ui))
        ui.returnToMainRecurring.clicked.connect(
            lambda: resources.return_to_main_clicked(dialog, main_window)
        )
        ui.exitRecurring.clicked.connect(lambda: resources.exit_clicked(dialog))'''
