########## Project editors ##########
# Imports
import resources, writers

from interface.ui_everyday import Ui_everydayProjectEditor
from interface.ui_programming import Ui_programmingProjectEditor 
from interface.ui_recurring import Ui_recurringProjectEditor

from PySide6.QtWidgets import QDialog


def edit_parser(project):
    print(f"Project to edit:\n{project.text()}")
    if "Language(s)" in project.text():
        ui = Ui_programmingProjectEditor()
        edit_programming(ui, project)
    elif "Task frequency" in project.text():
        ui = Ui_recurringProjectEditor()
        edit_recurring(ui, project)
    else:
        ui = Ui_everydayProjectEditor()
        edit_everyday(ui, project) 


def edit_everyday(ui, project):
    print("Editing everyday...")
    dialog = QDialog()
    ui.setupUi(dialog)
    dialog.exec()


def edit_programming(ui, project):
    print("Editing programming...")
    dialog = QDialog()
    ui.setupUi(dialog)
    dialog.exec()


def edit_recurring(ui, project):
    print("Editing recurring project...")
    dialog = QDialog()
    ui.setupUi(dialog)
    dialog.exec()

'''
def connect_editor_buttons(ui, dialog, main_window, project_type):
    if project_type == "everyday":
        ui.everydaySave.clicked.connect(
            lambda: writers.writer(ui, resources.EVERYDAY_FILE, dialog, main_window)
        )
        ui.everydayClear.clicked.connect(lambda: writers.clear_input(ui))
        ui.everydayReturn.clicked.connect(
            lambda: resources.return_to_main_clicked(dialog, main_window)
        )
        ui.everydayExit.clicked.connect(lambda: resources.exit_clicked(dialog))

    elif project_type == "programming":
        ui.programmingSave.clicked.connect(
            lambda: writers.writer(ui, resources.PROGRAMMING_FILE, dialog, main_window)
        )
        ui.programmingClear.clicked.connect(lambda: writers.clear_input(ui))
        ui.programmingReturn.clicked.connect(
            lambda: resources.return_to_main_clicked(dialog, main_window)
        )
        ui.programmingExit.clicked.connect(lambda: resources.exit_clicked(dialog))

    elif project_type == "recurring":
        ui.saveRecurring.clicked.connect(
            lambda: writers.writer(ui, resources.RECURRING_FILE, dialog, main_window)
        )
        ui.clearRecurring.clicked.connect(lambda: writers.clear_input(ui))
        ui.returnToMainRecurring.clicked.connect(
            lambda: resources.return_to_main_clicked(dialog, main_window)
        )
        ui.exitRecurring.clicked.connect(lambda: resources.exit_clicked(dialog))'''
