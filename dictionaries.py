# dictionaries are objects retrieved by key name, unordered and cant be sorted and lists are retrieved by location can be indexed or sliced
my_dictionary = {'key': 'value', 'key2': 'value2'}
print(my_dictionary)

price_lookup = {'apple': 2.99, 'kiwi': 5.99, 'avocado': 10.99}
print(price_lookup)
print(price_lookup['avocado'])

d = {'k1': 123, 'k2': [1, 2, 3]}
print(d)

d['k3'] = 500
print(d)

# tuples are almost like lists except they are IMMUTABLE
# if an element is assigned in a tuple, cannot be changed
# uses parenthasis

mytuple = (1, 2, 3)
mylist = [1, 2, 3]
print(len(mytuple))
mytuple.count(1)
