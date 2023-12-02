"""
# English
Exercise - List of tasks with undo and redo

# add = [] -> list of tasks
# add = ['make coffee'] -> Add make coffee
# add = ['make coffee', 'walk'] -> Add walk
# undo = ['make coffee']
# redo = ['make coffee', 'walk']

# Portuguese
# Exercício - Lista de tarefas com desfazer e refazer
# adicionar = [] -> lista de tarefas
# adicionar = ['fazer cafe'] -> Adicionar fazer cafe
# adicionar = ['fazer cafe', 'caminhar'] -> Adicionar caminhar
# undo = ['fazer cafe']
# redo = ['fazer cafe', 'caminhar']
"""
commands = {'undo', 'redo'}
task_list = []
popped_list = []


def add_task(task, task_list):
    task_list.append(task)
    return task_list


def print_tasks():
    print('TASKS')
    for task in task_list:
        print(task)


def type_task_or_command(value):
    if value is None:
        print('Available Commands:', *commands)
        value = input('Type a task or a command: ')

    if value not in commands:
        add_task(value, task_list)
        print_tasks()
        type_task_or_command(None)

    if value == 'undo':
        if task_list:
            popped_task = task_list.pop()
            popped_list.append(popped_task)
            print_tasks()
        else:
            print('Nothing to undo!')
        type_task_or_command(None)

    if value == 'redo':
        if popped_list:
            popped_item = popped_list.pop()
            task_list.append(popped_item)
            print_tasks()
        else:
            print('Nothing to redo!')
        type_task_or_command(None)


type_task_or_command(None)
