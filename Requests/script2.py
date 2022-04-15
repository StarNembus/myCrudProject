"""Загрузим файл на сервер
Для следующего примера воспользуемся сайтом для тестирования HTTP запросов Webhook.site.
В качестве URL мы будем использовать ссылку, которая генерируется на сайте автоматически.
."""
import requests
url = 'https://webhook.site/86b0f59f-afb4-4822-9a5d-f0c9604f793d'
with open('test.txt', 'w') as f:
    f.write('текст для проверки загрузки файла')

with open('test.txt', 'rb') as f:
    r = requests.post(url, {'files': f})
    print(r)

