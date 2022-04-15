# """Строки - неизменяемый тип данных"""
# my_string = 'Hello world'
# print(my_string)
# print(my_string[-2])
#
# my_string = 'abcdefghijklmnopqrstuvwxyz'
# print(my_string[2:])
# print(my_string[:3])
# print(my_string[3:6])
# print(my_string[2:7:2])
#
# """ Свойства и методы строк """
#
# x = 'Hello world'
# y = x + ' it is beautiful outside!'
# print(y)
#
# letter = 'z'
# z = letter * 10
# print(z)
#
# x = 'Hello world'
# y = 'Hello this is a string'
# # x = x.upper()  # переводит в верхний регистр
# x = x.split()  # разделяет строку на отдельные части ( создает список из строки)
# y = y.split()
# print(x)
# print(y)
import re


# def PalindromTwo(strParam):
#     a = re.sub(r'[-:;?! .,=+]', '', strParam.lower())[:: -1]
#     b = re.sub(r'[-:;?! .,=+]', '', strParam.lower())
#     return re.sub(r'[-:;?! .,=+]', '', strParam.lower()) == re.sub(r'[-:;?! .,=+]', '', strParam.lower())[:: -1]
#
# strParam = 'Noel - sees Leon'
# ans = PalindromTwo(strParam)
# print(ans)

strArr = ['1, 3, 4, 7, 13', '1, 2, 4, 13, 15']
ChallengeTocken = 'wd6ms1i5a'

a = strArr[0].split(', ')
b = strArr[1].split(', ')
c = []
for i in range(len(a)):
    if a[i] in b:
        c.append(a[i])

res = ','.join(c) + ChallengeTocken
str_res = ''
for j in range(len(res)):
    if (j + 1) % 4 == 0:
        str_res += '_'
    else:
        str_res += res[j]

print(str_res)







# def find(strArr):
#     strArr = ['1, 3, 4, 7, 13', '1, 2, 4, 13, 15']
#     return strArr



















