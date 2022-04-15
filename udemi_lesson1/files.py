my_file = open('file.txt')
print(my_file)  # <_io.TextIOWrapper name='file.txt' mode='r' encoding='UTF-8'>
print(my_file.read())
print(my_file.read())  # данных не будет
print(my_file.seek(0))
print(my_file.read())  # вновь увидим содержимое
print(my_file.seek(0))
print(my_file.readlines())  # отдельные элементы ['Первая строка\n', 'Вторая строка\n', 'Третья строка']

my_file = open("/home/kwazart/Документы/test.txt")
print(my_file.read())
my_file.close()
print(my_file.close())

# чтобы не закрывать файл в ручную

with open('file.txt', mode='r') as my_new_file:
    contents = my_new_file.read()

print(contents)

""" Чтение, запись и добавление в файл"""

# mode='r' - только чтение
# mode='w' - только запись(перезаписывает файл или создает новый)
# mode='a' - только добавление к уже существующему файлу
# mode='r+' - чтение и запись
# mode='w+' - запись и чтение(перезаписывает файл или создает новый)

# Базовая практика:
#
# http://codingbat.com/python
#
# Дополнительная практика, больше математики (и сложнее) :
#
# https://projecteuler.net/archives
#
# Список практических задач:
#
# http://www.codeabbey.com/index/task_list
#
# SubReddit, посвящённый ежедневным практическим задачам:
#
# https://www.reddit.com/r/dailyprogrammer
#
# Очень интересный сайт с разными подсказками и задачами (не для начинающих, но тем не менее интересный сайт)
#
# http://www.pythonchallenge.com/