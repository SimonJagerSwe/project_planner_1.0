########## Archive handlers ##########
# Imports
import button_handler, project_deleter, resources, writers


# Archiving function
def archive_project(project, project_type, viewer, main_window, tab_state):
    unpacked_project = resources.project_parser(project, project_type)
    print("Archiving project...")
    print(f"Project:\n{project}\n")
    print(f"Project type:\n{project_type}\n")
    print(f"Unpacked project:\n{unpacked_project}\n")
    print(f"Sending project to archive writer:\n{project}\n")
    complete = resources.complete_archive()
    if complete == "yes":
        print("Marking project as completed and archiving...")
        unpacked_project["Project progress"] = "100%"
        unpacked_project["Project status"] = "Completed"
        print(f"Completed project:\n{unpacked_project}\n")
    else:
        print("Archiving project as is...")
    writers.writer(unpacked_project, project_type, viewer, main_window, "archive", return_to_main=False)
    print("Archiving step 1 - Write to archive file: Done")
    project_deleter.delete_project(project, project_type, viewer, main_window, "archive", tab_state)
    print("Archiving step 2 - Delete from file: Done")
    button_handler.project_viewer_clicked(main_window, tab_state["main_index"], tab_state["sub_index"])
