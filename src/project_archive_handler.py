########## Archive handlers ##########
# Imports
import project_deleter, resources


# Archiving function
def archive_project(project, project_type, viewer, main_window):
    print("Archiving project...")
    print(f"Project:\n{project}\n")
    print(f"Project type:\n{project_type}\n")
    # project_deleter.delete_project(project, project_type, main_window, "archive")
