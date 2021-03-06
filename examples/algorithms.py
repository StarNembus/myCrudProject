# Bubble Sort
# сложность O(n2)

# Задача:
# поступает число n - количество элементов в списке
# затем список
# вывести отсортированный список по возрастанию и какое количество раз пришлось переставлять элементы местами
n = int(input())
mass = list(map(int, input().split()))
# n = 6  # из скольки элементов у нас состоит массив
# mass = [5, 7, 4, 3, 8, 2, 9]
count = 0  # количество замен
# необходимо добавить внешний цикл для обхода(количество повторений для получения результата
# будет равняться количеству элементов -1 (5 повторений для получения результата)
for run in range(n - 1):
    # код для одного обхода
    for i in range(n - 1 - run):  #  n - 1 (не берем последний элемент) (- run, чтобы не сравнивать с последними уже отсортированными числами)
        if mass[i] > mass[i + 1]:  # если текущий элемент больше чем его соседний элемент справа, меняем их местами
            count += 1
            mass[i], mass[i + 1] = mass[i + 1], mass[i]
print(*mass)  # распаковка массива
print(count)

# fib_dict = {0: 0, 1: 1}
#
#
# def fib(n):
#     if n in fib_dict:
#         return fib_dict[n]
#     fib_dict[n] = fib(n - 1) + fib(n - 2)
#     return fib_dict[n]
#
#
# def f(x):
#     if x == 0:
#         return None
#     if x == 1:
#         return 0
#     my_list = [0]
#     i = 2
#     while True:
#         t = fib(i)
#         if t % 2 == 0:
#             my_list.append(t)
#             if len(my_list) == x:
#                 return my_list
#         i = i + 1
#
#
# print(f(4))
