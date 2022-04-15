animals = ['Dog', 'Cat', 'Bird', 'Fish']
# Поиск значения в списке с помощью цикла for

for animal in animals:
    if animal == 'Cat':
        print('Mey')

# с помощью оператора in

# element in list
if 'Cat' in animals:
    print('Mey')

# с помощью оператора not in
# Он возвращает True, если элемент не присутствует в последовательности.

if 'Wolf' not in animals:
    print('Wow')

#  с помощью lambda
# Еще один способ проверить, присутствует ли элемент — отфильтровать все, кроме этого элемента
# Встроенный метод filter() принимает в качестве аргументов лямбда-функцию и список.
# Здесь мы можем использовать лямбда-функцию для проверки нашей строки «Bird» в списке animals.
# Затем мы оборачиваем результаты в list(), так как метод filter() возвращает объект filter, а не результаты.
# Если мы упакуем объект filter в список, он будет содержать элементы, оставшиеся после фильтрации:

elements = list(filter(lambda x: 'Bird' in x, animals))
print(elements)

# с помощью функции any
# возвращает True или False в зависимости от наличия или отсутствия элемента:
if any(element in 'Bird' for element in animals):
    print('Weeeee!')

# найти число и его индекс в списке
my_list = [1, 2, 555, 446, 3, 5, 10, 999, 1000]
for i in my_list:
    if i == 1:
        print(my_list.index(i))

# сортировка
# отсортированные списки чисел a и b, надо составить список с, который будет включать значения списка а, которых
# нет в списке b за линейное время

a = [1, 2, 3, 5]
b = [5, 6, 7, 8]
c = list(set(a) - set(b))
print(c)

my_list2 = []
for i in range(10):
    my_list2.append(i)
print(my_list2)

my_list2 = [i for i in range(1, 10) if i % 2 == 0]
print(my_list2)
print(my_list2)

my_list3 = (i for i in range(12) if i % 2 == 0)

for i in my_list3:
    print(i, end=' ')

# Список сразу удерживает в памяти определенное число значений.
# А генератор в каждый отдельный момент удерживает только одно значение — то, которое он возвращает.
