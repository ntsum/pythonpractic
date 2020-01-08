x = 25


def printer():
    x = 50
    return x


print(x)  # prints 25

print(printer())  # prints 50

# LEGB rule
#L: Local
#E: Enclosing
#G: Global
# B: Built-in

#lambda num:num**2
# local

name = 'THIS IS A GLOBAL STRING'
# global


def greet():

    name = 'Sammy'
    # enclosing

    def hello():
        name = "i'm local"
        print("Hello " + name)

    hello()


greet()
