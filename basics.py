
# Python comments work like this
a = 3   # this is an integer
b = 7.4 # this is a float

# we also have boolean values
x = True
y = False # NB capital T and capital F

# a string is a collection of characters
hello = 'Welcome to Python and related technologies'
# we may acces any  member of a collection by its numeric position
# [start:stop-before]
print( hello[11:17] ) # this is called slicing

# we may use slicing with any python collection
# a list is an ordinal mutable collection of any data type
my_data = [4, 7, a, x, hello]
# we may alter members of a list
my_data[1] = 42
my_data.append( 'new' )
my_data.insert( 2, 'changed' )
print( my_data[1:5] )

# Another collection is the tuple
# a tuple is an ordinal immutable collection of any data type
details = (x, y, 'data', b)
# NB once we make a tuple its values cannot be changed
print(details[0:3]) # slicing
# We can always find out a data type
print( type(a), type(b), type(details), type(my_data) )

# the dictionary type
# a dictionary is not ordinal. 
# It is a collection of key:value pairs
person = { 'name':'John', 'age': 34, 'height': 1.75 }
person['age'] = 35
person['admin'] = True
print(person, type(person), person['age'])