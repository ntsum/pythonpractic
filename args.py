#args and kwargs


def myfunc(*args):
    return sum(args) * 0.05


print(myfunc(40, 60, 50, 600, 300, 500))


def myfun(**kwargs):
    if 'dog' in kwargs:
        print('My pet of choice is {}'.format(kwargs['dog']))
    else:
        print('no food')


print(myfun(dog='walnut', cat='lulu'))
