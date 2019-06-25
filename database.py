import json

#id = '1'
#login = 'admin'
#password = 'secret'

data = {
    '0': {
        'id' : '0',
        'login': 'admin',
        'password': 'secret',
        'info': 'Hello, Admin',
    },

    '1': {
        'id' : '1',
        'login': 'natali',
        'password': '111',
        'info': 'Hello,Natali',
    },

    '2': {
        'id' : '2',
        'login': 'vlad',
        'password': '222',
        'info': 'Hello, Vlad',
    }
}

with open("data.json", 'w') as write_file:
    json.dump(data, write_file)
