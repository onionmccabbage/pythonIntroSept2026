# some utility functions

def validateNumeric(n):
    '''This function will validate that the value n is either in or float
    If it is neither we will return a safe default value'''
    if type(n) in (int, float):
        return n # the return statement will always end the function execution
    else:
        return 0

def askForNumber():
    '''This function will ask the user for a number and return it'''
    _value = '' # we start with an empty string
    while True:
        c = input("Please enter a number: ")
        # we can use exceptino handling to manage the input
        try:
            _value = float(c) # we cast to float first to handle decimal input
            return _value # our function stops when we return something
        except Exception as err:
            print(f"Invalid input: {err}")


# it's often a good idea to exercise your code to check it wokrs as expected
# does it work for int
# this will only run the following code if this module is being run directly (not imported)
if __name__ == "__main__": 
    i = 4
    check_i = validateNumeric(i)
    print(f'check_i: {check_i}') # check_i: 4
    # does it work for float
    f = 3.14
    check_f = validateNumeric(f)
    print(f'check_f: {check_f}') # check_f: 3.14
    # does it work for a string
    s = "hello"
    check_s = validateNumeric(s)
    print(f'check_s: {check_s}') # check_s: 0
    # make sure our inout validatorr works as expected
    s = askForNumber()