"""
CP1404 Prac 7 - Project Management Program
Estimated Time: 2 hours
Actual time:
"""
import datetime
from project import Project

MENU = """-(L)oad projects
-(S)ave projects
-(D)isplay projects
-(F)ilter projects by date
-(A)dd new project
-(U)pdate project
-(Q)uit"""
FILENAME = "projects.txt"

def main():
    projects = []
    print("Welcome to Pythonic Project Management")
    load_projects(FILENAME, projects)
    print(MENU)
    menu_choice = input(">>>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "S":
            pass
        elif menu_choice == "D":
            pass
        elif menu_choice == "F":
            pass
        elif menu_choice == "A":
            pass
        elif menu_choice == "U":
            pass
        else:
            print("Invalid Menu Choice.")
            menu_choice = input(">>>> ").upper()

    save_choice = input(f"Would you like to save to {FILENAME}?")
    #Pressing enter counts as yes
    wants_to_save = save_choice == ""
    if wants_to_save:
        pass
    print("Thank you for using custom-built project management software.")



def load_projects(filename, projects: list[Project]):
    with open(filename, "r") as in_file:
        #file format: name, start date, priority, cost estimate, completion percentage
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            projects.append(Project(parts[0], date, int(parts[2]), float(parts[3]), int(parts[4])))
    print(f"Loaded {len(projects)} from {filename}")


main()

