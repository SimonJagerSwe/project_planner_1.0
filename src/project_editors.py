########## Project editors ##########
# Imports
import loader


def edit_project(ui, project):
    print(f"Project to edit:\n{project.text()}")
    if "Language(s)" in project.text():
        print("Programming project, reading programming file...\n")
    elif "Task frequency" in project.text():
        print("Recurring task, reading tasks file...\n")
    else:
        print("Everyday project, reading everyday file...\n")

'''
def edit_everyday():
    print("Editing everyday...")


def edit_programming():
    print("Editing programming...")


def edit_recurring():
    print("Editing recurring project...")
'''
