empty_tuple= ()
#or
empty_tuple=tuple()


fruits=('grapes','starfruit','tamarind','lemon')

len(fruits)
#if we want to modify a tuple we can change it into a list 

lst=list(fruits)


#we can join tuples using the '+' operator

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables

#unpacking a tuple
my_tuple=(1,2,3,4,5)

a,b,c,d,e=my_tuple

print(a)