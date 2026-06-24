########## Project printers ##########
# Imports
import resources

from loader import load_file

# Print contents of file obtained from loaded projects file
def print_projects(ui, top_tab, sub_tab):
    print(f"Receiving top tab: {top_tab}\nBottom tab: {sub_tab}\n")
    ui.everydayProjects.clear()
    ui.programmingProjects.clear()
    ui.recurringProjects.clear()
    project_file = resources.tab_handler[top_tab][sub_tab]
    projects = load_file(project_file)
    project_list = []
    if sub_tab == 3:
        for project in projects:
            name = project["Task name"]
            frequency = project["Task frequency"]
            notes = project["Task notes"]
            full_project = f"Task name:\t\t{name}\nTask frequency:\t{frequency}\nTask notes:\t\t{notes}\n"
            print(full_project)
            project_list.append(full_project)
            print(project_list)
            ui.recurringProjects.addItem(full_project)
    else:
        for project in projects:
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
            project_list.append(full_project)
            