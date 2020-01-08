# functions allow code to be repeated many times
# def name_of_function():
# functions can take in parameters
# return allows us to assign the output to a new variable


def name_function(name='SHUTUP'):
    return "Hello " + name


result = name_function('Mary')
print(result)

# find out if the word dog is in a string


def dog_check(mystring):
    if 'dog' in mystring:
        return True
    else:
        return False


print(dog_check('My dog ran away'))


def pig_lation(word):

    first_letter = word[0]

    # check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

    return pig_word


print(pig_lation('orange'))
