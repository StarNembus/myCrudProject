# def get_age(age):
#     return int(age.split()[0])
#
#
# a = get_age('2 years old')
# print(a)



# from itertools import groupby

# def unique_in_order(iterable):
#     return [k for k, g in groupby(iterable)]
#
#
# a = unique_in_order('AAAABBBCCDAABBB')
# a_1 = unique_in_order('ABBCcAD')
# a_2 = unique_in_order([1, 2, 2, 3, 3])
# print(a)
# print(a_1)
# print(a_2)






def sum_dig_pow(a, b):
    my_list = []  # пустой список
    for i in range(a, b + 1):  # проходимся по списку + 1 чтобы захватить в список диапозон чисел включительно
        y = sum(int(j) ** (idx + 1) for idx, j in enumerate(str(i)))   #  enumerate() – индекс элемента и его значение.
        if y == i:
            my_list.append(i)
    return my_list

# Функция enumerate() применяется для так называемых итерируемых объектов (список относится к таковым)
# и создает объект-генератор, который генерирует кортежи, состоящие из двух элементов – индекса элемента и самого элемента.


 












