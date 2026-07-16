########## Writers ##########
# Imports
import json
import resources


# Project file creator
def project_data(ui, project_type, current_dialog, main_window, write_type):
    # Create everyday project
    if project_type == "everyday":
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
    elif project_type == "programming":
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

    # Write new file
    writer(project, project_type, write_type)

    # Return to main menu
    if current_dialog and main_window:
        resources.return_to_main_clicked(current_dialog, main_window)

# Project writer
def writer(project, project_type, write_type):
    # Determine which project file to write to
    if project_type == "everyday":
        projects_file = resources.EVERYDAY_FILE
    elif project_type == "programming":
        projects_file = resources.PROGRAMING_FILE
    else:
        projects_file = resources.RECURRING_FILE

    # Read current project type projects
    try:
        with open(projects_file, "r") as file:
            current_type_projects = json.load(file)
            print(f"Current projects of {project_type} type:\n{current_type_projects}\n\n")
            print(current_type_projects)
            current_type_projects.append(project)
    except:
        print("Project type file empty")
        current_type_projects = []
        current_type_projects.append(project)
    
    print(f"Updated projects of {project_type} type:\n{current_type_projects}\n\n")
    
    # Read full projects file
    try:
        with open(resources.ALL_PROJECTS_FILE, "r") as file:
            all_projects = json.load(file)
            print(f"All current projects:\n{all_projects}\n\n")
            all_projects.append(project)
    except:
        print("All projects file empty")
        all_projects = []
        all_projects.append(project)
    
    # Write to project type file
    try:
        with open(projects_file, "w") as file:
            json.dump(current_type_projects, file)
    except:
        print(f"Unexpected error while writing to {project_type} project file occurred")
    # Write to full project file
    if "Task frequency" not in project:
        try:
            with open(resources.ALL_PROJECTS_FILE, "w") as file:
                json.dump(all_projects, file)
        except:
            print("Unexpected error while writing to full project file occurred")

    # Trigger success message
    if write_type == "new":
        resources.success_message_main()
    else:
        resources.success_message_viewer()
    