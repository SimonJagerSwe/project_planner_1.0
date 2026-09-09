########## Button handler ##########
# Imports
import project_archive_handler, resources

from interface.ui_everyday import Ui_everydayProjectEditor
from interface.ui_new_project import Ui_addNewProject
from interface.ui_programming import Ui_programmingProjectEditor
from interface.ui_recurring import Ui_recurringProjectEditor
from interface.ui_tabs import Ui_Viewer
from loader import load_file as loader
from project_deleter import delete_project as deleter
from project_editors import edit_parser as editor
from project_printers import print_projects as printer
from resources import VERSION
from writers import writer as writer

from PySide6.QtCore import QDate
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QDialog, QListWidget, QPushButton 


# Main menu buttons
def main_menu_buttons(main_window):
    # Regular buttons
    add_project = main_window.findChild(QPushButton, "addProject")
    add_project.clicked.connect(lambda: add_project_clicked(main_window))
    view_projects = main_window.findChild(QPushButton, "viewProjects")
    view_projects.clicked.connect(lambda: project_viewer_clicked(main_window, 0, 0))
    view_archive = main_window.findChild(QPushButton, "viewArchive")
    view_archive.clicked.connect(lambda: project_viewer_clicked(main_window, 1, 0))
    main_exit = main_window.findChild(QPushButton, "mainExit")
    main_exit.clicked.connect(lambda: resources.exit_clicked(main_window))
    
    # Drop down menu actions TODO
    everyday_action = main_window.findChild(QAction, "actionAddEveryday")
    everyday_action.triggered.connect(lambda: everyday_project_clicked(None, main_window))
    programming_action = main_window.findChild(QAction, "actionAddProgramming")
    programming_action.triggered.connect(lambda: (programming_project_clicked(None, main_window)))
    projects_action = main_window.findChild(QAction, "actionProjects")
    projects_action.triggered.connect(lambda: (project_viewer_clicked(main_window, 0, 0)))
    archive_action = main_window.findChild(QAction, "actionArchive")
    archive_action.triggered.connect(lambda: (project_viewer_clicked(main_window, 1, 0)))
    exit_action = main_window.findChild(QAction, "actionExit")
    exit_action.triggered.connect(lambda: (resources.exit_clicked(main_window)))


# Add project menu
def add_project_clicked(main_window):
    print("Add project clicked!")
    add_project = QDialog(main_window)
    ui = Ui_addNewProject()
    ui.setupUi(add_project)
    add_project.setWindowTitle(f"{VERSION} - Add project")
    ui.addEveryday.clicked.connect(lambda: everyday_project_clicked(add_project, main_window))
    ui.addProgramming.clicked.connect(lambda: programming_project_clicked(add_project, main_window))
    ui.addRecurring.clicked.connect(lambda: recurring_project_clicked(add_project, main_window))
    ui.returnToMainAddProject.clicked.connect(lambda: (resources.return_to_main_clicked(add_project, main_window)))
    ui.exitAddProject.clicked.connect(lambda: resources.exit_clicked(add_project))
    add_project.exec()


# Add everyday project
def everyday_project_clicked(current_dialog, main_window):
    print("Add everyday project clicked")
    if current_dialog is not None:
        current_dialog.close()
    main_window.close()
    everyday_dialog = QDialog(None)
    ui = Ui_everydayProjectEditor()
    ui.setupUi(everyday_dialog)
    everyday_dialog.setWindowTitle(f"{VERSION} - Add everyday project")
    ui.everydayStart.setDate(QDate.currentDate())
    ui.everydayFinish.setDate(QDate.currentDate())
    ui.everydayProgressSlider.valueChanged.connect(lambda value: 
        ui.everydayProgressPercent.setText(f"{value}%"))
    ui.everydaySave.clicked.connect(lambda: writer(ui, "everyday", everyday_dialog, main_window, "new"))
    ui.everydayClear.clicked.connect(lambda: resources.clear_input(ui))
    ui.everydayReturn.clicked.connect(lambda: resources.return_to_main_clicked(everyday_dialog, main_window))
    ui.everydayExit.clicked.connect(lambda: resources.exit_clicked(everyday_dialog))
    everyday_dialog.exec()
    main_window.show()


# Add programming project
def programming_project_clicked(current_dialog, main_window):
    print("Add programming project clicked")
    if current_dialog is not None:
        current_dialog.close()
    main_window.close()
    programming_dialog = QDialog(main_window)
    ui = Ui_programmingProjectEditor()
    ui.setupUi(programming_dialog)
    programming_dialog.setWindowTitle(f"{VERSION} - Add programming project")
    ui.programmingStart.setDate(QDate.currentDate())
    ui.programmingFinish.setDate(QDate.currentDate())
    ui.programmingProgressSlider.valueChanged.connect(lambda value:
        ui.programmingProgressPercent.setText(f"{value}%"))
    ui.programmingSave.clicked.connect(lambda: writer(ui, "programming", programming_dialog, main_window, "new"))
    ui.programmingClear.clicked.connect(lambda: resources.clear_input(ui))
    ui.programmingReturn.clicked.connect(lambda: resources.return_to_main_clicked(programming_dialog, main_window))
    ui.programmingExit.clicked.connect(lambda: resources.exit_clicked(programming_dialog))
    programming_dialog.exec()
    main_window.show()


# Add recurring project
def recurring_project_clicked(current_dialog, main_window):
    print("Add recurring project clicked")
    if current_dialog is not None:
        current_dialog.close()
    main_window.close()
    recurring_dialog = QDialog(main_window)
    ui = Ui_recurringProjectEditor()
    ui.setupUi(recurring_dialog)
    recurring_dialog.setWindowTitle(f"{VERSION} - Add recurring task")
    ui.saveRecurring.clicked.connect(lambda: writer(ui, "recurring", recurring_dialog, main_window, "new"))
    ui.clearRecurring.clicked.connect(lambda: resources.clear_input(ui))
    ui.returnToMainRecurring.clicked.connect(lambda: resources.return_to_main_clicked(recurring_dialog, main_window))
    ui.exitRecurring.clicked.connect(lambda: resources.exit_clicked(recurring_dialog))
    recurring_dialog.exec()
    main_window.show()


# View projects and archives
def project_viewer_clicked(main_window, top_idx=0, sub_idx=0):
    print("Loading viewer...")
    resources.selected_project = None
    main_window.close()
    viewer = QDialog(main_window)
    ui = Ui_Viewer()
    ui.setupUi(viewer)
    viewer.setWindowTitle(f"{VERSION} - View projects")
    tab_state = {
        "main_index" : top_idx,
        "sub_index" : sub_idx 
    }

    # Function to handle tab changes and store tab index values for function calls
    def tab_changed():
        top_idx = ui.viewer.currentIndex()
        if top_idx == 0:
            sub_idx = ui.projectTabs.currentIndex()
        else:
            sub_idx = ui.archivedTabs.currentIndex()
        print(f"Tab change executed:\nTop index: {top_idx}\nSub index: {sub_idx}\n")
        tab_state["main_index"] = top_idx
        tab_state["sub_index"] = sub_idx
        printer(ui, top_idx, sub_idx)
        resources.selected_project = None

    # Initialise tab index based on user selection
    ui.viewer.setCurrentIndex(tab_state["main_index"])
    if tab_state["main_index"] == 0:
        ui.projectTabs.setCurrentIndex(tab_state["sub_index"])
    else:
        ui.archivedTabs.setCurrentIndex(tab_state["sub_index"])
    # if ui.viewer.currentIndex() == 0:
    #     ui.projectTabs.setCurrentIndex(sub_idx)
    # if ui.viewer.currentIndex() == 1:
    #     ui.archivedTabs.setCurrentIndex(sub_idx)
    
    # Print everyday projects to interface without having to select a tab first
    # to avoid user being greeted by an empty project view
    tab_changed()

    # Use a clicked project to set an item to use
    # for editing, archiving or deleting
    def project_clicked(item):
        resources.selected_project = item

    # Use set item to call the edit function
    def edit_clicked():
        if resources.selected_project is None:
            resources.no_project_selected()
        else:
            editor(resources.selected_project, viewer, main_window, tab_state)


    # Use a set project type to create new project of same type
    def new_clicked():
        top_idx = tab_state["main_index"]
        sub_idx = tab_state["sub_index"]

        print(f"Main tab:\n{top_idx}\nSub tab:\n{sub_idx}\n")


    # Use set item to call the archive function
    def archive_clicked():
        if resources.selected_project is None:
            resources.no_project_selected()
        else:
            project_type = resources.parse_type(resources.selected_project)
            print(project_type)
            archive = resources.archive_check(viewer)
            print(archive)
            if archive == "archive":
                project_archive_handler.archive_project(resources.selected_project, project_type, viewer, main_window, tab_state)

    # Use set item to call the delete function
    def delete_clicked():
        if resources.selected_project is None:
            resources.no_project_selected()
        else:
            print(resources.selected_project.text())
            project_type = resources.parse_type(resources.selected_project)
            print(project_type)
            delete = resources.safety_check(viewer)
            print(delete)
            if delete == "delete":
                deleter(resources.selected_project, project_type, viewer, main_window, "delete", tab_state)

    # Use set item to set recurring task status to done
    def recurring_done(task):
        print(f"Setting task status to done for:\n{task.text()}\n")
        project = resources.project_parser(task, "recurring")
        print(f"Task after parsing:\n{project}\n")
        deleter(project, "recurring", viewer, main_window, "edit")
        print("Project deleted from recurring file\n")
        project["Task status"] = True
        print(f"Task after altering status:\n{project}\n")        
        writer(project, "recurring", viewer, main_window, "edit")
        print("Project status set to done and saved!\n")

    # Reset single recurring task status
    def recurring_reset_single(task):
        print(f"Setting task status to done for:\n{task.text()}\n")
        project = resources.project_parser(task, "recurring")
        print(f"Task after parsing:\n{project}\n")
        deleter(project, "recurring", viewer, main_window, "edit")
        print("Project deleted from recurring file\n")
        project["Task status"] = False
        print(f"Task after altering status:\n{project}\n")
        writer(project, "recurring", viewer, main_window, "reset")
        print("Project status set to done and saved!\n")

    # Reset full category of recurring tasks
    def recurring_reset_group(category):
        print(f"Setting {category} tasks to not done")
        projects = loader(resources.RECURRING_FILE)
        project_list = []
        # Reset all weekly tasks
        for project in projects:
            print(project["Task frequency"])
            if project["Task frequency"] == category:
                print(f"{category} task found")
                if project["Task status"] == True:
                    print("Done task detected, resetting")
                    project["Task status"] = False
                    print(f"Updated project:\n{project}\n")
                print(f"Task status: {project["Task status"]}")
            project_list.append(project)
        print(f"Reset projects list to write to recurring file:\n{project_list}\n")
        writer(project_list, "recurring", viewer, main_window, "reset all")
        print(f"{category} tasks reset")
        

    # Logic for project selection
    recurring_list = [ui.recurringBi, ui.recurringOther, ui.recurringWeekly]
    for list_item in [
        ui.everydayProjects,
        ui.programmingProjects,
        ui.allProjects,
        ui.recurringBi,
        ui.recurringOther,
        ui.recurringWeekly
    ]:
        # If the user is selecting a recurring task
        # make sure to clear other fields to only use one item
        if list_item in recurring_list:
            for tab in recurring_list:
                tab.setSelectionMode(QListWidget.SingleSelection)

            def clear_other_recurring(clicked_item):
                current_item = clicked_item.listWidget()
                for item in recurring_list:
                    if item is not current_item:
                        item.clearSelection()

            for item in recurring_list:
                item.itemClicked.connect(clear_other_recurring)
            list_item.itemClicked.connect(project_clicked)

        # If the item is everyday or programming
        # ignore above clearing
        else:
            list_item.itemClicked.connect(project_clicked)

    # Action connections etc.
    # ui.viewer.currentChanged.connect(lambda: tab_changed(ui.viewer.currentIndex(), 0))
    ui.viewer.currentChanged.connect(lambda index: tab_changed())
    # ui.projectTabs.currentChanged.connect(lambda index: tab_changed(0, index))
    ui.projectTabs.currentChanged.connect(lambda index: tab_changed())
    # ui.archivedTabs.currentChanged.connect(lambda index: tab_changed(1, index))
    ui.archivedTabs.currentChanged.connect(lambda index: tab_changed())
    # ui.newProject.clicked.connect(lambda sub_idx: new_clicked(sub_idx))
    ui.newProject.clicked.connect(new_clicked)
    ui.editProject.clicked.connect(edit_clicked)
    ui.archiveProject.clicked.connect(lambda: archive_clicked())
    ui.deleteProject.clicked.connect(delete_clicked)
    ui.returnToMainProjects.clicked.connect(lambda: resources.return_to_main_clicked(viewer, main_window))
    ui.exitProjects.clicked.connect(lambda: resources.exit_clicked(viewer))
    ui.weeklyDone.clicked.connect(lambda: recurring_done(resources.selected_project))
    ui.weeklyResetTask.clicked.connect(lambda: recurring_reset_single(resources.selected_project))
    ui.weeklyResetAll.clicked.connect(lambda : recurring_reset_group("Weekly"))
    ui.biDone.clicked.connect(lambda: recurring_done(resources.selected_project))
    ui.biResetTask.clicked.connect(lambda: recurring_reset_single(resources.selected_project))
    ui.biResetAll.clicked.connect(lambda : recurring_reset_group("Bi-weekly"))
    ui.otherDone.clicked.connect(lambda: recurring_done(resources.selected_project))
    ui.otherReset.clicked.connect(lambda: recurring_reset_single(resources.selected_project))
    ui.restoreArchived.clicked.connect(restore_project_clicked)
    ui.returnToMainArchive.clicked.connect(lambda: resources.return_to_main_clicked(viewer, main_window))
    ui.exitArchive.clicked.connect(lambda: resources.exit_clicked(viewer))
    viewer.exec()
    main_window.show()

# Placeholder functions
def restore_project_clicked():
    print("Restore project...")
