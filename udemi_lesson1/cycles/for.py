"""Термин 'итерируемый' (iterable) означает, что можно выполнять действия для каждого отдельного элемента в объекте"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in my_list:
#     print('hello')

for num in my_list:  # для каждого числа в списке
    if num % 2 == 0:  # если число четное (остаток от деления на 2 равен 0)
        print(num)  # вывести список четных чисел
    else:
        print(f'Odd number: {num}')

# суммарное значение элементов списка

sum_my_list = 0

for num in my_list:
    sum_my_list = sum_my_list + num

print(sum_my_list)

my_list = [(1, 2), (3, 4)]
for item in my_list:
    print(item)

# распаковка кортежа

for a, b in my_list:
    print(a)
    print(b)

# распаковка словаря
d = {'key1': 1, 'key2': 2}

for item in d.items():
    print(item)

for key, value in d.items():
    print(value)

# break - выход из ближайшего цикла, содержащего эту команду,
# continue - переход в начало ближайшего цикла, содержащего эту команду

my_string = 'Sammy'
for letter in my_string:
    if letter == 'a':
        continue
    print(letter)

for letter in my_string:
    if letter == 'a':
        break
    print(letter)
