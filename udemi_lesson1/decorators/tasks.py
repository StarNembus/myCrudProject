print(str('Hello Python!')[3])

my_str = 'Hello Python!'

print(my_str[:2])
print(my_str[:-11])
print(str('z' * 7))
print(str('z' * 7).upper())


greeting = 'Hello Python!'
path = greeting[6] + 'a' + greeting[8:10]
print(path)

my_list = [1, 2, 'string', 4.5, 34.5]

new_list = my_list[:3]
print(new_list)

sum_numbers = 0
for x in range(10, 31):
    if x % 2 == 0:
        sum_numbers += x
print(sum_numbers)

