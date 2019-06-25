from flask import Flask, request, jsonify
import json
from main import Person
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        user = 'admin'
        login = request.args.get('login', None)
        print(login)
        password = request.args.get('password')
        print(password)
        with open("data.json", encoding='utf-8') as write_file:
            data = json.loads(write_file.read())
        if user in data:
            name = data[user]
            if name['login'] == login:
                if name['password'] == password:
                    return jsonify(data[user])
    else:
        return 'get'

@app.route('/connect', methods=['GET','POST'])
def connect():
    return 'ok'

@app.route('/send', methods=['GET','POST'])
def send():
    data = request.json
    print('data:', data)
    return 'ok'

if __name__ == '__main__':
    app.run()
