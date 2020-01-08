def square(num):
    return num**2


my_nums = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
    print(item)

list(map(square, my_nums))


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'Even'
    else:
        return mystring[0]


names = ['Mary', 'Cara', 'Sam']
print(list(map(splicer, names)))


def check_even(number):
    return number % 2 == 0


mynums = [1, 2, 3, 4, 5, 6]

for n in filter(check_even, mynums):
    print(n)


lambda num: num ** 2


mynums = [1, 2, 3, 4, 5, 6]
# lambda expression or anonymous function
# MY FIRST LAMBDA EXPRESSION AYYYYYYYY
list(map(lambda num: num**2, mynums))
