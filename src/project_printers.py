########## Project printers ##########
# Imports
import json

import resources

from loader import load_file



# Print contents of file obtained from loaded projects file
def print_projects(top_tab, sub_tab):
    print(f"Receiving top tab: {top_tab}\nBottom tab: {sub_tab}\n")
    project_file = resources.tab_handler[top_tab][sub_tab]
    print(f"Tab file again: {project_file}")
