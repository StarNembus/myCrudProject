# def decorator_func():
#     pass
#
#
# @decorator_func
# def func(x):
#     print('String')
#     return x * x + 1
# пример итератора, метод next, итератор - объект i
l = (1, 2, 3, 4, 5)

for i in l:
    print(i)


# пример list comprehensions
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]  # Пусть у нас есть исходный список
list_b = [x for x in list_a]  # Создадим новый список используя генератор списка
print(list_b)  # [-2, -1, 0, 1, 2, 3, 4, 5]

# x - это финальное выражение
# for x in list_a - цикл, где берется текущее значение, выдаваемое итератором x

# if x % 2 == 0 - остаток от деления на 2 равен нулю - число четное
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_b = [x for x in list_a if x % 2 == 0]
print(list_b)  # [-2, 0, 2, 4]


# if x % 2 == 0 - дополнительное условие

# генератор
# Генераторы - они написаны как обычные функции, но используют yield оператор всякий раз, когда хотят вернуть данные.
# Каждый раз, когда он next()вызывается,
# генератор возобновляет работу с того места, где он остановился
# (он запоминает все значения данных и какой оператор был выполнен последним).
def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]

# # Один из способов получения значений из генератора — это их перебрать в цикле for
a = reverse('frog')
for b in a:
    print(b)

# Генераторные выражения( синтаксис - круглые скобки) # генератор возобновляет работу с того места, где он остановился
a = sum(i*i for i in range(10))
print(a)
