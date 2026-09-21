# write code in a function to 
# check if a number is odd or even
# exercise the code using a collection 
# of odd and even number

def checkOddEven(n):
    '''returns True if n is odd, False otherwise'''
    if n % 2 == 1:
        return True
    else:
        return False    
    
# exercise the code
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in numbers:
    result = checkOddEven(n)
    print(f"{n} is odd: {result}")  