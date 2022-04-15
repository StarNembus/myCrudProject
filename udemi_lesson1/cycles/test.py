# написать команду, которая выведет слова начинающиес с s

st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0].lower() == 's':
        print(word)

# распечатать все четные числа с помощью range

my_list = []
for i in range(0, 10):
    if i % 2 == 0:
        my_list.append(i)
print(my_list)

# создать список  чисел от 1 до 50б  которые делятся нацело на 3 с помощью list comprehensions

my_list = [x for x in range(1, 51) if x % 3 == 0]
print(my_list)

# пройтись по словам в строке, если длина слова четная, напечатать 'Это слово имеет четную длину'
st = 'Print every word in this sentence that has an even number of letters'
my_list = st.split()
print(my_list)
for word in my_list:
    if len(word) % 2 == 0:
        print(f'Это слово ({word}) имеет четную длину')

#
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

# составить список первых букв из всех слов
st = 'Create a list of the first letters of every word in the list'
my_list = [word[0] for word in st.split()]
print(my_list)
