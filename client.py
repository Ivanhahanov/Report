import requests, json, random

class Client():


    def __init__(self, debug_mode, host):
        self.debug_mode = debug_mode
        self.host = host

    def login(self):
        if self.debug_mode:
            login, password = 'admin', 'secret'
        else:
            print('\n\n-------------------')
            login, password = input('| Login: '), input('| Password: ')
            print('-----------------------')
        params = {
            'login': login,
            'password': password,
        }
        r = requests.post(self.host, params=params).text
        data = json.loads(r)
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

    def main_menu(self):
        print('1. Посмотреть свою стату\n2.Внести таск\n3.Сформировать отчет\n0.Выйти')
        user_choice = input()
        if user_choice == '1':
            #вызов функции просмотра статистики
            self.show_personal_info()
            self.show_tasks_info()
        elif user_choice == '2':
            #вызов функции добавления таска
            current_task = self.new_task()
            #сохранение таска
            self.save_task(current_task)
        elif user_choice == '3':
            #получение ссылки на отчет
            print(self.create_report())
        elif user_choice == '0':
            #при возможности написать выход из программы
            #кажется что то вроде os.system('exit)
            #вместо return
            print('Bye, bye!')
            return
        else:
            print('Ты косорукий ублюдок')
            self.main_menu()

    def show_personal_info(self):
        user_info = self.get_full_user_info()
        print('Фамилия:',user_info['surname'])
        print('Имя:',user_info['name'])
        print('Отчество:',user_info['patronymic'])
        print()

    def show_tasks_info(self):
        user_info = self.get_full_user_info()
        user_tasks = user_info['tasks']
        print('Выполнено тасков:', len(user_tasks), '\n\n')
        for task in user_tasks:
            print('Название:', task['task_name'])
            print('Описание:', task['description'])
            print('Срок выполнения до:', task['deadline'])
            print('Посещаемость:', task['visits'])
            print('Коэффциент сложности:', task['task_weight'])
            print('Трудоемкость задания:', task['difficult'])
            print('Независимость вполнения:', task['independent'])
            print('-------------------------------------------------')
        print()
            #не стала сюда писать группу таска, ибо она == коэффициенту сложности

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

        task = {
            'task_name': input('Введите название таска: '),
            'description': input('Описание: '),
            'deadline': input('Срок выполнения до: '),
            'visits': input('Посещаемость: '),
            'task_weight': input('Коэффициент сложности: '),
            'task_group': input('Группа таска: '),
            'difficult': input('Трудоемкость таска: '),
            'independent': input('Независимость выполнения: '),
        }
        return task

    def test_new_task(self):
        #создание нового таска
        #print(self.data)

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
        user_info = self.get_full_user_info()
        # сохранение таска
        user_info['tasks'].append(task)
        answer = input('Добавить таск? (y/n)')
        user_info['id'] = self.id
        if answer == 'y':
            r = requests.post(self.host+'/send', json=user_info)

    def create_report(self):
        print('ВАНЯ!!! ПЕРЕПРОВЕРЬ корректность составления ссылки. Формируется отчет в папку пдф, а отображается с корневого')
        if self.id == '0':
            r = requests.post(self.host+'/adminreport').text
        else:
            r = requests.post(self.host+'/report/%s'%self.id).text
        return self.host+r

    def get_full_user_info(self):
        r = requests.post(self.host+'/user/%s'%self.id).text
        self.data = json.loads(r)
        return self.data



def main():
    client = Client(debug_mode=False, host='http://127.0.0.1:5000')
    if client.test():
        print('*****************************************')
        print('*  ╔═══╗╔══╗╔══╗╔═══╗╔╗──╔══╗╔══╗─╔══╗  *')
        print('*  ║╔══╝╚═╗║║╔═╝║╔═╗║║║──║╔╗║║╔╗║─║╔═╝  *')
        print('*  ║╚══╗──║╚╝║──║╚═╝║║║──║╚╝║║╚╝╚╗║╚═╗  *')
        print('*  ║╔══╝──║╔╗║──║╔══╝║║──║╔╗║║╔═╗║╚═╗║  *')
        print('*  ║╚══╗╔═╝║║╚═╗║║───║╚═╗║║║║║╚═╝║╔═╝║  *')
        print('*  ╚═══╝╚══╝╚══╝╚╝───╚══╝╚╝╚╝╚═══╝╚══╝  *')
        print('*****************************************')


        data = client.login()
        if data:
            while (True):
                menu = Menu(id=client.get_id(), debug_mode=False, host='http://127.0.0.1:5000')
                menu.main_menu()


if __name__ == '__main__':
    main()

