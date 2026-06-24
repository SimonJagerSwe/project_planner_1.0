########## Resources ##########
# Imports
import sys

import resources

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
tab_handler = [
    {
        0 : resources.EVERYDAY_FILE,
        1 : resources.PROGRAMING_FILE,
        2 : resources.ALL_PROJECTS_FILE,
        3 : resources.RECURRING_FILE
    }, 
    {
        0 : resources.EVERYDAY_ARCHIVE,
        1 : resources.PROGRAMMING_ARCHIVE,
        2 : resources.FULL_ARCHIVE
    }
]

# Utility functions
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

def success_message():
    success_message = QMessageBox()
    success_message.setWindowTitle(SUCCESS_WINDOW_TITLE)
    success_message.setText(f"{SUCCESS_TEXT}")
    success_message.setStandardButtons(QMessageBox.Ok)
    success_message.exec()
