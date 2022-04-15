# Задача1
# Напишите функцию, которая берёт список чисел, и возвращает True,
# если в списке содержатся числа 0 0 7 в указанном порядке

def spy_game(nums):
    code = [0, 0, 7, 'x']
    # 0, 7, 'x'
    # 7, 'x'
    # 'x' lenght = 1
    for num in nums:
        if num == code[0]:
            code.pop(0)

    return len(code) == 1


x = spy_game([1, 2, 4, 0, 0, 7, 5])
print(x)

y = spy_game([1, 0, 2, 4, 0, 5, 7])
print(y)

z = spy_game([1, 7, 2, 0, 4, 5, 0])
print(z)


# Задача 2
# count_primes: Напишите функцию, которая возвращает количество простых чисел, которые меньше или равны указанному числу.
# count_primes(100) --> 25

def count_primes(num):
    # проверка на 0 и 1
    if num < 2:
        return 0

    # проверка на 2 и больше

    # список для хранения простых чисел
    primes = [2]

    # счетчик
    x = 3

    # x пробегает значения от числа 3 до числа num
    while x <= num:
        # проверяем является ли число x простым
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


z = count_primes(100)
print(z)
