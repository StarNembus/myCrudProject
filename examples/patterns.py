# Observer - паттерн наблюдатель
# используется когда существует 2 объекта наблюдающий и наблюдаемый,
# предназначен для организации системы оповещений наблюдающего объекта об изменениях состояния наблюдаемого объекта.
# Push система наблюдаемый объект сообщает наблюдателю об изменениях
from abc import ABC, abstractmethod


# Реализация(менеджер уведомлений и подписчики)

class NotificationManager:  # Notification - уведомление
    def __init__(self):
        self._subscribes = set()  # подписываемся на уведомления менеджера

    def subscribe(self, subscriber):  # добавляет подписчика в список
        self._subscribes.add(subscriber)

    def unsubscribe(self, subscriber):  # удаляет подписчика из списка
        self._subscribes.remove(subscriber)

    def notify(self, message):  # метод отправки уведомлений
        for subscriber in self._subscribes:
            subscriber.update(message)  # update метод для отправки сообщений для subscriber - подписчик

        """Абстрактный наблюдатель"""


class AbstractObserver(ABC):  # наследуется от абстрактного класса
    # def __init__(self, name): !!! приватные поля не наследуются !!!
    #     self._name = name

    @abstractmethod
    def update(self, message):  # пустой метод update
        pass

        """ Реализации """


class MessageNotifier(AbstractObserver):  # notifier - уведомляет о том, что пришло сообщение
    def __init__(self, name):
        self._name = name

    def update(self, message):
        print(f"{self._name} received message!")  # сообщение пришло!


class MessagePrinter(AbstractObserver):  # printer - печатает сообщения

    def __init__(self, name):
        self._name = name

    def update(self, message):
        print(f"{self._name} received message: {message}")


# объекты

notifier = MessageNotifier("Notifier1")
printer1 = MessagePrinter("Printer1")
printer2 = MessagePrinter("Printer2")

manager = NotificationManager()

# подписываем наблюдателей к менеджеру

manager.subscribe(notifier)  # Notifier1 received message! получил сообщение
manager.subscribe(printer1)  # Printer1 received message: Hello! получил и распечатал
manager.subscribe(printer2)  # Printer2 received message: Hello!

# для того, чтобы отправить уведомление вызываем метод notify

manager.notify("Hello!")


# """ Decorator """

# Описание животных
class Creature(ABC):
    @abstractmethod
    def feed(self):  # feed - кормить
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def make_noise(self):  # make_noise - шуметь
        pass


class Animal(Creature):

    def feed(self):  # feed - кормить
        print("I eat grass")  # Я ем траву

    def move(self):
        print("I walk forward")  # Я иду вперед

    def make_noise(self):  # make_noise - шуметь
        print("WOOOOOO!")


class AbstractDecorator(Creature):

    def __init__(self, base):
        self.base = base  # сохраняем базовый объект  в пересенную

    def move(self):
        self.base.move()

    def feed(self):
        self.base.feed()

    def make_noise(self):
        self.base.make_noise()


class Swimming(AbstractDecorator):
    def move(self):
        print("I swim forward")

    def make_noise(self):
        print("...")


class Predator(AbstractDecorator):  # Predator - хищник
    def feed(self):
        print("I eat other animals")


class Fast(AbstractDecorator):
    def move(self):
        self.base.move()
        print("fast!")


# создаем животное

animal = Animal()
animal.move()
animal.feed()
animal.make_noise()

swimming = Swimming(animal)

swimming.move()
swimming.feed()
swimming.make_noise()

predator = Predator(swimming)
predator.move()
predator.feed()
predator.make_noise()

fast = Fast(predator)
fast.move()
fast.feed()
fast.make_noise()

faster = Fast(fast)
faster.move()
faster.feed()
faster.make_noise()

# снять декоратор
# спускаемся по классам вниз,хотим снять класс хищника
faster.base.base = faster.base.base.base

faster.move()
faster.feed()
faster.make_noise()
