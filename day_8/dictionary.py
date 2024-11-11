# a dictionary is a collection od unordere,modidiable(mutable)paired(key:value)data type

# we can change dictionaries into list of tuples

#items()
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])



# pop(key): removes the item with the specified key name:
# popitem(): removes the last item
# del: removes an item with specified key name


#Adding items to a dictionary
dct={"ket1":"value1","ket2":"value2"}
dct['ket3']='value3'

#getting dct keys as a list
key=dct.keys()
print(key)

#getting value 
value=dct.values()
print(value)