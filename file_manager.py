from functions import *


user_input = input(
    'Do you want to manage employees, projects, tasks or generate report? ')

if user_input.lower() == 'employees':
    print('Employees list: ')

    view_employees()

    print('')
    user_input = input('Do you want to add or edit employees? ')

    if user_input.lower() == 'add':
        print('Add employee')
        add_employees()
        print("Employee added")

    elif user_input.lower() == 'edit':
        print('Edit employee')
        # edit_employees(dictionary)

    elif user_input.lower() == 'generator report':
        print('Generate report')  # GENERATE RECORD
        # edit_employees(dictionary)

    else:
        print('Type add or edit')

elif user_input.lower() == 'projects':
    print('Projects list: ')

    view_projects()

    print('')
    user_input = input('Do you want to add or edit projects? ')

    if user_input.lower() == 'add':
        print('Add project')
        add_projects()
        print("Project added")

    elif user_input.lower() == 'edit':
        print('Edit project')
        # edit_projects(dictionary)

    else:
        print('Type add or edit')


elif user_input.lower() == 'tasks':
    print('Employees list: ')
    view_employees()

    print('Projects list: ')
    view_projects()

    print('Tasks list: ')
    view_tasks()

    print('')
    user_input = input('Do you want to add or edit tasks? ')

    if user_input.lower() == 'add':
        print('Add task')
        add_tasks()
        print("Tasks added")

    elif user_input.lower() == 'edit':
        print('Edit task')
        # edit_tasks(dictionary)

    else:
        print('Type add or edit')


elif user_input.lower() == 'generate report':
    print('Employees list: ')
    view_employees()

    print('Projects generate reportist: ')
    view_projects()

    print('Tasks list: ')
    view_tasks()  

    generator_report()


else:
    print('Type employees, projects, tasks or generate report')
