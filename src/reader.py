########## Reader ##########
# Imports
import json

def reader(file):
    try:
        with open(file, "r") as file:
            projects = json.load(file)
    except:
        projects = []
    return projects
