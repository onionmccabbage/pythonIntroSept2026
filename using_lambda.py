# Many languages including Python have anonymous functions
# these are called 'lambdas'

check = lambda x:'Positive' if x>=0 else 'Negative'
print( check(5) )
print( check(-5) )
print( check(False) ) # Zero is False, any other value is True
print( check(0) )

def mult(n):
    return lambda a : a * n

dbl = mult(2)
trp = mult(3)

print(dbl(3)) # 6
print(trp(3)) # 9

even_nums = filter(lambda x: x%2==0, range(0,11))
print( list(even_nums) )