# fib = {0: 0, 1: 1}
#
#
# def find_fib(n):
#     if n in fib:
#         return fib[n]
#     fib[n] = find_fib(n - 1) + find_fib(n - 2)
#     return fib[n]
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
#         t = find_fib(i)
#         if t % 2 == 0:
#             my_list.append(t)
#             if len(my_list) == x:
#                 return my_list
#         i = i + 1
#
#
# print(f(4))

list1 = [1, 2, 3]
list2 = list1
list1[0] = 100
print(list2)

list1 = [1, 2, 3, 4]
del list1[1:2]
print(list1)

var = [i ** 2 for i in [1, 3, 5]]
print(var)

