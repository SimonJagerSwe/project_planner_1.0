########## Archive handlers ##########
# Imports
import project_deleter, resources, writers


# Archiving function
def archive_project(project, project_type, viewer, main_window):
    print("Archiving project...")
    print(f"Project:\n{project}\n")
    print(f"Project type:\n{project_type}\n")
    unpacked_project = resources.project_parser(project, project_type)
    project_deleter.delete_project(unpacked_project, project_type, viewer, main_window, "archive")
    writers.writer(unpacked_project, project_type, viewer, main_window, "archive")
