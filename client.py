import requests, json, random

class Client():


    def __init__(self, debug_mode, host):
        self.debug_mode = debug_mode
        self.host = host

    def login(self):
        if self.debug_mode:
            login, password = 'admin', 'secret'
        else:
            login, password = input('Login: '), input('Password: ')
        params = {
            'login': login,
            'password': password,
        }
        r = requests.post(self.host, params=params).text
        data = json.loads(r)
        print(data)
        if 'status' in data:
            return False
        if data['id'] != '999':
            print('login success')
            self.id = data['id']
            return data
        else:
            print('login error')
            return None


    def test(self):
        test = requests.post(self.host+'/connect',).text
        if test == 'ok':
            return True
        else:
            print('Error connection')

    def send(self, data):
        r = requests.post(self.host+'/send', json=data)

    def get_id(self):
        return self.id

class Menu(Client):

    data = ''

    def __init__(self, id, debug_mode, host):
        super().__init__(debug_mode, host)
        self.id = id

    def print(self):
        return self.test()

    def show(self):
        r = requests.post(self.host+'/user/%s'%self.id).text
        self.data = json.loads(r)
        return self.data

    def change_task(self):
        # изменение таска
        i = 0
        for task in self.data['tasks']:

            print(i, task)
            i += 1
        task = input('Enter: ')
        if task == 'exit':
                return True
        while True:
            i = 0
            for key, field in self.data['tasks'][int(task)].items():
                i += 1
                print(i, key, field)
            command = input('Enter: ')
            if command == 'exit':
                break
            else:
                #some problems here
                pass

    def new_task(self):
        #создание нового таска
        print(self.data)
        task_name = input('Enter task name')
        task = {
            'task_name': input('Enter task name: '),
            'task_group': input('task_group: '),
            'task_weight': input('task_weight: '),
            'deadline': input('deadline: '),
            'difficult': input('difficult: '),
            'visits': input('visits: '),
            'independent': input('independent: '),
            'description': input('description: '),
        }
        return task

    def test_new_task(self):
        #создание нового таска
        print(self.data)

        task = {
            'task_name': 'test',
            'task_group': 'test',
            'task_weight': random.randint(1, 5),
            'deadline': random.randint(1, 5),
            'difficult': True,
            'visits': random.randint(1, 5),
            'independent': random.randint(1, 5),
            'description': 'test',
        }
        return task

    def save_task(self, task):
        # сохранение таска
        self.data['tasks'].append(task)
        print(self.data)
        answer = input('y/n')
        #answer = 'y'
        self.data['id'] = self.id
        if answer == 'y':
            r = requests.post(self.host+'/send', json=self.data)

    def create_report(self):
        if self.id == '0':
            r = requests.post(self.host+'/adminreport').text
        else:
            r = requests.post(self.host+'/report/%s'%self.id).text
        return self.host+r



def main():
    client = Client(debug_mode=False, host='http://127.0.0.1:5000')
    if client.test():
        data = client.login()
        if data:
            menu = Menu(id=client.get_id(), debug_mode=False, host='http://127.0.0.1:5000')
            menu.print()
            id = menu.show()
            print(id)

            task = menu.test_new_task()
            menu.save_task(task)
            link = menu.create_report()
            print(link)

if __name__ == '__main__':
    main()

