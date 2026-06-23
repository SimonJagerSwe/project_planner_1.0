########## Resources ##########
# Imports
import json
import os
import sys

import writers

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
SUCCESS_TEXT = "project saved successfully!"


# Utility functions
def success_message(type):
    success_message = QMessageBox()
    success_message.setWindowTitle(SUCCESS_WINDOW_TITLE)
    success_message.setText(f"{type} {SUCCESS_TEXT}")
    success_message.setStandardButtons(QMessageBox.Ok)
    success_message.exec()
