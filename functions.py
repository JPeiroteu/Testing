import json
from datetime import *


def view_employees(file_name='data/employees.json'):
    with open(file_name) as employees_file:
        # returns JSON object as a dictionary
        dictionary = json.load(employees_file)

        # Iterating through the json list
        for i in dictionary['employees_info']:
            print(i)

        employees_file.close()


def add_employees(file_name='data/employees.json'):
    name = input('Employee name: ')
    surname = input('Employee surname: ')
    age = input('Employee age: ')
    position = input('Employee position: ')
    skills = input('Employee skills: ')
    active = input('Employee active (true/false): ')

    new_info = {
        "name": name,
        "surname": surname,
        "age": age,
        "position": position,
        "skils": skills,
        "active": active
    }

    with open(file_name, 'r+') as employees_file:
        dictionary = json.load(employees_file)
        dictionary["employees_info"].append(new_info)

        json.dump(dictionary, employees_file)

        employees_file.close()


def view_projects(file_name='data/projects.json'):
    with open(file_name) as projects_file:
        # returns JSON object as a dictionary
        dictionary = json.load(projects_file)

        # Iterating through the json list
        for i in dictionary['projects_info']:
            print(i)

        projects_file.close()


def add_projects(file_name='data/projects.json'):
    id = input('Project id: ')
    name = input('Project name: ')
    description = input('Project description: ')
    begin_date = input('Project begin date: ')
    deadline = input('Project deadline: ')
    active = input('Project active (true/false): ')

    new_info = {
        "id": id,
        "name": name,
        "description": description,
        "begin_date": begin_date,
        "deadline": deadline,
        "active": active
    }

    with open(file_name, 'r+') as projects_file:
        dictionary = json.load(projects_file)
        dictionary["projects_info"].append(new_info)

        json.dump(dictionary, projects_file)

        projects_file.close()


def view_tasks(file_name='data/tasks.json'):
    with open(file_name) as tasks_file:
        # returns JSON object as a dictionary
        dictionary = json.load(tasks_file)

        # Iterating through the json list
        for i in dictionary['tasks_info']:
            print(i)

        tasks_file.close()


def add_tasks(file_name='data/tasks.json'):
    id = input('Task id: ')
    project = input('Task project: ')
    employees = input('Task employees: ')
    description = input('Task description: ')
    begin_date = input('Task begin date: ')
    deadline = input('Task deadline: ')
    active = input('Task active (true/false): ')

    new_info = {
        "id": id,
        "project": project,
        "employees": employees,
        "description": description,
        "begin_date": begin_date,
        "deadline": deadline,
        "active": active
    }

    with open(file_name, 'r+') as tasks_file:
        dictionary = json.load(tasks_file)
        dictionary["tasks_info"].append(new_info)

        json.dump(dictionary, tasks_file)

        tasks_file.close()


def generator_report(projects_file='data/projects.json', tasks_file='data/tasks.json'):
    with open(projects_file) as projects_file:
        projects_dictionary = json.load(projects_file)

    with open(tasks_file) as tasks_file:
        tasks_dictionary = json.load(tasks_file)

    user_input = input('\nWhich project do you want to generate a report? ')

    for i in projects_dictionary["projects_info"]:
        if i["name"] == user_input:
            proj_name = i["name"]
            proj_begin_date = i["begin_date"]
            proj_deadline = i["deadline"]
            proj_active = i["active"]

            projects_file.close()

    for i in tasks_dictionary["tasks_info"]: # caso haja repeticao de valores para uma só variavel -> resolver
        if i["project"] == user_input:
            proj_employees = i["employees"]
            
            projects_file.close()
            
    
    time_now = datetime.now()
    string_now = time_now.strftime("%Y%m%d_%H%M%S")

    file_name = string_now + "_report.txt"
    
    proj_deadline_dt = datetime.strptime(proj_deadline, '%d-%m-%Y')

    days_left = time_now - proj_deadline_dt

    days_left = str(days_left.days)

    # verficas este codigos
    with open("reports/" + file_name, "w+") as reports_file:
        if (time_now > proj_deadline_dt and proj_active == "true"):
            reports_file.write(
                "The Project " + proj_name + " began in" + proj_begin_date + ". has as deadline: " + proj_deadline + "\n" +
                "The project should have been completed " + days_left + " days ago \n" +
                "Project members: \n" +
                proj_employees
                )
            
            print("The project has already passed the deadline! Report created " + file_name)

        elif (time_now < proj_deadline_dt and proj_active == "true"):
            reports_file.write(
                "The Project " + proj_name + " began in" + proj_begin_date + ". has as deadline: " + proj_deadline +
                "The project has more " + days_left + " days left" +
                "Project members: \n" +
                proj_employees
                )
            
            print("Pay attention to the deadline! Report created " + file_name)


        else:
            reports_file.write(
                "The Project " + proj_name + " began in" + proj_begin_date + ". has as deadline: " + proj_deadline +
                "Project completed!" +
                "Project members: \n" +
                proj_employees
                )

            print("Project Completed! Report created " + file_name)
    
    
    # verificar se declaro o file_name aqui ou no def generator_report


    # Comments:
    # tambem verficar nome das variaveis file_name ou meter sempre a mesma variavel
    # create new file with some content
    # o que faz o with?
    # 