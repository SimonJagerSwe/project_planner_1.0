########## Resources ##########
# Imports
import json
import sys

from loader import load_file as loader
from writers import writer

from PySide6.QtCore import QDate
from PySide6.QtWidgets import QMessageBox

# Resource files
EVERYDAY_FILE = "project_files/everyday_projects.json"
PROGRAMING_FILE = "project_files/programming_projects.json"
RECURRING_FILE = "project_files/recurring_tasks.json"
ALL_PROJECTS_FILE = "project_files/all_projects.json"
EVERYDAY_ARCHIVE = "project_files/everyday_archive.json"
PROGRAMMING_ARCHIVE = "project_files/programming_archive.json"
FULL_ARCHIVE = "project_files/full_archive.json"
SUCCESS_WINDOW_TITLE = "Project saved"
SUCCESS_TEXT = "Project saved successfully!\nClick OK to return to main menu."

# Utility variables
selected_project = None
tab_handler = [
    {
        0 : EVERYDAY_FILE,
        1 : PROGRAMING_FILE,
        2 : ALL_PROJECTS_FILE,
        3 : RECURRING_FILE
    }, 
    {
        0 : EVERYDAY_ARCHIVE,
        1 : PROGRAMMING_ARCHIVE,
        2 : FULL_ARCHIVE
    }
]

# Utility functions
# Return to main menu
def return_to_main_clicked(current_dialog, main_window, parent_dialog=None):
    print("Return to main menu clicked")
    if current_dialog is not None:
        current_dialog.close()
    if parent_dialog is not None:
        parent_dialog.close()
    if main_window is not None:
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


# Clear project input
def clear_input(ui):
    if "everydayClear" in dir(ui):
        print("Clearing everyday project...")
        ui.everydayName.setText("")
        ui.everydayStart.setDate(QDate.currentDate())
        ui.everydayFinish.setDate(QDate.currentDate())
        ui.everydayNotes.setText("")
        ui.everydayProgressSlider.setValue(0)
        ui.everydayProgressPercent.setText("0%")
        ui.everydayStatus.setCurrentText("Select project status")
    elif "programmingClear" in dir(ui):
        print("Clearing programming project")
        ui.programmingName.setText("")
        ui.programmingStart.setDate(QDate.currentDate())
        ui.programmingFinish.setDate(QDate.currentDate())
        ui.languagesEdit.setText("")
        ui.githubEdit.setText("")
        ui.programmingNotes.setText("")
        ui.programmingProgressSlider.setValue(0)
        ui.programmingProgressPercent.setText("0%")
        ui.programmingStatus.setCurrentText("Select project status")
    else:
        print("Clearing recurring task")
        ui.recurringName.setText("")
        ui.recurringFrequency.setCurrentText("Select frequency")
        ui.recurringNotes.setText("")


# Successfull project creation
def success_message():
    success_message = QMessageBox()
    success_message.setWindowTitle(SUCCESS_WINDOW_TITLE)
    success_message.setText(f"{SUCCESS_TEXT}")
    success_message.setStandardButtons(QMessageBox.Ok)
    success_message.exec()


# Delete project from project type file, both for deletion and for editing
def delete_project(project, type):
    print(f"Project for deletion:\n{project}")
    if type == "everyday":
        projects_file = EVERYDAY_FILE
    elif type == "programming":
        projects_file = PROGRAMING_FILE
    else:
        projects_file = RECURRING_FILE

    projects = loader(projects_file)
    all_projects = loader(ALL_PROJECTS_FILE)
    print(f"Current projects:\n{projects}\n")
    try:
        projects.remove(project)
    except:
        print("Project not present in selected projects type")
    try:
        all_projects.remove(project)
    except:
        print("Project not present in full projects")

    print(f"Selected projects type after removal:\n{projects}")
    print(f"Full projects after removal:\n{all_projects}\n")

    writer(projects, type)


# TODO
# No project for editing or archiving selected
def no_project_selected():
    print("No project selected")
    no_project_selected = QMessageBox()
    no_project_selected.setWindowTitle("No project selected")
    no_project_selected.setText("No project selected")
    no_project_selected.setStandardButtons(QMessageBox.Ok)
    # no_project_selected.exec()
