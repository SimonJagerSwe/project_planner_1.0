########## Project deleter ##########
# Imports
import json

import button_handler

from loader import load_file as loader
from resources import EVERYDAY_FILE, PROGRAMMING_FILE, RECURRING_FILE, project_parser


# Delete project from project type file, both for deletion and for editing
def delete_project(project, project_type, viewer, main_window, delete_type):
    current_project = project_parser(project, project_type)
    print(f"Project received by delete function:\n{project}\nProject type:\n{project_type}\nDelete type:\n{delete_type}\n")
    if project_type == "everyday":
        projects_file = EVERYDAY_FILE
    elif project_type == "programming":
        projects_file = PROGRAMMING_FILE
    elif project_type == "recurring":
        projects_file = RECURRING_FILE
    else:
        print("Unknown error")

    projects = loader(projects_file)
    print(f"Current projects:\n{projects}\n")
    try:
        projects.remove(current_project)
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
        