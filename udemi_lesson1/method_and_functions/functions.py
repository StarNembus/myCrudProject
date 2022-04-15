def name_function():
    """
    :return:
    DOCSTRING: информация о функции
    INPUT: нет
    OUTPUT: Hello
    """
    print('Hello')


name_function()  # вызов функции
help(name_function)  # печать комментария


def say_hello(name='Имя'):  # Имя вначале функции указывается как дефолтное, если функция будет вызываться без параметра
    print('Привет, ' + name)


say_hello('Juli')
say_hello()


# return используется для сохранения результата функции( результат работы)

def say_hello(name='Имя'):  # Имя вначале функции указывается как дефолтное, если функция будет вызываться без параметра
    return 'Привет, ' + name


result = say_hello('Juli')
print(result)


def add(n1, n2):
    return n1 + n2


result = add(20, 30)
print(result)


# найти слово Кот в строке


def cat_check(my_string):
    return 'кот' in my_string.lower()


result = cat_check('Кот здесь')
print(result)


# Pig Latin
# Чтобы получить слово берется слово на англ
# если первая буква гласная, то добавлемя в конце слова 'ау'
# если первая буква согласнаяб то добавляем первую букву в конец слова, и добавляем к концу 'ау'
# word -> ordway
# apple -> appleay

def pig_latin(word):
    first_letter = word[0]

    # проверить, является ли первая буква гласной
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

    return pig_word


a = pig_latin('apple')
print(a)





























