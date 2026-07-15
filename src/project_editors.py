########## Project editors ##########
# Imports
import button_handler
import resources

from interface.ui_everyday import Ui_everydayProjectEditor
from interface.ui_programming import Ui_programmingProjectEditor 
from interface.ui_recurring import Ui_recurringProjectEditor
from loader import load_file as loader
from writers import project_data

from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDialog

# Connect editor buttons to reuse the button calls from button_handler.py
def connect_buttons(ui, dialog, main_window, project_type, viewer_dialog=None, current_project=None):
    if project_type == "everyday":
        ui.everydaySave.clicked.connect(lambda: save_and_return(ui, dialog, main_window, viewer_dialog, project_type, current_project))
        # ui.everydaySave.clicked.connect(lambda: resources.delete_project(current_project, project_type))
        # ui.everydaySave.clicked.connect(lambda: project_data(ui, project_type, dialog, main_window))
        ui.everydayClear.clicked.connect(lambda: resources.clear_input(ui))
        ui.everydayReturn.clicked.connect(lambda: resources.return_to_main_clicked(dialog, main_window, viewer_dialog))
        ui.everydayExit.clicked.connect(lambda: resources.exit_clicked(dialog))
    elif project_type == "programming":
        ui.programmingSave.clicked.connect(lambda: save_and_return(ui, dialog, main_window, viewer_dialog, project_type, current_project))
        # ui.programmingSave.clicked.connect(lambda: resources.delete_project(current_project, project_type))
        # ui.programmingSave.clicked.connect(lambda: project_data(ui,project_type, dialog))
        ui.programmingClear.clicked.connect(lambda: resources.clear_input(ui))
        ui.programmingReturn.clicked.connect(lambda: resources.return_to_main_clicked(dialog, main_window, viewer_dialog))
        ui.programmingExit.clicked.connect(lambda: resources.exit_clicked(dialog))
    else:
        ui.saveRecurring.clicked.connect(lambda: save_and_return(ui, dialog, main_window, viewer_dialog, project_type, current_project))
        # ui.saveRecurring.clicked.connect(lambda: resources.delete_project(current_project, project_type))
        # ui.saveRecurring.clicked.connect(lambda: project_type(ui, project_type, dialog, main_window))
        ui.clearRecurring.clicked.connect(lambda: resources.clear_input(ui))
        ui.returnToMainRecurring.clicked.connect(lambda: resources.return_to_main_clicked(dialog, main_window, viewer_dialog))
        ui.exitRecurring.clicked.connect(lambda: resources.exit_clicked(dialog))


# Function to determine which ui to use for editing
def edit_parser(project, viewer_dialog, main_window):
    print(f"Project to edit:\n{project.text()}")

    # Identify project type
    if "Language(s)" in project.text():
        ui = Ui_programmingProjectEditor()
        dialog = QDialog(viewer_dialog)
        ui.setupUi(dialog)
        current_project = project_parser(project, "programming")
        connect_buttons(ui, dialog, main_window, "programming", viewer_dialog, current_project)
        edit_programming(ui, project, main_window)
        dialog.exec()
    elif "Task frequency" in project.text():
        ui = Ui_recurringProjectEditor()
        dialog = QDialog(viewer_dialog)
        ui.setupUi(dialog)
        current_project = project_parser(project, "recurring")
        connect_buttons(ui, dialog, main_window, "recurring", viewer_dialog, current_project)
        edit_recurring(ui, project, main_window)
        dialog.exec()
    else:
        ui = Ui_everydayProjectEditor()
        dialog = QDialog(viewer_dialog)
        ui.setupUi(dialog)
        current_project = project_parser(project, "everyday")
        connect_buttons(ui, dialog, main_window, "everyday", viewer_dialog, current_project)
        edit_everyday(ui, project, main_window)
        dialog.exec()


# Get the correct projects file to delete old version of project
def project_parser(project, type):
    # Find project name
    for var in project.text().split("\n"):
        if "name" in var:
            project_name = var.split(":")[1].strip()
    
    # Load everyday file
    if type == "everyday":
        e_projects = loader(resources.EVERYDAY_FILE)
        for project in e_projects:
            if project["Project name"] == project_name:
                return project
    # Load programming file
    elif type == "programming":
        p_projects = loader(resources.PROGRAMING_FILE)
        for project in p_projects:
            if project["Project name"] == project_name:
                return project
    # Load recurring task file
    else:
        r_tasks = loader(resources.RECURRING_FILE)
        for task in r_tasks:
            if task["Task name"] == project_name:
                return task

def save_and_return(ui, dialog, main_window, viewer_dialog, project_type, current_project):
    resources.delete_project(current_project, project_type)
    project_data(ui, project_type, dialog, main_window)
    dialog.close()
    if viewer_dialog is not None:
        viewer_dialog.close()
        button_handler.project_viewer_clicked(main_window, 0)


def edit_everyday(ui, project, main_window):
    print("Editing everyday...")
    current_project = project_parser(project, "everyday")
    print(current_project)
    ui.everydayName.setText(current_project["Project name"])
    ui.everydayStart.setDate(QDate.fromString(current_project["Project start"], "yyyy-MM-dd"))
    ui.everydayFinish.setDate(QDate.fromString(current_project["Project end"], "yyyy-MM-dd"))
    ui.everydayNotes.setText(current_project["Project notes"])
    progress_text = current_project["Project progress"]
    progress_value = int(progress_text.strip("%"))
    ui.everydayProgressSlider.setValue(progress_value)
    ui.everydayProgressSlider.valueChanged.connect(lambda value: 
        ui.everydayProgressPercent.setText(f"{value}%"))
    ui.everydayStatus.setCurrentText(current_project["Project status"])


def edit_programming(ui, project, main_window):
    print("Editing programming...")
    current_project = project_parser(project, "programming")
    print(current_project)
    ui.programmingName.setText(current_project["Project name"])
    ui.programmingStart.setDate(QDate.fromString(current_project["Project start"], "yyyy-MM-dd"))
    ui.programmingFinish.setDate(QDate.fromString(current_project["Project end"], "yyyy-MM-dd"))
    ui.languagesEdit.setText(current_project["Language(s)"])
    ui.githubEdit.setText(current_project["GitHub link"])
    progress_text = current_project["Project progress"]
    progress_value = int(progress_text.strip("%"))
    ui.programmingProgressSlider.setValue(progress_value)
    ui.programmingProgressSlider.valueChanged.connect(lambda value:
        ui.programmingProgressPercent.setText(f"{value}%"))
    ui.programmingProgressSlider.setValue(progress_value)
    ui.programmingProgressPercent.setText(progress_text)
    ui.programmingStatus.setCurrentText(current_project["Project status"])


def edit_recurring(ui, project, main_window):
    print("Editing recurring project...")
    current_project = project_parser(project, "recurring")
    print(current_project)
    ui.recurringName.setText(current_project["Task name"])
    ui.recurringFrequency.setCurrentText(current_project["Task frequency"])
    ui.recurringNotes.setText(current_project["Task notes"])
    