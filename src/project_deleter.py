########## Project deleter ##########
# Imports
import json

from loader import load_file as loader
from resources import ALL_PROJECTS_FILE, EVERYDAY_FILE, PROGRAMING_FILE, RECURRING_FILE


# Delete project from project type file, both for deletion and for editing
def delete_project(project, type):
    print(f"Project for deletion:\n{project}")
    if type == "everyday":
        projects_file = EVERYDAY_FILE
    elif type == "programming":
        projects_file = PROGRAMING_FILE
    else:
        projects_file = RECURRING_FILE

    projects = loader(projects_file)
    print(f"Current projects:\n{projects}\n")
    try:
        projects.remove(project)
        print(f"Selected projects type after removal:\n{projects}")
    except:
        print("Project not present in selected projects type")
    
    if "Task frequency" not in project:        
        all_projects = loader(ALL_PROJECTS_FILE)
        try:
            all_projects.remove(project)
            print(f"Full projects after removal:\n{all_projects}\n")
            with open(ALL_PROJECTS_FILE, "w") as file:
                json.dump(all_projects, file)
        except:
            print("Project not present in full projects")

    with open (projects_file, "w") as file:
        json.dump(projects, file)
        