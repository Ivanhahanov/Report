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
        return

class Menu(Client):

    def print(self):
        return self.test()

    def show(self):
        print()

def main():
    client = Client(debug_mode=True)
    if client.test():
        data = client.login()
        if data:
            print(data)
            menu = Menu(debug_mode=True)
            menu.print()
            client.send(data)

if __name__ == '__main__':
    main()

