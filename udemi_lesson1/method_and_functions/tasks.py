# Задача 1
# Напишите функцию, которая возвращает меньшее из двух чисел, если оба эти числа чётные.
# Иначе возвращает большее из двух чисел, если одно или оба числа нечётные.
def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        # оба числа четные
        if a < b:
            result = a
        else:
            result = b
    else:
        # одно или оба числа нечетные
        if a > b:
            result = a
        else:
            result = b

    return result


my_result = lesser_of_two_evens(2, 4)
print(my_result)


# решение с помощью min, max (такой вариант решения возможен только для 2х чисел)
def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        # оба числа четные
        return min(a, b)
    else:
        # одно или оба числа нечетные
        return max(a, b)


# Задача 2
# animal_crackers: Напишите функцию, которая получает на входе строку из двух слов,
# и возвращает True если оба слова начинаются с одной и той же буквы.

def animal_crackers(text):
    my_list = text.lower().split()
    first = my_list[0]
    second = my_list[1]

    return first[0] == second[0]


animal_crackers('Levelheaded Llama')
animal_crackers('Crazy Kangaroo')

my_result = animal_crackers('Levelheaded Llama')
my_result2 = animal_crackers('Crazy Kangaroo')
print(my_result)
print(my_result2)

# Задача 3
# makes_twenty: На входе два числа, функция возвращает True если сумма этих чисел равна 20,
# или если одно из чисел равно 20. В противном случае, возвращает False.


def makes_twenty(a, b):
    if a + b == 20 or a == 20 or b == 20:
        return True
    else:
        return False

# вариант решения


def makes_twenty1(a, b):
    return (a + b) == 20 or a == 20 or b == 20


x = makes_twenty(2, 3)
print(x)
