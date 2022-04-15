""" range"""
# my_list = [1, 2, 3]

for num in range(0, 10, 2):  # start, stop, step
    print(num)

# Генератор - особый тип функции, который генерирует информацию, при этом не сохраняет ее полностью в памяти

"""enumirate"""

word = 'abcde'
for item in enumerate(word):
    print(item)

# for index, letter in enumerate(word):
#     print(index)
#     print(letter)
#     print('\n')

# index_count = 0
#
# for letter in 'abcde':
#     print('At index {} the letter is {}'.format(index_count, letter))
#     index_count += 1

"""zip - соединяет списки вместе"""

my_list1 = [1, 2, 3, 4, 5]
my_list2 = ['a', 'b', 'c', 'd', 'e']

for item in zip(my_list1, my_list2):  # ориентруется на самый короткий список, если списки разно длины
    print(item)

""" оператор in """

# d = {'mykey': 345}
# 345 in d.keys()

