# # #import mymodule

# # from mymodule import generate_full_name


# # #the os module in python provides functions for
# # #creatong directory
# # #changing working directory
# # #removing a directory
# # #fetch its contents
# # #changing and identifying the current directory

# # # import the module
# # import os
# # # Creating a directory
# # os.mkdir('directory_name')
# # # Changing the current directory
# # os.chdir('path')
# # # Getting current working directory
# # os.getcwd()
# # # Removing directory
# # os.rmdir()

# #statistics module

# from statistics import *    #importing all the statistics modules
# ages = [20,20,4,24,8,25,22,26,20,26,22]

# print(mean(ages))
# print(median(ages))
# print(mode(ages))
# print(stdev(ages))

# #math module

import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base


#random module

# from random import random, randint
# print(random())#does not take any arguments,it returna a  between 0 and 0.9999
# print (randint(5,20))# returns a random interger numbber between 5, 20


# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

from random import randint
def numbers():
    unique_numbers= set ()

    while len(unique_numbers) < 7 :
      number= randint(0,9)
      unique_numbers.add(number)
    return list(unique_numbers)


print(numbers())

