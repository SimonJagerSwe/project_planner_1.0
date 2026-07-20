########## Project printers ##########
# Imports
import resources

from loader import load_file

# Print contents of file obtained from loaded projects file
def print_projects(ui, top_tab, sub_tab):
    # Clear ui on tab switch, otherwise all projects will be printed multiple times
    ui.everydayProjects.clear()
    ui.programmingProjects.clear()
    ui.recurringWeekly.clear()
    ui.recurringBi.clear()
    ui.recurringOther.clear()
    ui.allProjects.clear()

    # Open project file based on tab indices
    project_file = resources.tab_handler[top_tab][sub_tab]
    projects = load_file(project_file)
    

    # Print active projects
    if top_tab == 0:
    # Print all projects
        if sub_tab == 2:
            everyday_projects = load_file(resources.EVERYDAY_FILE)
            for project in everyday_projects:
                name = project["Project name"]
                start = project["Project start"]
                end = project["Project end"]
                notes = project["Project notes"]
                progress = project["Project progress"]
                status = project["Project status"]
                everyday_project = f"Project name:\t{name}\nStart date:\t\t{start}\nEnd date:\t\t{end}\nProject notes:\t{notes}\nProject progress:\t{progress}\nProject status:\t{status}\n"
                ui.allProjects.addItem(everyday_project)
            programming_projects = load_file(resources.PROGRAMMING_FILE)
            for project in programming_projects:
                name = project["Project name"]
                start = project["Project start"]
                end = project["Project end"]
                language = project["Language(s)"]
                link = project["GitHub link"]
                notes = project["Project notes"]
                progress = project["Project progress"]
                status = project["Project status"]
                programming_project = f"Project name:\t{name}\nStart date:\t\t{start}\nEnd date:\t\t{end}\nLanguage(s):\t\t{language}\nGitHub link:\t\t{link}\nProject notes:\t{notes}\nProject progress:\t{progress}\nProject status:\t{status}\n"
                ui.allProjects.addItem(programming_project)
        # Print precurring tasks depending on frequency
        elif sub_tab == 3:
            for project in projects:
                name = project["Task name"]
                frequency = project["Task frequency"]
                notes = project["Task notes"]
                full_project = f"Task name:\t\t{name}\nTask notes:\t\t{notes}\n"
                if frequency == "Weekly":
                    ui.recurringWeekly.addItem(full_project)
                elif frequency == "Bi-weekly":
                    ui.recurringBi.addItem(full_project)
                else:
                    ui.recurringOther.addItem(full_project)
        # Print everyday or programming projects, based on whether programming-specific variables exist
        else:
            for project in projects:
                if "Project name" not in project:
                    continue
                name = project["Project name"]
                start = project["Project start"]
                end = project["Project end"]
                if "Language(s)" in project:
                    language = project["Language(s)"]
                if "GitHub link" in project:
                    link = project["GitHub link"]
                notes = project["Project notes"]
                progress = project["Project progress"]
                status = project["Project status"]

                if "Language(s)" in project:
                    full_project = f"Project name:\t{name}\nStart date:\t\t{start}\nEnd date:\t\t{end}\nLanguage(s):\t\t{language}\nGitHub link:\t\t{link}\nProject notes:\t{notes}\nProject progress:\t{progress}\nProject status:\t{status}\n"
                    ui.programmingProjects.addItem(full_project)
                else:
                    full_project = f"Project name:\t{name}\nStart date:\t\t{start}\nEnd date:\t\t{end}\nProject notes:\t{notes}\nProject progress:\t{progress}\nProject status:\t{status}\n"
                    ui.everydayProjects.addItem(full_project)
    # Print archives                
    else:
        if sub_tab == 0:
            ...