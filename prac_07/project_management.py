"""
Project Management Program
Estimated time: 50 minutes
Actual time:
"""
import datetime
from project import Project
from operator import attrgetter

DEFAULT_FILENAME = "projects.txt"
DATE_FORMAT = "%d/%m/%Y"
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    """Run the project management program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()

    save_choice = input(f"Would you like to save to {DEFAULT_FILENAME}? ").lower()
    if save_choice in ("y", "yes"):
        save_projects(DEFAULT_FILENAME, projects)
    print("Thank you for using custom-built project management software.")

def filter_projects_by_date(projects: list[Project]):
    """Prompt for a date and display projects starting on or after that date, sorted by date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(date_string, DATE_FORMAT).date()

    filtered_projects = [p for p in projects if p.start_date >= filter_date]
    filtered_projects.sort(key=attrgetter("start_date"))

    for project in filtered_projects:
        print(project)

def update_project(projects: list[Project]):
    """Allow the user to select a project and update its completion percentage and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_index = int(input("Project choice: "))
    selected_project = projects[project_index]
    print(selected_project)

    new_percentage = input("New Percentage: ")
    if new_percentage != "":
        selected_project.completion_percentage = int(new_percentage)

    new_priority = input("New Priority: ")
    if new_priority != "":
        selected_project.priority = int(new_priority)

def add_new_project(projects: list[Project]):
    """Prompt user for project details and add a new Project to the list."""
    print("Let's add a new project")
    name = input("Name: ")
    date_string = input("Start date (dd/mm/yy): ")
    start_date = datetime.datetime.strptime(date_string, DATE_FORMAT).date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def display_projects(projects: list[Project]):
    """Display incomplete and completed projects, each sorted by priority."""
    incomplete_projects = sorted([p for p in projects if not p.is_complete()])
    completed_projects = sorted([p for p in projects if p.is_complete()])

    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects: ")
    for project in completed_projects:
        print(f"  {project}")

def save_projects(filename: str, projects: list[Project]):
    """Save a list of Project objects to a tab-delimited file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            date_str = project.start_date.strftime(DATE_FORMAT)
            print(f"{project.name}\t{date_str}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)

def load_projects(filename: str) -> list[Project]:
    """Load projects from a tab-delimited file and return a list of Project objects."""
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()  # Skip header line
        for line in in_file:
            parts = line.strip().split("\t")
            name = parts
            start_date = datetime.datetime.strptime(parts, DATE_FORMAT).date()
            priority = int(parts)
            cost_estimate = float(parts)
            completion_percentage = int(parts)
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


if __name__ == "__main__":
    main()
