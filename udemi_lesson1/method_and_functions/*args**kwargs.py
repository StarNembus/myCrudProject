def my_func(a, b):  # a, b аргументы функции (позиционные)
    # Returns 5% of the sum of a and b
    return sum((a, b)) * 0.05


x = my_func(40, 60)
print(x)

""" *args - произвольное количество позиционных аргументов"""  # используется кортеж


def my_func(*args):  # для возможности передать произвольное количество позиционных аргументов
    return sum(args) * 0.05


x = my_func(40, 60, 100)
print(x)


# итерация по args
def my_func(*args):
    for item in args:
        print(item)


my_func(40, 60, 100, 200)

""" **kwargs - произвольное количество именованных параметров"""  # используется словарь, порядок следования параметров не важен


def my_func(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))  # получим значение по ключу
    else:
        print('I did not find any fruit here')


my_func(fruit='apple', veggie='lettuce')

""" *args, **kwargs together"""


def my_func(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0], kwargs['food']))


my_func(10, 20, 30, fruit='apple', food='eggs', animal='dog')
