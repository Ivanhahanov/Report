import json

id = '1'
login = 'admin'
password = 'secret'

data = {
    '0': {
        'name': 'Ivan',
        'surname': 'Hahanov',
        'patronymic': 'Sergeevich',
        'tasks': {
            'task_name': '',
            'task_group': '',
            'task_weight': '',
            'deadline': '',
            'difficult': '',
            'visit': '',
            'indepentdent': '',
            'description': '',
        }
    },
    '1': {
        'name': 'Natali',
        'surname': 'Darovskikh',
        'patronymic': 'Pavlovna',
        'tasks': {
            'task_name': '',
            'task_group': '',
            'task_weight': '',
            'deadline': '',
            'difficult': '',
            'visit': '',
            'indepentdent': '',
            'description': '',
        }
    },
    '2': {
        'name': 'Vlad',
        'surname': 'Chernyakov',
        'patronymic': 'Alexandrovich',
        'tasks': {
            'task_name': '',
            'task_group': '',
            'task_weight': '',
            'deadline': '',
            'difficult': '',
            'visit': '',
            'indepentdent': '',
            'description': '',
        }
    }
}

with open("staff.json", 'w') as write_file:
    json.dump(data, write_file)
