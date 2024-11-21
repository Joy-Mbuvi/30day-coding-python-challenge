# a set i a collection of unordered and un-indexed dictinct elements

st=set()

'use .add to add things to a set'
#we can join sets using the union() or update() method

# fruits={'banana','orange','lemon','mango'}
# vegetables={'kale','spinach','carrots','bellpeppers'}

# shopping=fruits.union(vegetables)

# print(shopping)

fruits={'banana','orange','lemon','mango'}
vegetables={'kale','spinach','carrots','bellpeppers'}

fruits.update(vegetables)

print(fruits)


#intersection returns a set of items which are in both sets

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}


# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
str='I am a teacher and I love to inspire and teach people'
words=str.split()

unique_words=set(words)


#remember sets do not allow duplicates
print('unique words:',unique_words)
