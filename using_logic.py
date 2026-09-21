# We may use 'if' statements for logical operations
m=5
n=3

# < > != == <= >= 
if m < n:
    print("less than")
elif m > n:
    print("greater than")
elif m == n: # double-equals checks equality
    print("equal")  
else:
    print("unknown")

# ask the user for a value
temperature = int(input("Enter the temperature: "))

# we may need to control a/c
if temperature > 30:
    print("turn on AC")
elif temperature < 20:
    print("turn on heater")
else:
    print("maintain normal temperature")    