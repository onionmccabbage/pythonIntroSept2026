# we can write re-useable code in functions

def checkType(v):
    '''We may choose to write a docstring explaining our function
    In this case, we will check the type of a variable'''
    if type(v) == int:
        return (v, 'int')
    elif type(v) == float:
        return (v, 'float')   
    elif type(v) == str:
        return (v, 'string')  

# we may exercise the code
data = [4,5.1, 9, -3, 44.444, 'lunch']
for d in data:
    result = checkType(d)
    # f'' lets us format the string
    print(f"{result[0]} is a {result[1]}")