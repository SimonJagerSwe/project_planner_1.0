########## Button handler ##########
# Imports
import project_deleter, project_editors, project_archive_handler, resources, writers

from interface.ui_everyday import Ui_everydayProjectEditor
from interface.ui_new_project import Ui_addNewProject
from interface.ui_programming import Ui_programmingProjectEditor
from interface.ui_recurring import Ui_recurringProjectEditor
from interface.ui_tabs import Ui_Viewer
from project_printers import print_projects as printer

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
    view_archive.clicked.connect(lambda: project_viewer_clicked(main_window, 1))
    main_exit = main_window.findChild(QPushButton, "mainExit")
    main_exit.clicked.connect(lambda: resources.exit_clicked(main_window))
    
    # Drop down menu actions
    everyday_action = main_window.findChild(QAction, "actionAddEveryday")
    everyday_action.triggered.connect(lambda: everyday_project_clicked(None, main_window))
    programming_action = main_window.findChild(QAction, "actionAddProgramming")
    programming_action.triggered.connect(lambda: (programming_project_clicked(None, main_window)))
    projects_action = main_window.findChild(QAction, "actionProjects")
    projects_action.triggered.connect(lambda: (project_viewer_clicked(main_window)))
    archive_action = main_window.findChild(QAction, "actionArchive")
    archive_action.triggered.connect(lambda: (project_viewer_clicked(main_window)))
    exit_action = main_window.findChild(QAction, "actionExit")
    exit_action.triggered.connect(lambda: (resources.exit_clicked(main_window)))


# Add project menu
def add_project_clicked(main_window):
    print("Add project clicked!")
    add_project = QDialog(main_window)
    ui = Ui_addNewProject()
    ui.setupUi(add_project)
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
    ui.everydayStart.setDate(QDate.currentDate())
    ui.everydayFinish.setDate(QDate.currentDate())
    ui.everydayProgressSlider.valueChanged.connect(lambda value: 
        ui.everydayProgressPercent.setText(f"{value}%"))
    ui.everydaySave.clicked.connect(lambda: writers.project_data(ui, "everyday", everyday_dialog, main_window, "new"))
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
    ui.programmingStart.setDate(QDate.currentDate())
    ui.programmingFinish.setDate(QDate.currentDate())
    ui.programmingProgressSlider.valueChanged.connect(lambda value:
        ui.programmingProgressPercent.setText(f"{value}%"))
    ui.programmingSave.clicked.connect(lambda: writers.project_data(ui, "programming", programming_dialog, main_window, "new"))
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
    ui.saveRecurring.clicked.connect(lambda: writers.project_data(ui, "recurring", recurring_dialog, main_window, "new"))
    ui.clearRecurring.clicked.connect(lambda: resources.clear_input(ui))
    ui.returnToMainRecurring.clicked.connect(lambda: resources.return_to_main_clicked(recurring_dialog, main_window))
    ui.exitRecurring.clicked.connect(lambda: resources.exit_clicked(recurring_dialog))
    recurring_dialog.exec()
    main_window.show()


# View projects and archives
def project_viewer_clicked(main_window, top_idx, sub_idx):
    print("Loading viewer...")
    resources.selected_project = None
    main_window.close()
    viewer = QDialog(main_window)
    ui = Ui_Viewer()
    ui.setupUi(viewer)

    # Function to handle tab changes
    def tab_changed(top_tab, sub_tab):
        printer(ui, top_tab, sub_tab)
        resources.selected_project = None

    # Initialise tab index based on user selection
    ui.viewer.setCurrentIndex(top_idx)
    if ui.viewer.currentIndex() == 0:
        ui.projectTabs.setCurrentIndex(sub_idx)
    if ui.viewer.currentIndex() == 1:
        ui.archive.setCurrentIndex(sub_idx)
    
    # Print everyday projects to interface without having to select a tab first
    # to avoid user being greeted by an empty project view
    # tab_changed(ui.viewer.currentIndex(), 0)
    tab_changed(top_idx, sub_idx)

    # Use a clicked project to set an item to use
    # for editing, archiving or deleting
    def project_clicked(item):        
        resources.selected_project = item

    # Use set item to call the edit function
    def edit_clicked():
        if resources.selected_project is None:
            resources.no_project_selected()
        else:
            project_editors.edit_parser(resources.selected_project, viewer, main_window)

    def archive_clicked():
        if resources.selected_project is None:
            resources.no_project_selected()
        else:
            project_type = resources.parse_type(resources.selected_project)
            print(project_type)
            project_archive_handler.archive_project(resources.selected_project, project_type, viewer, main_window)
            archive = resources.archive_check(viewer)
            print(archive)

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
                project_deleter.delete_project(resources.selected_project, project_type, viewer, main_window, "delete")

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
    ui.viewer.currentChanged.connect(lambda: tab_changed(ui.viewer.currentIndex(), 0))
    ui.projectTabs.currentChanged.connect(lambda index: tab_changed(0, index))
    ui.archivedTabs.currentChanged.connect(lambda index: tab_changed(1, index))
    ui.editProject.clicked.connect(edit_clicked)
    ui.archiveProject.clicked.connect(lambda: archive_clicked())
    ui.deleteProject.clicked.connect(lambda: delete_clicked())
    ui.returnToMainProjects.clicked.connect(lambda: resources.return_to_main_clicked(viewer, main_window))
    ui.exitProjects.clicked.connect(lambda: resources.exit_clicked(viewer))
    ui.restoreArchived.clicked.connect(restore_project_clicked)
    ui.returnToMainArchive.clicked.connect(lambda: resources.return_to_main_clicked(viewer, main_window))
    ui.exitArchive.clicked.connect(lambda: resources.exit_clicked(viewer))
    viewer.exec()
    main_window.show()


# Placeholder functions

def restore_project_clicked():
    print("Restore project...")
