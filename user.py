class User:  # создание класса
    def __init__(self, id, name, age, email):  # основные объекты класса
        self.id = id
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):  # для вывода строки
        return f' {self.id}. {self.name}, {self.age}, {self.email}'


class ManageUsers:
    def __init__(self):
        self.users = []  # переменная для списка пользователей

    def add_user(self):  # функция добавления пользователей
        id = len(self.users) + 1
        name = (input('Введите имя пользователя латиницей: '))
        age = (int(input('Введите возраст пользователя: ')))
        email = (input('Введите email пользователя: '))
        user = User(id, name, age, email)
        return self.users.append(user)

    def print_users(self):  # функция вывода пользователей в консоль
        for el in self.users:  # перебор
            print(el)

    def find_user_by_id(self):
        id = int(input('Введите id user: '))
        for i in range(len(self.users)):  # перебор списка
            if self.users[i].id == id:  # если индекс данных юзера равен его id
                return i
        print('Некорректный ID')
        self.find_user_by_id()

    def remove_user(self):  # удаление пользователей
        idx = self.find_user_by_id()
        self.users.pop(idx)

    def update_user(self):  # изменение данных
        idx = self.find_user_by_id()
        self.users.pop(idx)
        name = (input('Введите имя пользователя латиницей: '))
        age = (int(input('Введите возраст пользователя: ')))
        email = (input('Введите email пользователя: '))
        user = User(idx + 1, name, age, email)
        return self.users.insert(idx, user)


manager = ManageUsers()
manager.add_user()
manager.add_user()
manager.add_user()
manager.print_users()
manager.remove_user()
manager.print_users()
manager.update_user()
manager.print_users()
