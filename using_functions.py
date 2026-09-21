# we can write re-useable code in functions

def checkType(v):
    '''We may choose to write a docstring explaining our function
    In this case, we will check the type of a variable'''
    if type(v) == int:
        # f'' lets us format the string
        return f"{v} is an integer"
    elif type(v) == float:
        return f"{v} is a float"   
    elif type(v) == str:
        return f"{v} is a string"  

# we may exercise the code
d = 4
result = checkType(d)
print(result)