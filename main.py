# this may be our main running module
from other.util import validateNumeric

# here we have a funcrtion to check a whoel bunch of data values
def checkAllValues(s):
    '''Here we iterate over an incoming collection, 
    validating that we have just numeric values'''
    result_list = [] # we start with an empty list
    # iterate over the structure
    for _ in s: # often python uses _ as an iterator
        validated = validateNumeric(_) # we call our utility function
        # append our validated value to our new list
        result_list.append(validated)
    # we now return the new structure containing valid values
    return result_list


if __name__ == "__main__":
    v1 = (4,3,2,1) # all ok
    v2 = ['4', '3' ,'2', '1'] # all get converted to 0
    print( checkAllValues(v1) )
    print( checkAllValues(v2) )