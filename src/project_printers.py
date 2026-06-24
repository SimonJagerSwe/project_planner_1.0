########## Project printers ##########
# Imports
import json

import resources

from loader import load_file



# Print contents of file obtained from loaded projects file
def print_projects(top_tab, sub_tab):
    print(f"Receiving top tab: {top_tab}\nBottom tab: {sub_tab}\n")
    project_file = resources.tab_handler[top_tab][sub_tab]
    projects = load_file(project_file)
    # print(projects)
    if sub_tab == 0:
        for project in projects:
            name = project["Project name"]
            start = project["Project start date"]
            end = project["Project end date"]
            notes = project["Project notes"]
            progress = project["Project progress"]
            status = project["Project status"]
            full_project = f"{name}\n{start}\n{end}\n{notes}\n{progress}\n{status}\n"
            print(full_project)

    elif sub_tab == 1:
        for project in projects:
            name = project["Project name"]
            start = project["Project start date"]
            end = project["Project end date"]
            language = project["Language(s)"]
            link = project["GitHub link"]
            notes = project["Project notes"]
            progress = project["Project progress"]
            status = project["Project status"]
            full_project = f"{name}\n{start}\n{end}\n{language}\n{link}\n{notes}\n{progress}\n{status}\n"
            print(full_project)
