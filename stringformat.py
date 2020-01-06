# .format() and f-strings
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

result = 100/777
print("The result was {r:1.3f}".format(r=result))

# f-strings
name = "Jose"
print(f'Hello, his name is {name}')
