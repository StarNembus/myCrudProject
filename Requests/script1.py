import requests
"""Скачаем изображение с сайта"""
image = requests.get('https://learn.python.ru/media/projects/sl1_Cj4bKxp.png')
with open('new_image.png', 'wb') as f:
    f.write(image.content)