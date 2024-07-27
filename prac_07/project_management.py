from prac_07.project import Project
import datetime

FILENAME = 'projects.txt'
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""

projects = []


def main():
    """a program for manage projects"""
    print("Welcome to Pythonic Project Management")
    read_file()
    project_number = len(projects)
    print(f"Loaded {project_number} projects from projects.txt")
    user_choice = input(MENU).upper()
    while user_choice != "Q":
        if user_choice == "L":
            load_project()
        elif user_choice == "S":
            save_project()
        elif user_choice == "D":
            display_projects()
        elif user_choice == "F":
            filter_project()
        elif user_choice == "A":
            add_project()
        elif user_choice == "U":
            update_project()
        else:
            print("Invalid Menu Choice")
        user_choice = input(MENU).upper()
    save_choice = input("Would you like to save to projects.txt?")
    if "no" not in save_choice:
        save_file()
    print("Thank you for using custom-built project management software.")


def load_project():
    project_name = input("Enter project name: ")
    if project_name:
        read_file(project_name)
    else:
        print("Invalid filename, save in default file.")
        read_file()


def read_file(filename=FILENAME):
    """read the file and store the data"""
    with open(filename, 'r') as in_file:
        next(in_file)
        for line in in_file:
            data = line.split('\t')
            project = Project(data[0], data[1], int(data[2]), float(data[3]), int(data[4]))
            projects.append(project)


def display_projects():
    """display all projects"""
    completed_projects = []
    incomplete_projects = []
    projects.sort()
    for project in projects:
        if project.is_complete():
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)
    print('Incomplete projects: ')
    for i in incomplete_projects:
        print('\t', i)
    print('Completed projects:')
    for i in completed_projects:
        print('\t', i)


def update_project():
    """update completion percentage for a project"""
    for i, project in enumerate(projects):
        print(i, project)
    project_choice = int(input("Project choice: "))
    print(projects[project_choice])
    new_percentage = int(input("New Percentage: "))
    new_priority = int(input("New Priority: "))
    projects[project_choice].completing_percentage = new_percentage
    projects[project_choice].priority = new_priority


def add_project():
    """add a new project"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date(dd / mm / yy): ")
    priority = int(input("Priority: "))
    cost_estimate = int(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def get_valid_date(prompt):
    """return a valid date"""
    valid_date = False
    date = 0
    while not valid_date:
        date = input(prompt)
        try:
            date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
        except ValueError:
            print("Invalid date,please input again.")
            date = input(prompt)
        valid_date = True
    return date


def filter_project():
    """filter project by date"""
    start_date = get_valid_date("Show projects that start after date (dd/mm/yy): ")
    for project in projects:
        project_date = datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
        if start_date < project_date:
            print(project)


def save_project():
    project_name = input("Enter project name: ")
    if project_name:
        save_file(project_name)
    else:
        print("Invalid filename, save in default file.")
        save_file()


def save_file(filename=FILENAME):
    """save the project data into file"""
    with open(filename, "w") as on_file:
        print("Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=on_file)
        for project in projects:
            print(f"{project.name}\t"
                  f"{project.start_date}\t"
                  f"{project.priority}\t"
                  f"{project.cost_estimate}\t"
                  f"{project.completion_percentage}", file=on_file)


main()
