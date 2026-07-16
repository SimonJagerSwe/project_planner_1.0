########## Project deleter ##########
# Imports
import json

import button_handler

from loader import load_file as loader
from resources import ALL_PROJECTS_FILE, EVERYDAY_FILE, PROGRAMMING_FILE, RECURRING_FILE


# Delete project from project type file, both for deletion and for editing
def delete_project(project, project_type, viewer, main_window, delete_type):
    print(project, project_type)
    print(delete_type)
    print(f"Project in delete function: {project}")
    print(f"Project type in delete function: {project_type}")
    if project_type == "everyday":
        projects_file = EVERYDAY_FILE
    elif project_type == "programming":
        projects_file = PROGRAMMING_FILE
    elif project_type == "recurring":
        projects_file = RECURRING_FILE
    else:
        print("Unknown error")

    if project_type != "recurring":        
        all_projects = loader(ALL_PROJECTS_FILE)
        try:
            all_projects.remove(project)
            print(f"Full projects after removal:\n{all_projects}\n")
            with open(ALL_PROJECTS_FILE, "w") as file:
                json.dump(all_projects, file)
        except:
            print("Project not present in full projects")

    projects = loader(projects_file)
    print(f"Current projects:\n{projects}\n")
    try:
        projects.remove(project)
        print(f"Selected projects type after removal:\n{projects}")
        with open (projects_file, "w") as file:
            json.dump(projects, file)
    except:
        print("Project not present in selected projects type")

    if viewer is not None:
        viewer.close()

    if delete_type == "delete":
        if project_type == "everyday":
            button_handler.project_viewer_clicked(main_window, 0, 0)
        elif project_type == "programming":
            button_handler.project_viewer_clicked(main_window, 0, 1)
        else:
            button_handler.project_viewer_clicked(main_window, 0, 3)
        