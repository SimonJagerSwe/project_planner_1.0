########## Archive handlers ##########
# Imports
import project_deleter, resources, writers


# Archiving function
def archive_project(project, project_type, viewer, main_window):
    print("Archiving project...")
    print(f"Project:\n{project}\n")
    print(f"Project type:\n{project_type}\n")
    project_deleter.delete_project(project, project_type, viewer, main_window, "archive")
    print("Archiving step 1 - Delete from file: Done")
    print(f"Sending project to archive writer: {project}\n")
    writers.writer(project, project_type, viewer, main_window, "archive")
    print("Archiving step 2 - Write to archive file: Done")
