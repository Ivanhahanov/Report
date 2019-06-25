import json
name = 'admin'
login = 'admin'
password = 'secret'

data = {
    name: {
        'login': login,
        'password': password,
        'info': 'good stuff',
    }
}

with open("data.json", 'w') as write_file:
    json.dump(data, write_file)
