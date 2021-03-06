from threading import Thread
import time


def remind():
    # Спрашиваем текст напоминания, который нужно потом показать пользователю
    print('О чем вам напомнить?')
    # Ждём ответа пользователя и результат помещаем в строковую переменную text
    text = str(input())
    # Спрашиваем про время
    print('Через сколько минут?')
    # Тут будем хранить время, через которое нужно показать напоминание
    local_time = float(input())
    # Переводим минуты в секунды
    local_time = local_time * 60
    # Ждём нужное количество секунд, программа в это время ничего не делает
    time.sleep(local_time)
    # Показываем текст напоминания
    print(text)


    # Создаём новый поток
th = Thread(target=remind, args=())
    # И запускаем его
th.start()

# Пока работает поток, выведем что-то на экран через 20 секунд после запуска
time.sleep(20)
print("Пока поток работает, мы можем сделать что-нибудь ещё.\n")
