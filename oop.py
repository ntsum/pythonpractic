mylist = [1, 2, 3]
myset = set()
type(set)
type(list)


class Dog():
    species = 'mammal'
# attribute
    def __init__(self, breed, name):

        self.breed = breed
        self.name = name
# method is an action the object can take

    def bark(self):
        print("WOOF! My name is {} and I am a {}".format(self.name, self.breed))


my_dog = Dog(breed='Basset Hound', name='Walnut')
print(type(my_dog))
print('My dog ' + my_dog.name + ' is a ' + my_dog.breed)

print(my_dog.bark())


class Circle():
    pi = 3.14
    def __init__(self, radius=30):

        self.radius = radius

    def get_circumfrance(self):
        return self.radius * self.pi * 2


my_circle = Circle()
print(my_circle.get_circumfrance())
