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

def main():
    client = Client(debug_mode=True)
    if client.test():
        data = client.login()
        print(data)
        client.send(data)

if __name__ == '__main__':
    main()

