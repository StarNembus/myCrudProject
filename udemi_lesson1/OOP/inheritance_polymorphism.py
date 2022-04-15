# inheritance - наследование
# способ создания новых классов на основе существующих классовnimal
class Animal():

    def __init__(self):
        print('Animal created')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog created')


    def eat(self):  # переопределение родительского метода
        print('I am a dog and eating')

    def bark(self):
        print('WOOF!')


my_dog = Dog()
my_dog.eat()


# polymorphism - полиморфизм, описывает то, как различные классы объектов могут использовать одно и тоже название метода
# эти методы можно вызывать передавая различные параметры


class Dog():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says woof!'


class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says meow!'

niko = Dog('Niko')
felix = Cat('Felix')

# print(niko.speak())
# print(felix.speak())

def pet_speak(pet):
    return pet.speak()


print(pet_speak(felix))
print(pet_speak(niko))

# Абстрактные классы - классы, которые обязательно должны быть наследованы, то есть ожидается,
# что от них никогда не будут создаваться экземпляры класса, предназначен служить базовым классом

class Animal():

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')


