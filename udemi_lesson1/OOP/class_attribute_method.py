
class Dog():
    # атрибуты на уровне класса
	species = 'mammal'

	def __init__(self, breed, name):
		self.breed = breed
		self.name = name
		# self.spots = spots

	# методы класса(функции) используются для выполнения различных действий с объектом
	def bark(self):
		print('WOOF! My name is {}'.format(self.name))


my_dog = Dog('Lab', 'Sam')
# a = my_dog.species
my_dog.bark()  # метод
# print(a)

class Circle():

# class object attribute
	pi = 3.14
# constructor
	def __init__(self, radius=1):  # radius - атрибут в конструкторе
		self.radius = radius
		self.area = radius * radius * self.pi  # новый атрибут, формула расчета площади круга
		self.area = radius * radius * Circle.pi  # новый атрибут, вариант написания, который могут использовать другие программисты


	# method вычисления окружности
	def get_circle(self):
		return self.radius * self.pi * 2

# создаем экземпляр круга
my_circle = Circle()

# my_a = my_circle.radius
# print(my_a)
# a = my_circle.pi
# print(a)
print(my_circle.get_circle())





