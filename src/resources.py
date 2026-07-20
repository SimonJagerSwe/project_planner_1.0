########## Resources ##########
# Imports
import sys

from loader import load_file as loader

from PySide6.QtCore import QDate
from PySide6.QtWidgets import QMessageBox


# Resource files
EVERYDAY_FILE = "project_files/everyday_projects.json"
PROGRAMMING_FILE = "project_files/programming_projects.json"
RECURRING_FILE = "project_files/recurring_tasks.json"
ALL_PROJECTS_FILE = "project_files/all_projects.json"
EVERYDAY_ARCHIVE = "project_files/everyday_archive.json"
PROGRAMMING_ARCHIVE = "project_files/programming_archive.json"
FULL_ARCHIVE = "project_files/full_archive.json"
SUCCESS_WINDOW_TITLE = "Project saved"
SUCCESS_TEXT_MAIN = "Project saved successfully!\nClick OK to return to main menu."
SUCCESS_TEXT_VIEWER = "Project updated successfully!\nClick OK to return to project viewer."
SUCCESS_ARCHIVE_WINDOW = "Project archived"
SUCCESS_ARCHIVE_TEXT = "Project archived successfully\nClick OK to return to return to project viewer"
SAFETY_WINDOW = "Confirm project deletion"
SAFETY_TEXT = "Are you sure you want to delete this project?"
ARCHIVE_WINDOW = "Confirm project archiving"
ARCHIVE_TEXT = "Are you sure you want to archive this project?"
ARCHIVE_DONE_WINDOW = "Finish project"
ARCHIVE_DONE_TEXT = "Do you want to finish this project (set status to Completed and set progress to 100%)?"


# Utility variables
selected_project = None
tab_handler = [
    {
        0 : EVERYDAY_FILE,
        1 : PROGRAMMING_FILE,
        2 : ALL_PROJECTS_FILE,
        3 : RECURRING_FILE
    }, 
    {
        0 : EVERYDAY_ARCHIVE,
        1 : PROGRAMMING_ARCHIVE,
        2 : FULL_ARCHIVE
    }
]

##### Utility functions #####
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


##### Message box dialogs #####
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


# Successfull project creation and return to main menu
def success_message_main():
    success_message = QMessageBox()
    success_message.setWindowTitle(SUCCESS_WINDOW_TITLE)
    success_message.setText(SUCCESS_TEXT_MAIN)
    success_message.setStandardButtons(QMessageBox.Ok)
    success_message.exec()


# Successful project edit and return to project viewer
def success_message_viewer():
    success_message = QMessageBox()
    success_message.setWindowTitle(SUCCESS_WINDOW_TITLE)
    success_message.setText(SUCCESS_TEXT_VIEWER)
    success_message.setStandardButtons(QMessageBox.Ok)
    success_message.exec()


# Successful project archiving
def success_message_archive():
    success_message = QMessageBox()
    success_message.setWindowTitle(SUCCESS_ARCHIVE_WINDOW)
    success_message.setText(SUCCESS_ARCHIVE_TEXT)
    success_message.setStandardButtons(QMessageBox.Ok)
    success_message.exec()


# Delete yes/no message box
def safety_check(parent=None):
    safety_check = QMessageBox()
    safety_check.setWindowTitle(SAFETY_WINDOW)
    safety_check.setText(SAFETY_TEXT)
    delete = QMessageBox.question(
        parent, 
        SAFETY_WINDOW, 
        SAFETY_TEXT,
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        QMessageBox.StandardButton.No
        )
    if delete == QMessageBox.StandardButton.Yes:
        return "delete"
    else:
        return "cancel"


# Archive yes/no checker
def archive_check(parent=None):
    archive_check = QMessageBox()
    archive_check.setWindowTitle(ARCHIVE_WINDOW)
    archive_check.setText(ARCHIVE_TEXT)
    archive = QMessageBox.question(
        parent,
        ARCHIVE_WINDOW,
        ARCHIVE_TEXT,
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        QMessageBox.StandardButton.No
    )
    if archive == QMessageBox.StandardButton.Yes:
        return "archive"
    else:
        return "cancel"

# TODO
# Archive finish yes/no checker
def complete_archive(parent=None):
    ...

# TODO
# No project for editing, deleting or archiving selected
def no_project_selected():
    print("No project selected")
    no_project_selected = QMessageBox()
    no_project_selected.setWindowTitle("No project selected")
    no_project_selected.setText("No project selected")
    no_project_selected.setStandardButtons(QMessageBox.Ok)
    # no_project_selected.exec()


##### Parsers #####
# Project type parser
def parse_type(project):
    if "Language(s)" in project.text():
        project_type = "programming"
    elif "Task name" in project.text():
        project_type = "recurring"
    else:
       project_type =  "everyday"
    return project_type


# Get the correct projects file to delete old version of project
def project_parser(project, project_type):
    # Find project name
    print(f"Project received by parser: {project}\nProject type: {type(project)}\n")
    if type(project) == dict:
        project_name = project["Project name"]
    else:
        for var in project.text().split("\n"):
            if "name" in var:
                project_name = var.split(":")[1].strip()
            
    
    # Load everyday file
    if project_type == "everyday":
        e_projects = loader(EVERYDAY_FILE)
        for project in e_projects:
            if project["Project name"].strip() == project_name:
                print(f"Project found: {project["Project name"]}")
                return project
    # Load programming file
    elif project_type == "programming":
        p_projects = loader(PROGRAMMING_FILE)
        for project in p_projects:
            if project["Project name"].strip() == project_name:
                return project
    # Load recurring task file
    else:
        r_tasks = loader(RECURRING_FILE)
        for task in r_tasks:
            if task["Task name"].strip() == project_name:
                return task
            