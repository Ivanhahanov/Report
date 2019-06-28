from flask import Flask, request, jsonify, url_for
import json
from fpdf import FPDF
from main import Person, Task

app = Flask(__name__, static_folder='pdf')

def admin_doc(data):
        spacing=1
        pdf = FPDF()
        pdf.set_font("Arial", size=12)
        pdf.add_page()

        col_width = pdf.w / 4.5
        row_height = pdf.font_size
        for row in data:
            for item in row:
                pdf.cell(col_width, row_height*spacing,
                     txt=item, border=1)
            pdf.ln(row_height*spacing)

        pdf.output('pdf/admin.pdf')

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

@app.route('/report/<id>', methods=['GET','POST'])
def report(id):
    with open("staff.json", encoding='utf-8') as write_file:
        data = json.loads(write_file.read())
    data = data[id]
    p = Person()
    p.name = data['name']
    p.patronymic = data['patronymic']
    p.surname = data['surname']
    p.tasks = data['tasks']
    p.calc()
    p.doc()
    #неправильно формируется ссылка
    #обращается к разным файлам (в корневой, а не в папке пдф)
    return url_for('static', filename='%s.pdf'%p.name)

@app.route('/adminreport/', methods=['GET','POST'])
def admin_report():
    with open("staff.json", encoding='utf-8') as write_file:
        data = json.loads(write_file.read())
    user_info = []
    data_report = [['name', 'surname', 'patronymic', 'tasks']]
    print(data)
    for user in data:
        data_user = data[user]
        p = Person()
        p.name = data_user['name']
        p.patronymic = data_user['patronymic']
        p.surname = data_user['surname']
        p.tasks = data_user['tasks']
        p.calc()
        user_info.append(p.name)
        user_info.append(p.surname)
        user_info.append(p.patronymic)
        user_info.append(str(len(p.tasks)))
        data_report.append(user_info)
        user_info = []

    print(data_report)
    admin_doc(data_report)
    return url_for('static', filename='admin.pdf')

if __name__ == '__main__':
    app.run()
