import json

id = '1'
login = 'admin'
password = 'secret'

data = {
    'id': id,
    'user': {
        'name': '',
        'surname': '',
        'patronymic': '',
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
