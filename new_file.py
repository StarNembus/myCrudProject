from __future__ import print_function

import os
import io

word = 'CI/CD'
directory = '/home/kwazart/Рабочий стол/txt'

my_files = os.listdir(directory)
# result = my_files.endswith('sql')
print(my_files)


def open_find_word():
    for file in my_files:
        with open(os.path.join(directory, file), 'r') as f:
            text = f.read()
        if word in text:
            print(word, file)


open_find_word()


def find_files():
    my_files = os.listdir(directory)
