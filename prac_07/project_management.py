"""
CP1404 Prac 7 - Project Management Program
Estimated Time: 2 hours
Actual time:
"""
import datetime
from project import Project
from operator import attrgetter

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
            display_projects(projects)
        elif menu_choice == "F":
            filter_projects_by_date(projects)
        elif menu_choice == "A":
            projects.append(create_project())
        elif menu_choice == "U":
            update_project(projects)
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

def display_projects(projects: list[Project]):
    incomplete_projects = [project for project in projects if not project.is_complete()]
    completed_projects = [project for project in projects if project.is_complete()]
    incomplete_projects.sort(key=attrgetter("priority"))
    completed_projects.sort(key=attrgetter("priority"))

    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(f"\t{project}")
    print("Completed projects: ")
    for project in incomplete_projects:
        print(f"\t{project}")

def filter_projects_by_date(projects: list[Project]):
    """Display projects that start on or after a given date, sorted by start date."""
    cutoff_date = get_date("Show projects that start after date (dd/mm/yyyy): ")
    filtered_projects = [project for project in projects if project.start_date >= cutoff_date]
    filtered_projects.sort()
    for project in filtered_projects:
        print(project)

def display_indexed_projects(projects: list[Project]):
    """Print each project preceded by its position in the list."""
    for index, project in enumerate(projects):
        print(f"[{index}] {project}")

def get_valid_index(prompt, projects: list[Project]):
    """Get a valid project index from the user."""
    index = -1
    while index < 0 or index >= len(projects):
        try:
            index = int(input(prompt))
            if index <0 or index >= len(projects):
                print("Invalid project number.")
        except ValueError:
            print("Invalid input; enter a valid number")
    return index

def get_new_percentage(prompt, current_percentage):
    """Get a new completion percentage, keeping the current value if left blank."""
    percentage_text = input(prompt)
    while percentage_text != "":
        try:
            percentage = int(percentage_text)
            if 0 <= percentage <= 100:
                return percentage
            print("Percentage must be between 0 and 100.")
        except ValueError:
            print("Invalid input; enter a valid number")
        percentage_text = input(prompt)
    return current_percentage

def get_new_priority(prompt, current_priority):
    """Get a new priority, keeping the current value if left blank."""
    priority_text = input(prompt)
    while priority_text != "":
        try:
            priority = int(priority_text)
            if priority > 0:
                return priority
            print("Priority must be greater than 0.")
        except ValueError:
            print("Invalid input; enter a valid number")
        priority_text = input(prompt)
    return current_priority

def update_project(projects: list[Project]):
    """Let the user select a project and adjust its priority and/or completion progress"""
    display_indexed_projects(projects)
    index = get_valid_index("Project Choice: ", projects)
    project = projects[index]
    print(project)
    project.completion_percentage = get_new_percentage("New Percentage: ", project.completion_percentage)
    project.priority = get_new_priority("New Priority: ", project.priority)

main()

