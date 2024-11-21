#Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative =[i for i in numbers if i<=0]
# print(negative)


#Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

list=[i for row1 in list_of_lists for row2 in row1 for i in row2]

# print(list)

#flatten into a lsits
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output=[
    [country.upper(),country [:3].upper(),capital.upper()]
     for sublist in countries for (country,capital) in sublist]
# print(output)


# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output=[
    { 'country': country, 'capital':capital} for sublist in countries for (country,capital) in sublist 
]

# print(output)

#Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output =[
    firstname + ''+ lastname for sublist in names for (firstname,lastname) in sublist
]

# print(output)


# Write a lambda function 

area= lambda a,b :0.5 * a * b

print(area(2,3))