"""
manage the Project class
estimated time: 40 minutes
needed time: 46 minutes
"""

from project import Project
import datetime

MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n"
        "- (A)dd new project\n- (U)pdate project\n- (Q)uit")


def main():
    projects = []
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Please insert the filename to load the projects: ")
            in_file = open(filename, 'r')
            for line in in_file:
                parts = line.strip().split(',')
                project = Project(parts[0], datetime.datetime.strptime(parts[1], "%Y-%m-%d").date(), int(parts[2]),
                                  float(parts[3]), int(parts[4]))
                projects.append(project)
            in_file.close()

        elif choice == "S":
            filename = input("Please insert the filename where the projects should be saved: ")
            in_file = open(filename, 'w')
            for project in projects:
                in_file.write(f"{project.name},{project.start_date},{project.priority},{project.cost},"
                              f"{project.completion}\n")
            in_file.close()

        elif choice == "D":
            print("Incomplete projects:")
            incomplete_projects = sorted([project for project in projects if project.completion != 100])
            complete_projects = sorted([project for project in projects if project.completion == 100])
            for project in incomplete_projects:
                print(project)
            print("Complete projects:")
            for project in complete_projects:
                print(project)

        elif choice == "F":
            date_string = input("Show projects that start after date (dd/mm/yy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%y").date()
            filtered_projects = [project for project in projects if project.start_date > date]
            for project in filtered_projects:
                print(project)

        elif choice == "A":
            print("Lets add a new project")
            name = input("Name: ")
            start_date = datetime.datetime.strptime(input("Start date (dd/mm/yy): "), "%d/%m/%y").date()
            priority = int(input("Priority: "))
            cost = float(input("Cost estimate: "))
            completion = int(input("Percent complete: "))
            new_project = Project(name, start_date, priority, cost, completion)
            projects.append(new_project)

        elif choice == "U":
            for i, project in enumerate(projects):
                print(f"{i} {project}")
            project_id = int(input("Project choice: "))
            print(projects[project_id])
            new_completion = int(input("New Percentage: "))
            new_priority = int(input("New priority: "))
            projects[project_id].update(new_completion, new_priority)

        else:
            print("You entered a wrong letter - please try again.")

        print(MENU)
        choice = input(">>> ").upper()
    print("thank you for using custom-built project management software.")

main()
