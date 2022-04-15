# Задание1
# Напишите функцию, которая вычисляет объём сферы по заданному радиусу.

def vol(rad):
    return (4 / 3) * (3.14) * (rad ** 3)


x = vol(2)
print(x)


# Задание2
# Напишите функцию, которая проверяет, содержится ли число в указанном диапазоне (включая верхнюю и нижнюю границы)

def ran_check(num, low, high):
    if num in range(low, high + 1):
        print('{} находится в диапазоне между {} и {}'.format(num, low, high))
    else:
        print('Число находится вне диапазона')


x = ran_check(5, 2, 7)


# Если Вы хотите вернуть только значение boolean:

def ran_bool(num, low, high):
    return num in range(low, high + 1)


y = ran_bool(5, 1, 10)
print(y)


# Задание3
# Напишите функцию Python, которая принимает на вход строку,
# и вычисляет количество букв в верхнем регистре и в нижнем регистре.

def up_low(s):
    d = {'upper': 0, 'lower': 0}
    for char in s:
        if char.isupper():
            d['upper'] += 1
        elif char.islower():
            d['lower'] += 1
        else:
            pass
    print('Исходная строка: ', s)
    print('Количество символов в верхнем регистре:', d['upper'])
    print('Количество символов в нижнем регистре:', d['lower'])


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


# Задача4
# Напишите функцию Python, которая получает на входе список,
# и возвращает новый список, содержащий уникальные элементы из первого списка.
# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]


def unique_list(lst):
    my_list = []
    for i in lst:
        if i not in my_list:
            my_list.append(i)
    return my_list


z = unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])
print(z)

# Задача5
# Напишите функцию Python, которая перемножает все числа в списке.

def multiply(numbers):
    total = 1  # для умножения, умножение на 1 не меняет число
    for num in numbers:
        total *= num
    return total


z = multiply([1, 2, 3, -4])
print(z)

# Задача6
# Напишите функцию Python, которая проверяет входную строку, является ли эта строка палиндромом или нет.

def palindrome(s):
    s = s.replace(' ', '')  # заменяем все пробелы
    return s == s[::-1]

z = palindrome('helleh')
print(z)

# Задача7
#Напишите функцию Python, которая проверяет, является ли строка панграммой или нет.

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

x = ispangram("The quick brown fox jumps over the lazy dog")
print(x)