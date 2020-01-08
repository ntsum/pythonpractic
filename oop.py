mylist = [1, 2, 3]
myset = set()
type(set)
type(list)


class Dog():

    def __init__(self, breed, name, spots):

        self.breed = breed
        self.name = name
        self.spots = spots


my_dog = Dog(breed='Basset Hound', name='Walnut', spots=True)
print(type(my_dog))
print('My dog ' + my_dog.name + ' is a ' + my_dog.breed)
