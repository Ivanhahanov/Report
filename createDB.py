import json

id = '1'
login = 'admin'
password = 'secret'

data = {
    '0': {
        'name': 'Ivan',
        'surname': 'Hahanov',
        'patronymic': 'Sergeevich',
        'tasks': [{
            'task_name': '',
            'task_group': '',
            'task_weight': 1,
            'deadline': 1,
            'difficult': 1,
            'visits': 1,
            'independent': 1,
            'description': '',
        }]
    },
    '1': {
        'name': 'Natali',
        'surname': 'Darovskikh',
        'patronymic': 'Pavlovna',
        'tasks': [{
            'task_name': '',
            'task_group': '',
            'task_weight': 1,
            'deadline': 1,
            'difficult': 1,
            'visits': 1,
            'independent': 1,
            'description': '',
        }]
    },
    '2': {
        'name': 'Vlad',
        'surname': 'Chernyakov',
        'patronymic': 'Alexandrovich',
        'tasks': [{
            'task_name': '',
            'task_group': '',
            'task_weight': 1,
            'deadline': 1,
            'difficult': 1,
            'visits': 1,
            'independent': 1,
            'description': '',
        }]
    }
}

with open("staff.json", 'w') as write_file:
    json.dump(data, write_file)
