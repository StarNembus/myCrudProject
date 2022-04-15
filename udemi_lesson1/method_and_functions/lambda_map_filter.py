"""Lambda выражения - одноразовые функции(функция, которую в коде хотим использовать один раз)"""

# def square(num):
#     result = num ** 2
#     return result

# lampda

square = lambda num: num ** 2
print(square(5))


names = ['Andy', 'Eve', 'Sally']
print(list(map(lambda name: name[0], names)))  # вывести 0 индекс у каждой строки в списке
print(list(map(lambda x: x[::-1], names)))


"""map"""

def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4]
my_nums1 = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
    print(item)

# lambda
print(list(map(lambda num: num ** 2, my_nums1)))


def splicer(my_string):
    if len(my_string) % 2 == 0:
        return 'EVEN'
    else:
        return my_string[0]


names = ['Andy', 'Eve', 'Sally']

x = list(map(splicer, names))
print(x)

"""filter"""


my_nums = [1, 2, 3, 4, 5]


# lambda
print(list(filter(lambda num: num % 2 == 0, my_nums)))


# без lambda
def check_even(num):
    return num % 2 == 0


print(list(filter(check_even, my_nums)))

for n in filter(check_even, my_nums):
    print(n)
