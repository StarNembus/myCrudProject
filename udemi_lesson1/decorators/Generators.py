# Функции - генераторы - это функции, которые возвращают значение
# и затем могут продолжить работу с того места, где они остановились в предыдущий раз
# отличие в синтаксисе - использование yield вместо return
# функция range - является генератором


# Итератор - объект перечислитель, который для данного объекта выдает следующий элемент,
# либо бросает исключение, если элементов больше нет.



def create_cubes(n):
    for x in range(n):
        yield x ** 3


for x in create_cubes(10):
    print(x)

print(create_cubes(10))


# числа Фибоначчи ряд, в котором каждое следующее число равно сумме двух предыдущих:
# генератором
def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for number in gen_fibon(10):
    print(number)

# функцией
def gen_fibon1(n):
    a = 1
    b = 1
    output = []
    for i in range(n):
        output.append(a)
        a, b = b, a + b
    return output


for number in gen_fibon(10):
    print(number)


def simple_gen():
    for x in range(3):
        yield x


for number in simple_gen():
    print(number)

g = simple_gen()

print(next(g))  #0

print(next(g))  #1

print(next(g))  #2


























