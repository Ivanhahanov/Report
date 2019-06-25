import json
id = '1'
login = 'admin'
password = 'secret'

data = {
    'id':id,
    'user': {
        'login': login,
        'password': password,
        'info': 'Hello, %s'%login,
    }
}

with open("data.json", 'w') as write_file:
    json.dump(data, write_file)
