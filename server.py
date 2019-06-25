from flask import Flask, request, jsonify, url_for
import json
import configuration
from main import Person, Task
app = Flask(__name__)
app.config.from_object(configuration)
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        login = request.args.get('login', None)
        #print(login)
        password = request.args.get('password')
        #print(password)
        with open("data.json", encoding='utf-8') as write_file:
            data = json.loads(write_file.read())

        # У нас есть только логин и пароль
        # Ищем какой id у логин-пароля введенного пользователем
        # Пробегаем по всей БД и возвращаем id (в json)))
        for id in data:
            if login == data[id]['login']:
                if password == data[id]['password']:
                    return jsonify({'id': data[id]['id']})

        return jsonify({'id': '999'})
    else:
        return 'get'

@app.route('/connect', methods=['GET','POST'])
def connect():
    return 'ok'


@app.route('/user/<staff>', methods=['GET','POST'])
def user(staff):
    with open("staff.json", encoding='utf-8') as write_file:
            data = json.loads(write_file.read())
    return jsonify(data[staff])


@app.route('/send', methods=['GET','POST'])
def send():
    new_data = request.json
    with open("staff.json", encoding='utf-8') as write_file:
        data = json.loads(write_file.read())
    id = new_data['id']
    new_data.pop('id')
    data[id] = new_data
    with open("staff.json", 'w') as write_file:
        json.dump(data, write_file)
    return 'ok'

@app.route('/report', methods=['GET','POST'])
def report():
    with open("staff.json", encoding='utf-8') as write_file:
        data = json.loads(write_file.read())
    data = data['0']
    p = Person()
    p.name = data['name']
    p.patronymic = data['patronymic']
    p.surname = data['surname']
    p.tasks = data['tasks']
    p.calc()
    p.doc()
    return 'http://0.0.0.0:5000/static/Ivan.pdf'

if __name__ == '__main__':
    app.run()
