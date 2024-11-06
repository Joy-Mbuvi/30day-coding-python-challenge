age= 24
height=5.0
store= 3 +7j

base= int(input('enter base of the triangle:'))

height=int(input('enter thr height of the triange:'))

def area(base,height):
    total=0.5 *base *height

    return total


print(f"your total:{area(base,height)}")

a=int(input("enter side a:"))
b=int(input("enter side b:"))
c=int(input("enter side c:"))

def perimenter(a,b,c):
    
    tt=a+b+c
    return tt

print(f"your total:{perimenter(a,b,c)}")


# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years=int(input('enter how many years you have lived:'))

def seconds(years):
    ss=31556952
    total_seconds= years * ss

    return total_seconds

print(f"you have lived for {seconds(years)}seconds")


# # Write a Python script that displays the following table
# # 1 1 1 1 1
# # 2 1 2 4 8
# # 3 1 3 9 27
# # 4 1 4 16 64
# # 5 1 5 25 125

rows = [
    [1, 1, 1, 1, 1],
    [2, 1, 2, 4, 8],
    [3, 1, 3, 9, 27],
    [4, 1, 4, 16, 64],
    [5, 1, 5, 25, 125]
]

for row in rows:
    print (row)


# # Use and operator to check if 'on' is found in both 'python' and 'dragon'

def check_word():
 if 'on' in 'python' and 'dragon':
    return True
 else:
   return False
 
print(check_word())

# # I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
def check_word():
    sentence="I hope this course is not full of jargon"
    if "jargon" in sentence:
        return True
    else:
        return False

print(check_word())

# # There is no 'on' in both dragon and python

def checkword():
    if 'on' not in 'dragon' and 'on' not in'python':
        return True
    else:
        return False
    
print (checkword())