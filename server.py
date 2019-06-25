from flask import Flask, request, jsonify
import json
from main import Person
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        id = '0'
        login = request.args.get('login', None)
        print(login)
        password = request.args.get('password')
        print(password)
        with open("data.json", encoding='utf-8') as write_file:
            data = json.loads(write_file.read())
        if id in data:
            name = data[id]
            if name['login'] == login:
                if name['password'] == password:
                    return jsonify({'id':id})
        return jsonify({'status': 'error'})
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
    data = request.json
    print('data:', data)
    return 'ok'

if __name__ == '__main__':
    app.run()
