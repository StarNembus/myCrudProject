import requests

result = requests.get('https://scotch.io')

print(result)

# Этот код просто отправляет запрос GET на сайт Scotch.io
# Для отправки запроса нужно запустить файл script.py.

if result:
    print('Response OK')
else:
    print('Response Failed')

print(result.status_code)


# Также в ответе вы можете получить заголовки. Вы можете посмотреть их, используя словарь headers для объекта response.
# print(result.headers)

# Если мы посмотрим на файл res.text (это работает для текстовых данных, таких как просматриваемая нами страница HTML),
# мы увидим весь код HTML, требуемый для построения домашней страницы Scotch.
print(result.text)