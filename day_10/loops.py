# #   # syntax
# # while condition:
# #     code goes here


# # language='Python'
# # #for loop with string
# # for i in range (len(language)):
# #     print(language[i])

# # #for loop with list

# # numbers=[1,2,3,4,5]

# # for number in numbers:
# #     print(number)

# # exercises
# # for number in  range(11):
# #     print(number)

# # number= 0
# # while number < 11:
# #     print(number)
# #     number +=1

# # for i in range (1,8):
# #     print('#' * i)  

# # i = 1

# # while i < 7 :
# #     print ('#' * i)
# #     i += 1


# # for i in range(8): #for row
# #     for j in range(8): #for columns
# #         print('#', end="")
# #     print()

# # for number in range(11):
# #  print(f'{number} * {number}= {number *number}')

# # list=['Python','Numpy','Pandas','Django','Flask']

# # for i in list:
# #     print (i)
# # for number in range(101):# even numbers
# #     if number % 2 ==0 :
# #         print (number)

# # for number in range(101):
# #     if number % 2 !=0 : # odd numbers
# #         print (number)
#  #range for intergers

# import time
# lyrics=[
# 'Id rather be working ',
# 'Whenever we breathe',
# 'Every time you email me',
# 'Dont say that you noted',
# 'Just come get me',
# ]

# for sentence in lyrics:
#     print(sentence + '\n')
#     time.sleep(1.5)

even_sum= 0
odd_sum=0
for numbers in range (101):
   if numbers % 2 == 0:
    even_sum += numbers 
   else: 
     odd_sum += numbers

print(f'The sum of all even numbers is {even_sum}.And the sum of all odds is {odd_sum}')