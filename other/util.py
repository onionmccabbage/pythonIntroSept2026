# some utility functions

def validadteNumeric(n):
    '''This function will validate that the value n is either in or float
    If it is neither we will return a safe default value'''
    if type(n) in (int, float):
        return n # the return statement will always end the function execution
    else:
        return 0

# it's often a good idea to exercise your code to check it wokrs as expected
# does it work for int
i = 4
check_i = validadteNumeric(i)
print(f'check_i: {check_i}') # check_i: 4

# does it work for float
f = 3.14
check_f = validadteNumeric(f)
print(f'check_f: {check_f}') # check_f: 3.14

# does it work for a string
s = "hello"
check_s = validadteNumeric(s)
print(f'check_s: {check_s}') # check_s: 0