"""Объектно - ориентированное программирование позволяет создавать свои объекты с методами и атрибутами"""
# ООП - позволяет создавать структурированный код, который можно использовать повторно

# каждый экземпляр - это конкретный объект, созданный из этого класса
# class - набор методов и атрибутов, которые будут определять содержание экземпляров класса

class Dog():
	# создание атрибутов
# метод init создается автоматически при создании экземпляра класса
	def __init__(self, mybreed, name, ):
		self.mybreed = mybreed  # атрибут класса внутри экземпляра класса


my_dog = Dog(mybreed='Lab')
a = my_dog.mybreed
print(a)
