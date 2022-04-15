# Задача 1
# OLD MACDONALD: Напишите функцию, которая переводит в верхний регистр первую и четвёртую буквы имени.

# Решение
def old_macdonald(name):
    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]

    return first_letter.upper() + inbetween + fourth_letter.upper() + rest


x = old_macdonald('macdonald')
print(x)


# Решение с помощью capitalize()
# 'macdonald'.capitalize() возвращает 'Macdonald' переводит первую букву в верхний регистр
def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]

    return first_half.capitalize() + second_half.capitalize()


x = old_macdonald('macdonald')
print(x)


# Задача2
# master_yoda: На входе фраза, на выходе вернуть слова в обратном порядке.
# Замечание: здесь может пригодиться метод .join(). Этот метод позволяет соединять строки, используя определенный разделитель. Вот пример для метода .join():
#
# >>> "--".join(['a','b','c'])
# >>> 'a--b--c

# Это значит, что если у Вас есть список слов и Вы хотите составить из них фразу, то можно соединить их, используя в качестве разделителя пробел:
#
# >>> " ".join(['Hello','world'])
# >>> "Hello world"

def master_yoda(text):
    wordlist = text.split()
    reverse_wordlist = wordlist[::-1]

    return ' '.join(reverse_wordlist)


x = master_yoda('I am home')
print(x)


# Задача3
# almost_there: на входе число n, вернуть True если n находится не далее чем на 10 от чисел 100 или 200.
# abs(num) возвращает абсолютное значение числа


def almost_there(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)


x = almost_there(104)
print(x)

y = almost_there(150)
print(y)
