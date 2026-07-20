########## Writers ##########
# Imports
import json
import resources


# Project file creator
def project_data(ui, project_type):     # , current_dialog, main_window, write_type
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
    return project


# Project writer
def writer(project, project_type, current_dialog, main_window, write_type):
    print(f"Writing file using:\n{project}")
    print(f"Project type to write:\n{project_type}")
    print(f"Write type:\n{write_type}")
    if write_type != "archive":
        project = project_data(project, project_type)
    else:
        project = resources.project_parser(project, project_type)
    print(f"Project to write:\n{project}")

    # Determine if project should be written to project files or archive files
    if write_type == "new" or write_type == "edit":
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
        project.append(project)
        print(f"Updated projects list:\n{project_list}\n")

    # Write to target file/archive
    try:
        with open(target_file, "w") as file:
            print(f"Writing {project_list} to {target_file}...")
            json.dump(project_list, file)
    except:
        print(f"Writing {project_list} to {target_file} failed")

    # Write to full project files/archive files if not recurring    
    '''if "Task frequency" not in project:
        if write_type == "new" or write_type == "edit":
            full_file = resources.ALL_PROJECTS_FILE
        else:
            full_file = resources.FULL_ARCHIVE        
        try:
            with open(full_file, "w") as file:
                print(f"Writing {updated_list} to {target_file}...")
                json.dump(updated_list, file)
        except:
            print(f"Writing {updated_list} to {target_file} failed")'''
    
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


'''
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

    
'''