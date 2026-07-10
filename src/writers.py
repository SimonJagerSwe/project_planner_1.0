########## Writers ##########
# Imports
import json

import resources

from loader import load_file

from PySide6.QtCore import QDate


# Project writer
def writer(ui, projects_file, current_dialog=None, main_window=None):
    projects = load_file(projects_file)
    all_projects = load_file(resources.ALL_PROJECTS_FILE)
    print(f"Working file:\n{projects_file}\n\n")
    print(f"Projects in file:\n{projects}\n\n")

    # Create everyday project
    if projects_file == resources.EVERYDAY_FILE:
        name = ui.everydayName.text()
        start = ui.everydayStart.date().toString("yyyy-MM-dd")
        finish = ui.everydayFinish.date().toString("yyyy-MM-dd")
        notes = ui.everydayNotes.text()
        percent = ui.everydayProgressPercent.text()
        status = ui.everydayStatus.currentText()
        project = {
            "Project name" : name,
            "Project start" : start,
            "Project end" : finish,
            "Project notes" : notes,
            "Project progress" : percent,
            "Project status" : status
        }
    
    # Create programming project
    elif projects_file == resources.PROGRAMING_FILE:
        name = ui.programmingName.text()
        start = ui.programmingStart.date().toString("yyyy-MM-dd")
        finish = ui.programmingFinish.date().toString("yyyy-MM-dd")
        language = ui.languagesEdit.text()
        link = ui.githubEdit.text()
        notes = ui.programmingNotes.text()
        percent = ui.programmingProgressPercent.text()
        status = ui.programmingStatus.currentText()
        project = {
            "Project name" : name,
            "Project start" : start,
            "Project end" : finish,
            "Language(s)" : language,
            "GitHub link" : link,
            "Project notes" : notes,
            "Project progress" : percent,
            "Project status" : status
        }

    # Create recurring task
    else:
        name = ui.recurringName.text()
        frequency = ui.recurringFrequency.currentText()
        notes = ui.recurringNotes.text()
        project = {
            "Task name" : name,
            "Task frequency" : frequency,
            "Task notes" : notes
        }

    print(f"Project to be added:\n{project}\n\n")
    projects.append(project)
    all_projects.append(project)
    print(f"Updated projects file:\n{projects}\n\n")


    # Write updated projects file
    with open(projects_file, "w") as file:
        json.dump(projects, file)
    with open(resources.ALL_PROJECTS_FILE, "w") as file:
        json.dump(all_projects, file)
    resources.success_message()

    # Return to main menu
    if current_dialog and main_window:
        resources.return_to_main_clicked(current_dialog, main_window)
