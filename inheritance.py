class Animal():
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


myanimal = Animal()


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):
        print("I am a dog bork")

    def bark(self):
        print("bork bork woof woof")


mydog = Dog()
print(mydog.bark())

# while functions can take in different arguments, methods belong to the objects.


class Book():

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")


b = Book('python rocks', 'mary', 200)

print(b)
del b
