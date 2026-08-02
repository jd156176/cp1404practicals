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
    print(projects)
    print(MENU)
    menu_choice = input(">>>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            in_file_name = input("Type filename to load projects from: ")
            load_projects(in_file_name, projects)
        elif menu_choice == "S":
            out_file_name = input("Type filename to save projects to: ")
            save_projects(out_file_name, projects)
        elif menu_choice == "D":
            pass
        elif menu_choice == "F":
            pass
        elif menu_choice == "A":
            projects.append(create_project())
        elif menu_choice == "U":
            pass
        else:
            print("Invalid Menu Choice.")

        print(MENU)
        menu_choice = input(">>>> ").upper()

    save_choice = input(f"Would you like to save to {FILENAME}?")
    #Pressing enter counts as yes
    wants_to_save = save_choice == ""
    if wants_to_save:
        pass
    print("Thank you for using custom-built project management software.")



def load_projects(filename, projects: list[Project]):
    """Load projects from file and store them as a list of objects"""
    with open(filename, "r") as in_file:
        #file format: name, start date, priority, cost estimate, completion percentage
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            projects.append(Project(parts[0], date, int(parts[2]), float(parts[3]), int(parts[4])))
    print(f"Loaded {len(projects)} from {filename}")

def save_projects(filename, projects: list[Project]):
    """Write list of project objects formatted into tabular style to out file"""
    with open(filename, "w") as out_file:
        out_file.write("Name    Start Date  Priority    Cost Estimate   Completion Percentage\n")
        for project in projects:
            out_file.write(f"{project.to_file_line()}\n")
    print(f"Saved {len(projects)} to {filename}")

def get_non_empty_string(prompt):
    """Get a non-empty string from the user"""
    text = input(prompt).strip()

    while text == "":
        print("Input cannot be blank")
        text = input(prompt).strip()
    return text

def get_percentage(prompt):
    """Get an integer between 0 and 100 from the user."""
    number = -1

    while number < 0 or number > 100:
        try:
            number = int(input(prompt))
            if number < 0 or number > 100:
                print("Number must be greater than 0 and less than 100.")
        except ValueError:
            print("Invalid input; enter a valid number")
    return number

def get_positive_integer(prompt):
    """Get a positive integer from the user."""

    number = -1

    while number < 0:
        try:
            number = int(input(prompt))
            if number < 0:
                print("Number must be greater than 0.")
        except ValueError:
            print("Invalid input; enter a valid number")
    return number

def get_positive_float(prompt):
    """Get a positive floating point value from the user."""
    number = -1

    while number < 0:
        try:
            number = float(input(prompt))
            if number < 0:
                print("Number must be greater than 0.")
        except ValueError:
            print("Invalid input; enter a valid number")
    return number

def get_date(prompt):
    """Get a valid date in the dd/mm/yyyy format from the user."""
    date = None
    while date is None:
        date_text = input(prompt)
        try:
            date = datetime.datetime.strptime(date_text, "%d/%m/%Y").date()
        except ValueError:
            print("Invalid date; use dd/mm/yyyy format.")
    return date

def create_project():
    """Get details for a new project from the user and return it as a Project object"""
    print("Let's add a new project")
    name = get_non_empty_string("Name: ")
    start_date = get_date("Start date (dd/mm/yyyy): ")
    priority = get_positive_integer("Priority: ")
    cost_estimate = get_positive_float("Cost estimate: $")
    completion_percentage = get_percentage("Percentage Complete: ")

    return Project(name, start_date, priority, cost_estimate, completion_percentage)


main()

