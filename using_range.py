# the range object lets us work with series of numeric values

r = range(-100, 101, 20) # start, stop-before, step

def isNegative(n):
    '''returns True if n is negative, False otherwise'''
    if n < 0:
        return True
    else:
        return False


for i in r:
    check = isNegative(i)
    print(f"{i} is negative: {check}")

