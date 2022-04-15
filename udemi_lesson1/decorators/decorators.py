# Декораторы - позволяют добавить функциональность в уже существующую функцию
# Используют оператор @  помещаются поверх исходной фнкции


# передавать одну функцию как параметр в другую функцию

def hello(name='Влад'):
    print('Мы запустили функцию hello')

    def greet():
        return '\t Это функция greet внутри функции hello'

    def welcome():
        return '\t Это функция welcome внутри функции hello'

    print('Собираемся вернуть функцию')

    if name == 'Влад':
        return greet
    else:
        return welcome

    # print(greet())
    # print(welcome())
    # print('Это окончание функции hello')


my_new_func = hello('Влад')
print(my_new_func())


def cool():
    def super_cool():
        return 'Super cool'

    return super_cool()


some_func = cool()

print(some_func)


def hello():
    return 'Привет, Влад!'


def other(some_def_func):
    print('Здесь выполняется другой код')
    print(some_def_func())


other(hello)


def new_decorator(origin_func):
    def wrap_func():
        print('Некоторый код, выполняющийся до функции origin_func')

        origin_func()

        print('Код, выполняющийся после функции origin_func')

    return wrap_func


def func_needs_decorator():
    print('Эта функция нуждается в декораторе')


decorated_func = new_decorator(func_needs_decorator)
decorated_func()


# Создание декоратора
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


# Функция к которой будет применяться декоратор
def say_hi():
    return 'hello'


decorate = uppercase_decorator(say_hi)
print(decorate())
