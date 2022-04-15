"""Словари - неупорядоченные мвппинги для хранения объектов. Словари хранят пары ключ-значение"""
# изменяемый тип данных

my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict)

# получить значение ключа
print(my_dict['key1'])  # value1

prices_lookup = {'apple': 2.99, 'oranges': 4.25, 'milk': 5.80}
print(prices_lookup['apple'])  # 2.99

d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': 100}}
print(d['k2'])  # [0, 1, 2]
print(d['k3']['insideKey'])  # 100

# заменяем данные

my_dict = {'key1': ['a', 'b', 'c']}
print(my_dict)

my_list = my_dict['key1']
print(my_list)  # ['a', 'b', 'c']

letter = my_list[2]
print(letter)  # c

print(letter.upper())

print(my_dict['key1'][2].upper())  # C

# добавляем новую пару - ключ: значение


d = {'k1': 100, 'k2': 200}
d['k3'] = 300
print(d)  # {'k1': 100, 'k2': 200, 'k3': 300}

# изменяем данные значения в словаре, значение может быть разных типов данных
d['k1'] = True
print(d)  # {'k1': True, 'k2': 200, 'k3': 300}
d['k1'] = 500
print(d)  # {'k1': 500, 'k2': 200, 'k3': 300}


""" Методы"""

# метод для получения всех значений в словаре .keys()
print(d.keys())  # dict_keys(['k1', 'k2', 'k3'])

# получение всех значений .values()
print(d.values())  # dict_values([500, 200, 300])

# получение пар ключ значение из словаря .items()
print(d.items())  # dict_items([('k1', 500), ('k2', 200), ('k3', 300)])








