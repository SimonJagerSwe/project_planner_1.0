########## Project editors ##########
# Imports
import button_handler, project_deleter, resources, writers

from interface.ui_everyday import Ui_everydayProjectEditor
from interface.ui_programming import Ui_programmingProjectEditor 
from interface.ui_recurring import Ui_recurringProjectEditor
# from writers import project_data

from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDialog

# Connect editor buttons to reuse the button calls from button_handler.py
def connect_buttons(ui, dialog, main_window, project_type, viewer_dialog=None, current_project=None):
    if project_type == "everyday":
        ui.everydaySave.clicked.connect(lambda: save_and_return(ui, dialog, main_window, viewer_dialog, project_type, current_project, "edit"))
        ui.everydayClear.clicked.connect(lambda: resources.clear_input(ui))
        ui.everydayReturn.clicked.connect(lambda: resources.return_to_main_clicked(dialog, main_window, viewer_dialog))
        ui.everydayExit.clicked.connect(lambda: resources.exit_clicked(dialog))
    elif project_type == "programming":
        ui.programmingSave.clicked.connect(lambda: save_and_return(ui, dialog, main_window, viewer_dialog, project_type, current_project, "edit"))
        ui.programmingClear.clicked.connect(lambda: resources.clear_input(ui))
        ui.programmingReturn.clicked.connect(lambda: resources.return_to_main_clicked(dialog, main_window, viewer_dialog))
        ui.programmingExit.clicked.connect(lambda: resources.exit_clicked(dialog))
    else:
        ui.saveRecurring.clicked.connect(lambda: save_and_return(ui, dialog, main_window, viewer_dialog, project_type, current_project, "edit"))
        ui.clearRecurring.clicked.connect(lambda: resources.clear_input(ui))
        ui.returnToMainRecurring.clicked.connect(lambda: resources.return_to_main_clicked(dialog, main_window, viewer_dialog))
        ui.exitRecurring.clicked.connect(lambda: resources.exit_clicked(dialog))


# Function to determine which ui to use for editing
def edit_parser(project, viewer_dialog, main_window):
    print(f"Project to edit:\n{project.text()}\n")

    # Identify project type
    project_type = resources.parse_type(project)
    print(f"Project type received by edit parser:\n{project_type}\n")
    current_project = resources.project_parser(project, project_type)
    print(f"Name of current project:\n{current_project}\n")
    
    if project_type == "programming":
        ui = Ui_programmingProjectEditor()
        dialog = QDialog(viewer_dialog)
        ui.setupUi(dialog)
        connect_buttons(ui, dialog, main_window, project_type, viewer_dialog, current_project)
        edit_programming(ui, project, main_window)
        dialog.exec()
    elif project_type == "recurring":
        ui = Ui_recurringProjectEditor()
        dialog = QDialog(viewer_dialog)
        ui.setupUi(dialog)
        connect_buttons(ui, dialog, main_window, project_type, viewer_dialog, current_project)
        edit_recurring(ui, project, main_window)
        dialog.exec()
    else:
        ui = Ui_everydayProjectEditor()
        dialog = QDialog(viewer_dialog)
        ui.setupUi(dialog)
        connect_buttons(ui, dialog, main_window, project_type, viewer_dialog, current_project)
        edit_everyday(ui, project, current_project, main_window)
        dialog.exec()


# Save edited file, refresh project files read
# And return to project viewer 
def save_and_return(ui, dialog, main_window, viewer_dialog, project_type, current_project, write_type):
    print("Deleting current project from project file(s)...\n")
    project_deleter.delete_project(current_project, project_type, viewer_dialog, main_window, "edit")
    print("Project deleted from project files\n")
    writers.writer(ui, project_type, dialog, main_window, write_type)
    dialog.close()
    if viewer_dialog is not None:
        viewer_dialog.close()
        if project_type == "everyday":
            print("Sub idx: 0\n")
            button_handler.project_viewer_clicked(main_window, 0, 0)
        elif project_type == "programming":
            print("Sub-idx: 1\n")
            button_handler.project_viewer_clicked(main_window, 0, 1)
        else:
            print("Sub idx: 3\n")
            button_handler.project_viewer_clicked(main_window, 0, 3)       


# Edit everyday project 
def edit_everyday(ui, project, current_project, main_window):
    print("Editing everyday...\n")
    print(f"Everyday project:\n{project}\n")
    # current_project = resources.project_parser(project, "everyday")
    ui.everydayName.setText(current_project["Project name"])
    ui.everydayStart.setDate(QDate.fromString(current_project["Project start"], "yyyy-MM-dd"))
    ui.everydayFinish.setDate(QDate.fromString(current_project["Project end"], "yyyy-MM-dd"))
    ui.everydayNotes.setText(current_project["Project notes"])
    progress_text = current_project["Project progress"]
    progress_value = int(progress_text.strip("%"))
    ui.everydayProgressSlider.setValue(progress_value)
    ui.everydayProgressSlider.valueChanged.connect(lambda value: 
        ui.everydayProgressPercent.setText(f"{value}%"))
    ui.everydayProgressSlider.setValue(progress_value)
    ui.everydayProgressPercent.setText(progress_text)
    ui.everydayStatus.setCurrentText(current_project["Project status"])


# Edit programming project
def edit_programming(ui, project, main_window):
    print("Editing programming...\n")
    print(f"Programming project:\n{project}\n")
    current_project = resources.project_parser(project, "programming")
    print(f"Parsed programming project:\n{current_project}\n")
    ui.programmingName.setText(current_project["Project name"])
    ui.programmingStart.setDate(QDate.fromString(current_project["Project start"], "yyyy-MM-dd"))
    ui.programmingFinish.setDate(QDate.fromString(current_project["Project end"], "yyyy-MM-dd"))
    ui.languagesEdit.setText(current_project["Language(s)"])
    ui.githubEdit.setText(current_project["GitHub link"])
    progress_text = current_project["Project progress"]
    progress_value = int(progress_text.strip("%"))
    ui.programmingProgressSlider.setValue(progress_value)
    ui.programmingProgressSlider.valueChanged.connect(lambda value:
        ui.programmingProgressPercent.setText(f"{value}%"))
    ui.programmingProgressSlider.setValue(progress_value)
    ui.programmingProgressPercent.setText(progress_text)
    ui.programmingStatus.setCurrentText(current_project["Project status"])


# Edit recurring project
def edit_recurring(ui, project, main_window):
    print("Editing recurring task...\n")
    print(f"Recurring task:\n{project}\n")
    current_project = resources.project_parser(project, "recurring")
    print(f"Parsed recurring task:\n{current_project}\n")
    ui.recurringName.setText(current_project["Task name"])
    ui.recurringFrequency.setCurrentText(current_project["Task frequency"])
    ui.recurringNotes.setText(current_project["Task notes"])
    