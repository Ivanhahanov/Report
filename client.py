import requests, json

class Client():


    def __init__(self, debug_mode):
        self.debug_mode = debug_mode

    def login(self):
        if self.debug_mode:
            login, password = 'admin', 'secret'
        else:
            login, password = input('Login: '), input('Password: ')
        params = {
            'login': login,
            'password': password,
        }
        r = requests.post('http://127.0.0.1:5000/', params=params).text
        data = json.loads(r)
        if 'status' in data:
            return False
        print('login success')
        self.id = data['id']
        return data


    def test(self):
        test = requests.post('http://127.0.0.1:5000/connect',).text
        if test == 'ok':
            return True
        else:
            print('Error connection')

    def send(self, data):
        r = requests.post('http://127.0.0.1:5000/send', json=data)

    def get_id(self):
        return self.id

class Menu(Client):

    def __init__(self, id, debug_mode):
        super().__init__(debug_mode)
        self.id = id

    def __init__(self, id):
        self.id = id

    def print(self):
        return self.test()

    def show(self):
        r = requests.post('http://127.0.0.1:5000/user/%s'%self.id).text
        data = json.loads(r)
        return data

def main():
    client = Client(debug_mode=False)
    if client.test():
        data = client.login()
        if data:
            print(data['id'])
            menu = Menu(id=client.get_id())
            menu.print()
            client.send(data)
            id = menu.show()
            print(id)

if __name__ == '__main__':
    main()

