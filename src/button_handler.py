########## Button handler ##########
# Imports
import os
import sys

from interface.ui_everyday import Ui_everydayProjectEditor
from interface.ui_main import Ui_ProjectPlannerMain
from interface.ui_programming import Ui_programmingProjectEditor
from interface.ui_tabs import Ui_Viewer


# Universal buttons
def return_to_main_clicked():
    print("Return to main menu clicked")

def exit_clicked():
    print("Exiting program...")
    close = input("Are you sure you want to quit? y/n").upper()
    if close == "Y":
        sys.exit()
    else:
        print("Returning to previous menu")

# Main menu buttons
def add_project_clicked():
    print("Add project clicked!")

def view_projects_clicked():
    print("View projects clicked")

def view_archive_clicked():
    print("View archive clicked")

# Add project menu buttons
def 