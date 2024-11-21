
# # syntax
# # [i for i in iterable if expression]

# #example

# # languange= 'Python'
# # lst= [i for i in languange]
# # print(lst)

# #generating a list of numbers

# numbers= [i for i in range (13)]
# # print (numbers)

# #mathematical operations

# squares= [i * i for i in range (11)]
# # print (squares)

# #making a list of tuples
# coordinates= [(i,i *i) for i in range (9)]
# # print(coordinates)

# #using the if statement

# #generating even numbers

# even_numbers= [i for i in range (21) if i % 2==0]
# print(even_numbers)

# odd_numers= [i for i in range (21) if i % 2 != 0]
# print(odd_numers)


##Lambda function - its does not have a return 
#To create a lambda function we use lambda keyword followed by a parameter(s), followed by an expression. See the syntax and the example below. 
# Lambda function does not use return but it explicitly returns the expression.



x= lambda param1, param2,param3 : param1+param2+param1


#named function

def add_sum(a,b):
    return a+b


#lambda function

add_sum=lambda a, b : a+b



