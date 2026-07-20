########## Archive handlers ##########
# Imports
import project_deleter, resources, writers

from PySide6.QtCore import QDate

# Archiving function
def archive_project(project, project_type, viewer, main_window):
    unpacked_project = resources.project_parser(project, project_type)
    print("Archiving project...")
    print(f"Project:\n{project}\n")
    print(f"Project type:\n{project_type}\n")
    print(f"Unpacked project:\n{unpacked_project}\n")
    print(f"Sending project to archive writer: {project}\n")
    complete = resources.complete_archive()
    if complete == "yes":
        print("Marking project as completed and archiving...")
        unpacked_project["Project progress"] = "100%"
        unpacked_project["Project status"] = "Completed"
        print(f"Completed project:\n{unpacked_project}\n")
    else:
        print("Archive project as is...")
    writers.writer(unpacked_project, project_type, viewer, main_window, "archive")
    print("Archiving step 1 - Write to archive file: Done")
    project_deleter.delete_project(project, project_type, viewer, main_window, "archive")
    print("Archiving step 2 - Delete from file: Done")
