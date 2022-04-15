
"""Списки - упорядоченные последовательности, которые могут содержать различные типы объектов"""
# Изменяемый тип данных

my_list = [1, 2, 3]

my_list1 = ['string', 2, 3.8, True]

print(len(my_list))
print(len(my_list1))

# конкатенация
my_list = ['one', 'two', 'three']
another_list = ['four', 'five']
print(my_list + another_list)

new_list = my_list + another_list
print(new_list)

# меняем список
new_list[0] = 'ONE'
print(new_list)

# добавить элемент в конец списка append
new_list.append('six')
print(new_list)

# удалить элемент с конца списка - pop
new_list.pop()
print(new_list)

new_list.pop(2)  # удалить элемент с индексом 2
print(new_list)

# метод sort

my_list = ['a', 'c', 'b', 'n']
num_list = [1, 3, 5, 4]

my_list.sort()  # ['a', 'b', 'c', 'n']
print(my_list)

# отсортированный список в новое значение
my_list = ['a', 'c', 'b', 'n', 'd']
my_list.sort()
my_list2 = my_list
print(my_list2)  # ['a', 'b', 'c', 'd', 'n']

num_list.sort()  # [1, 3, 4, 5]
print(num_list)


# метод reverse
num_list.reverse()
print(num_list)  # [5, 4, 3, 1]

