import random # there are many libraries that are built in to python
r = random.randint(1, 100) # returns a random integer between 1 and 100 inclusive   
n=1
# while is a loop with a condition attached
while n <= r:
    print(n) 
    # n = n + 1 # increment by 1
    # alternatively
    n+= 1 # increment by 1 (a reliable way to increment)
