########## Button handler ##########
# Imports
import sys

import resources, writers

from interface.ui_everyday import Ui_everydayProjectEditor
from interface.ui_new_project import Ui_addNewProject
from interface.ui_programming import Ui_programmingProjectEditor
from interface.ui_recurring import Ui_recurringProjectEditor
from interface.ui_tabs import Ui_Viewer
from project_printers import print_projects as printer

from PySide6.QtCore import QDate
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QDialog, QMessageBox, QPushButton


##### Universal buttons #####
# Return to main menu
def return_to_main_clicked(current_dialog, main_window):
    print("Return to main menu clicked")
    if current_dialog is not None:
        current_dialog.close()
    main_window.show()
    main_window.setEnabled(True)

# Exit program
def exit_clicked(parent=None):
    print("Exiting program...")
    close = QMessageBox.question(
        parent, 
        "Confirm exit", 
        "Are you sure you want to quit?",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        QMessageBox.StandardButton.No
        )
    if close == QMessageBox.StandardButton.Yes:
        sys.exit()
    else:
        print("Returning to previous menu")


##### Non-universal buttons #####
# Main menu buttons
def main_menu_buttons(main_window):
    # Regular buttons
    add_project = main_window.findChild(QPushButton, "addProject")
    add_project.clicked.connect(lambda: add_project_clicked(main_window))
    view_projects = main_window.findChild(QPushButton, "viewProjects")
    view_projects.clicked.connect(lambda: project_viewer_clicked(main_window, 0))
    view_archive = main_window.findChild(QPushButton, "viewArchive")
    view_archive.clicked.connect(lambda: project_viewer_clicked(main_window, 1))
    main_exit = main_window.findChild(QPushButton, "mainExit")
    main_exit.clicked.connect(lambda: exit_clicked(main_window))
    
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
    exit_action.triggered.connect(lambda: (exit_clicked(main_window)))


# Add project menu
def add_project_clicked(main_window):
    print("Add project clicked!")
    add_project = QDialog(main_window)
    ui = Ui_addNewProject()
    ui.setupUi(add_project)
    ui.addEveryday.clicked.connect(lambda: everyday_project_clicked(add_project, main_window))
    ui.addProgramming.clicked.connect(lambda: programming_project_clicked(add_project, main_window))
    ui.addRecurring.clicked.connect(lambda: recurring_project_clicked(add_project, main_window))
    ui.returnToMainAddProject.clicked.connect(lambda: (return_to_main_clicked(add_project, main_window)))
    ui.exitAddProject.clicked.connect(lambda: exit_clicked(add_project))
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
    # ui.everydaySave.clicked.connect(lambda: writers.w_e_project(ui, everyday_dialog, main_window))
    ui.everydaySave.clicked.connect(lambda: writers.writer(ui, resources.EVERYDAY_FILE, everyday_dialog, main_window))
    ui.everydayClear.clicked.connect(lambda: writers.clear_input(ui))
    ui.everydayReturn.clicked.connect(lambda: return_to_main_clicked(everyday_dialog, main_window))
    ui.everydayExit.clicked.connect(lambda: exit_clicked(everyday_dialog))
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
    # ui.programmingSave.clicked.connect(lambda: writers.w_p_project(ui, programming_dialog, main_window))
    ui.programmingSave.clicked.connect(lambda: writers.writer(ui, resources.PROGRAMING_FILE, programming_dialog, main_window))
    ui.programmingClear.clicked.connect(lambda: writers.c_p_project(ui))
    ui.programmingReturn.clicked.connect(lambda: return_to_main_clicked(programming_dialog, main_window))
    ui.programmingExit.clicked.connect(lambda: exit_clicked(programming_dialog))
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
    # ui.saveRecurring.clicked.connect(lambda: writers.w_r_task(ui, recurring_dialog, main_window))
    ui.saveRecurring.clicked.connect(lambda: writers.writer(ui, resources.RECURRING_FILE, recurring_dialog, main_window))
    ui.clearRecurring.clicked.connect(lambda: writers.c_r_task(ui))
    ui.returnToMainRecurring.clicked.connect(lambda: return_to_main_clicked(recurring_dialog, main_window))
    ui.exitRecurring.clicked.connect(lambda: exit_clicked(recurring_dialog))
    recurring_dialog.exec()
    main_window.show()


# View projects and archives
def project_viewer_clicked(main_window, idx):
    print("Loading viewer...")
    main_window.close()
    viewer = QDialog(main_window)
    ui = Ui_Viewer()
    ui.setupUi(viewer)

    # Function to handle tab changes
    def tab_changed(top_tab, sub_tab):
        print(f"Top tab: {top_tab}")
        print(f"Sub tab: {sub_tab}\n")
        printer(top_tab, sub_tab)


    ui.viewer.setCurrentIndex(idx)
    if ui.viewer.currentIndex == 0:
        ui.currentProjects.setCurrentIndex(0)
    if ui.viewer.currentIndex == 1:
        ui.archive.setCurrentIndex(0)
    ui.viewer.currentChanged.connect(tab_changed(ui.viewer.currentIndex, ))
    ui.projectTabs.currentChanged.connect(tab_changed)
    ui.archivedTabs.currentChanged.connect(tab_changed)
    ui.editProject.clicked.connect(lambda: edit_project_clicked)
    ui.archiveProject.clicked.connect(lambda: archive_project_clicked)
    ui.deleteProject.clicked.connect(lambda: delete_project_clicked)
    ui.returnToMainProjects.clicked.connect(lambda: return_to_main_clicked(viewer, main_window))
    ui.exitProjects.clicked.connect(lambda: exit_clicked(viewer))
    ui.restoreArchived.clicked.connect(restore_project_clicked)
    ui.deleteArchived.clicked.connect(delete_archive_clicked)
    ui.returnToMainArchive.clicked.connect(lambda: return_to_main_clicked(viewer, main_window))
    ui.exitArchive.clicked.connect(lambda: exit_clicked(viewer))
    viewer.exec()
    main_window.show()

    


def edit_project_clicked():
    print("Editing project...")

def archive_project_clicked():      # Check if project is completed or to be archived as is
    print("Archiving project...")

def delete_project_clicked():
    print("Deleting project from project list...")   # Needs a safety check

def restore_project_clicked():
    print("Restore project...")

def delete_archive_clicked():
    print("Deleting project from archive...")       # Needs a safety check
