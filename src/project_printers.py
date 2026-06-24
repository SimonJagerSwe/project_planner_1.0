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
    if sub_tab == 3:
        for project in projects:
            name = project["Task name"]
            frequency = project["Task frequency"]
            notes = project["Task notes"]
            full_project = f"{name}\n{frequency}\n{notes}\n"
            print(full_project)
    else:
        for project in projects:
            name = project["Project name"]
            start = project["Project start date"]
            end = project["Project end date"]
            if "Language(s)" in project:
                language = project["Language(s)"]
            if "GitHub link" in project:
                link = project["GitHub link"]
            notes = project["Project notes"]
            progress = project["Project progress"]
            status = project["Project status"]
            if "Language(s)" in project:
                full_project = f"{name}\n{start}\n{end}\n{language}\n{link}\n{notes}\n{progress}\n{status}\n"
            else:
                full_project = f"{name}\n{start}\n{end}\n{notes}\n{progress}\n{status}\n"
            print(full_project)
