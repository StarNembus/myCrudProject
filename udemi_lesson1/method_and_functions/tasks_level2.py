# Задача1

# Найти 33: На входе список чисел, вернуть True если массив содержит где-нибудь 3 рядом с 3.


def has_33(nums):
    # нужны элементы от нуля, до количества элементов в списке(len(nums)) сравниваем как очередной,так и следующий элемент,
    # для последнего элемента нет последующего, поэтому в цикле берем до предпоследнего элемента (len(nums)) - 1
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True

    return False


x = has_33([1, 3, 3])
print(x)

x = has_33([1, 3, 1, 3])
print(x)

x = has_33([3, 1, 3])
print(x)


# Задача2

# paper_doll: На входе строка, вернуть строку где каждый символ исходной строки повторяется три раза.
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'


def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3

    return result


x = paper_doll('Hello')
print(x)
x = paper_doll('Mississippi')
print(x)


# Задача3

# blackjack: На входе три числа от 1 до 11. Если их сумма меньше или равна 21, то вернуть их сумму.
# Если сумма больше 21 и среди чисел есть 11, то уменьшить общую сумму на 10.
# И наконец, если сумма (в том числе после уменьшения) превышает 21, вернуть 'BUST'.
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19


def blackjack(a, b, c):
    if sum([a, b, c]) <= 21:
        return sum([a, b, c])
    elif 11 in [a, b, c] and sum([a, b, c]) - 10 <= 21:
        return sum([a, b, c]) - 10
    else:
        return 'BUST'


x = blackjack(5, 6, 7)
print(x)
y = blackjack(9, 9, 9)
print(y)
z = blackjack(9, 9, 11)
print(z)


# Задача4

# summer_69: Вернуть сумму чисел в массиве,
# кроме набора чисел который начинается с 6 и продолжается до 9 (для каждого числа 6 далее где-то будет число 9).
# Вернуть 0 если чисел нет.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14


def summer_69(arr):
    total = 0  # переменная для накопления суммы элементов
    add = True

    for num in arr:  # проходимся по массиву значение True означает, что нам нужно суммировать числа, False - нет
        while add:  # находимся в режиме суммирования # здесь потенциально можно встретить число 6
            if num != 6:   # если число не равно 6
                total += num   # суммируем данные
                break
            else:    #  иначе переходим в режим игнорирования чисел, не суммируем
                add = False
        while not add:  # если мы находимся в режиме игнорирования чисел
            if num != 9:
                break  # ждем число 9, пока оно не встретилось игнорируем другие числа
            else:   # если число встретилось
                add = True  # переключаемся в режим суммирования чисел
                break
    return total


x = summer_69([1, 3, 5])
print(x)

y = summer_69([4, 5, 6, 7, 8, 9])
print(y)

z = summer_69([2, 1, 6, 9, 11])
print(z)
