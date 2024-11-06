#dictionary-unordered collection of data in a key value pair format

{
    'name': 'Joy',
    'age': 24,
    'skills':['js','React','Python']
}


#tuple- an ordered collection of different data types like list but tuples cannot be modified

('Mercury','VENUS','MARS','SATURN')

#find an euclidian distance between (2,3) and (10,8)
import math
def euclidian(a,b):
 a_sq=a*a
 b_sq=b*b

 sum= a_sq +b_sq
 c=math.sqrt(sum)

 return c

print(euclidian(3,4))