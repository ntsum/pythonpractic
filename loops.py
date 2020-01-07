from random import shuffle
mystring = "Hello World"

for letter in mystring:
    print(letter)

d = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}

for key, value in d.items():
    print(value)


x = 0

while x < 5:
    print(f'The Current value of x is {x}')
    x = x + 1
else:
    print("x is not less than five")

# pass continue break

dog = ['walnut', 'cashew', 'oscar', 'sophie', 'rocky']
dog.append('lulu isnt a dog')
print(dog)

yawning = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15]
shuffle(yawning)
print(yawning)

input('Enter a number:')
# input always accepts every input as a string transform by float or int for number or decimal

# list comprehensions
