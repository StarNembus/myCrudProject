""" Способ быстрого создания списков"""

# обычный способ создания списков

my_string = 'hello'
my_list = []

for letter in my_string:
    my_list.append(letter)
print(my_list)

# генератор списка!(не путать с генератором)
my_list = [letter for letter in my_string]
print(my_list)

my_list = [x for x in 'abcde']
print(my_list)

my_list = [num for num in range(0, 11)]
print(my_list)

my_list = [num ** 2 for num in range(0, 11)]
print(my_list)

my_list = [x for x in range(0, 11) if x % 2 == 0]
print(my_list)

# с генератором списка!!! (не путать с генератором)
celsius = [0, 10, 20, 34.5]
fahrenheit = [((9 / 5) * temp + 32) for temp in celsius]
print(fahrenheit)

# без генератора
fahrenheit1 = []

for temp in celsius:
    fahrenheit1.append((9 / 5) * temp + 32)
print(fahrenheit1)

# вложенный цикл
# в данном примере каждое число из верхнего цикла умножается на 3 числа из нижнего ( получается список из 9 чисел)
my_list = []

for x in [2, 4, 6]:  # допустим первая 2 получаются числа 2, 20, 2000б тоже самое для 4 и 6
    for y in [1, 10, 1000]:
        my_list.append(x * y)
print(my_list)

# с помощью генератора списка!!!(не путать с генератором), но так не принято кодить (снижается читаемость кода)
my_list = [x * y for x in [2, 4, 6] for y in [1, 10, 1000]]
print(my_list)

