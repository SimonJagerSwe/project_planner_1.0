########## Writers ##########
# Imports
import json

import resources, button_handler

from PySide6.QtCore import QDate

# Write everyday project
def w_e_project(ui, current_dialog=None, main_window=None):
    # Try to open file with current everyday projects and load into projects list
    try:
        with open(resources.EVERYDAY_FILE, "r") as file:
            projects = json.load(file)
            print(projects)

    # If there are no active everyday projects, initialise empty projects list
    except:
        print("No current everyday projects found")
        projects = []

    # Read project parameters from gui
    name = ui.everydayName.text()
    start = ui.everydayStart.date().toString("yyyy-MM-dd")
    finish = ui.everydayFinish.date().toString("yyyy-MM-dd")
    notes = ui.everydayNotes.text()
    percent = ui.everydayProgressPercent.text()
    status = ui.everydayStatus.currentText()

    # Store project parameters in project dict
    e_project = {
        "Project name" : name,
        "Project start date" : start,
        "Project end date" : finish,
        "Project notes" : notes,
        "Project progress" : percent,
        "Project status" : status
    }
    print(f"Project variables to save:\n{e_project}")

    # Append new project to the end of the everyday projects file
    projects.append(e_project)
    print(projects)

    # Write updated everyday projects file
    with open(resources.EVERYDAY_FILE, "w") as file:
        json.dump(projects, file)

    # Display message to let user know that the everyday project has been saved
    resources.success_message("Everyday")

    # Return to main menu
    if current_dialog and main_window:
        button_handler.return_to_main_clicked(current_dialog, main_window)
    

# Edit everyday project
def e_e_project(ui):
    print("Editing everyday project...")

# Clear everyday project input
def c_e_project(ui):
    print("Clearing everyday project...")
    ui.everydayName.setText("")
    ui.everydayStart.setDate(QDate.currentDate())
    ui.everydayFinish.setDate(QDate.currentDate())
    ui.everydayNotes.setText("")
    ui.everydayProgressSlider.setValue(0)
    ui.everydayProgressPercent.setText("0%")
    ui.everydayStatus.setCurrentText("Select project status")

# Delete everyday project
def d_e_project():
    print("Deleting everyday project...")

# Write programming project
def w_p_project(ui, current_dialog=None, main_window=None):
    # Try to open file with current programming projects and load into projects list
    try:
        with open(resources.PROGRAMING_FILE, "r") as file:
            projects = json.load(file)
            print(projects)

    # If there are no active everyday projects, initialise empty projects list
    except:
        print("No programming projects found")
        projects = []

    # Read project parameters from gui
    name = ui.programmingName.text()
    start = ui.programmingStart.date().toString("yyyy-MM-dd")
    finish = ui.programmingFinish.date().toString("yyyy-MM-dd")
    language = ui.languagesEdit.text()
    link = ui.githubEdit.text()
    notes = ui.programmingNotes.text()
    percent = ui.programmingProgressPercent.text()
    status = ui.programmingStatus.currentText()

    # Store project parameters in project dict
    p_project = {
        "Project name" : name,
        "Project start date" : start,
        "Project end dage" : finish,
        "Language(s)" : language,
        "GitHub link" : link,
        "Project notes" : notes,
        "Project progress" : percent,
        "Project status" : status
    }
    print(f"Project variables to save:\n{p_project}")

    # Append new project to the end of the programming projects file
    projects.append(p_project)
    print(projects)

    # Write updated programming projects file
    with open(resources.PROGRAMING_FILE, "w") as file:
        json.dump(projects, file)

    # Display message to let user know that the programming project has been saved
    resources.success_message("Programming")

    # Return to main menu
    if current_dialog and main_window:
        button_handler.return_to_main_clicked(current_dialog, main_window)


# Edit programming project
def e_p_project(ui):
    print("Editing programming project...")

# Clear programming project
def c_p_project(ui):
    print("Clearing programming project...")
    ui.programmingName.setText("")
    ui.programmingStart.setDate(QDate.currentDate())
    ui.programmingFinish.setDate(QDate.currentDate())
    ui.languagesEdit.setText("")
    ui.githubEdit.setText("")
    ui.programmingNotes.setText("")
    ui.programmingProgressSlider.setValue(0)
    ui.programmingProgressPercent.setText("0%")
    ui.programmingStatus.setCurrentText("Select project status")

# Delete programming project
def d_e_project():
    print("Deleting programming project...")

# Write recurring task
def w_r_task():
    print(f"Writing recurring task to {resources.RECURRING_FILE}")
    r_task = {

    }

# Clear recurring task
def c_r_task(ui):
    print("Clearing recurring task")
    ui.recurringName.setText("")
    ui.recurringFrequency.setCurrentText("Select frequency")
    ui.recurringNotes.setText("")
    
    
# Delete recurring task
def d_r_task():
    print("Deleting recurring task...")

# Write all projects
def w_a_projects():
    print(f"Writing project to {resources.ALL_PROJECTS_FILE}")
    a_projects = {

    }

# Write everyday archive
def w_e_archive():
    print(f"Writing everyday project to {resources.EVERYDAY_ARCHIVE}")
    e_archive = {

    }

# Write programming archive
def w_p_archive():
    print(f"Writing programming project to {resources.PROGRAMMING_ARCHIVE}")
    p_archive = {

    }

# Write full archive
def w_f_archive():
    print(f"Writing project to {resources.FULL_ARCHIVE}")
    f_archive = {

    }
