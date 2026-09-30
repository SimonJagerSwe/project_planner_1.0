########## Project printers ##########
# Imports
import resources

from loader import load_file

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QListWidgetItem


def add_project_item(list_widget, text, project, id_key="Project ID"):
    item = QListWidgetItem(text)
    item.setData(Qt.ItemDataRole.UserRole, project[id_key])
    list_widget.addItem(item)
    return item


# Clear tab in order to populate it with the correct projects
def clear_target_tab(ui, top_tab, sub_tab):
    if top_tab == 0:
        if sub_tab == 2:
            ui.allProjects.clear()
        elif sub_tab == 3:
            ui.recurringWeekly.clear()
            ui.recurringBi.clear()
            ui.recurringOther.clear()
        else:
            ui.everydayProjects.clear()
            ui.programmingProjects.clear()
    else:
        if sub_tab == 2:
            ui.fullArchive.clear()
        else:
            ui.everydayArchive.clear()
            ui.programmingArchive.clear()


# Print contents of file obtained from loaded projects file
def print_projects(ui, top_tab, sub_tab):
    # Clear ui on tab switch, otherwise all projects will be printed multiple times
    clear_target_tab(ui, top_tab, sub_tab)

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
                # ui.allProjects.addItem(everyday_project)
                add_project_item(ui.allProjects, everyday_project, project)
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
                # ui.allProjects.addItem(programming_project)
                add_project_item(ui.allProjects, programming_project, project)

        # Print recurring tasks depending on frequency
        elif sub_tab == 3:
            for project in projects:
                print(f"Recurring task:\n{project}\n")
                name = project["Task name"]
                frequency = project["Task frequency"]
                notes = project["Task notes"]
                full_project = f"Task name:\t\t{name}\nTask notes:\t\t{notes}\n"
                # list_item = QListWidgetItem(full_project)
                
                # if project["Task status"] == True:
                #     list_item.setBackground(QColor("#87d489"))
                if frequency == "Weekly":
                    # ui.recurringWeekly.addItem(list_item)
                    target_list = ui.recurringWeekly
                elif frequency == "Bi-weekly":
                    # ui.recurringBi.addItem(list_item)
                    target_list = ui.recurringBi
                else:
                    # ui.recurringOther.addItem(list_item)
                    target_list = ui.recurringOther

                list_item = add_project_item(
                    target_list,
                    full_project,
                    project,
                    id_key="Task ID"
                    )

                if project["Task status"]:
                    list_item.setBackground(QColor("#87d489"))
                    

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
                    # ui.programmingProjects.addItem(full_project)
                    add_project_item(ui.programmingProjects, full_project, project)
                else:
                    full_project = f"Project name:\t{name}\nStart date:\t\t{start}\nEnd date:\t\t{end}\nProject notes:\t{notes}\nProject progress:\t{progress}\nProject status:\t{status}\n"
                    # ui.everydayProjects.addItem(full_project)
                    add_project_item(ui.everydayProjects, full_project, project)
    # Print archives                
    else:
        # Print full archive
        if sub_tab == 2:
            everyday_projects = load_file(resources.EVERYDAY_ARCHIVE)
            for project in everyday_projects:
                name = project["Project name"]
                start = project["Project start"]
                end = project["Project end"]
                notes = project["Project notes"]
                progress = project["Project progress"]
                status = project["Project status"]
                everyday_project = f"Project name:\t{name}\nStart date:\t\t{start}\nEnd date:\t\t{end}\nProject notes:\t{notes}\nProject progress:\t{progress}\nProject status:\t{status}\n"
                # ui.fullArchive.addItem(everyday_project)
                add_project_item(ui.fullArchive, everyday_project, project)
            programming_projects = load_file(resources.PROGRAMMING_ARCHIVE)
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
                # ui.fullArchive.addItem(programming_project)
                add_project_item(ui.fullArchive, programming_project, project)
        # Print individual archive types
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
                    # ui.programmingArchive.addItem(full_project)
                    add_project_item(ui.programmingArchive, full_project, project)
                else:
                    full_project = f"Project name:\t{name}\nStart date:\t\t{start}\nEnd date:\t\t{end}\nProject notes:\t{notes}\nProject progress:\t{progress}\nProject status:\t{status}\n"
                    # ui.everydayArchive.addItem(full_project)
                    add_project_item(ui.everydayArchive, full_project, project)
