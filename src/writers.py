########## Writers ##########
# Imports
import json
import resources


# Project file creator
def project_data(ui, project_type):
    print("Writing project data...")
    print(f"Ui fetched: {ui}")
    print(project_type)

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
        print(f"Everyday project for printing:\n{project}\n")
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
        print(f"Programming project for printing:\n{project}\n")
    # Create recurring task
    else:
        # This receives a new or edited recurring task
        if type(ui) != dict:
            name = ui.recurringName.text()
            frequency = ui.recurringFrequency.currentText()
            notes = ui.recurringNotes.text()
            status = False  # Never printed, only to use for status check
            project = {
                "Task name" : name,
                "Task frequency" : frequency,
                "Task notes" : notes,
                "Task status" : status
            }
        # This is only in effect when marking a recurring task as done or resetting
        else:
            project = ui
        print(f"Recurring task for printing:\n{project}\n")
    return project


# Project writer
def writer(project, project_type, current_dialog, main_window, write_type):
    print(f"Writing file using:\n{project}\n")
    print(f"Project type to write:\n{project_type}\n")
    print(f"Write type:\n{write_type}\n")
    # This is for resetting recurring task statuses
    if write_type == "reset":
        target_file = resources.RECURRING_FILE
        project_list = []
        for task in project:
            project_list.append(task)
    else:
        if write_type == "new" or write_type == "edit":
            project = project_data(project, project_type)
        print(f"Project to write:\n{project}\n")

        # Determine if project should be written to project files or archive files
        if write_type == "new" or write_type == "edit" or write_type == "reset":
            print("Writing project to current project files")
            # Determine what project file to write to
            if project_type == "everyday":
                target_file = resources.EVERYDAY_FILE
            elif project_type == "programming":
                target_file = resources.PROGRAMMING_FILE
            elif project_type == "recurring":
                target_file = resources.RECURRING_FILE
            else:
                print("Unknown error occurred")
        # Determine which archive file to write to
        else:
            if project_type == "everyday":
                target_file = resources.EVERYDAY_ARCHIVE
            elif project_type == "programming":
                target_file = resources.PROGRAMMING_ARCHIVE
            else:
                print("Unknown error occurred")

        # Read target file
        try:
            with open(target_file, "r") as file:
                project_list = json.load(file)
                print(f"File loaded\nProjects found:\n{project_list}\n")
                project_list.append(project)
                print(f"Updated projects list:\n{project_list}\n")
        except:
            print("Project file empty or not found")
            project_list = []
            project_list.append(project)
            print(f"Updated projects list:\n{project_list}\n")

    # Write to target file/archive
    try:
        with open(target_file, "w") as file:
            print(f"Writing {project_list} to {target_file}...")
            json.dump(project_list, file)
    except:
        print(f"Writing {project_list} to {target_file} failed")
    
    # Return to main menu
    if current_dialog and main_window:
        resources.return_to_main_clicked(current_dialog, main_window)

    # Trigger success message
    if write_type == "new":
        resources.success_message_main()
    elif write_type == "edit":
        resources.success_message_viewer()
    else:
        resources.success_message_archive()
