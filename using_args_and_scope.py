# Scope is an important part of Python
# here is the global scope
g = 'hello'

def fn():
    # this is the local scope
    l = 'world'
    g = 'also local' # this variable is different to the global g
    print(g) # we can see the global variable
    print(l) # we can see the local variable`

def fn2():
    global g # we can access the global variable from within the function
    g = 'altered'

# we may call our functions
fn2() # this changes the global value of g
fn()
# we may acces the global scope from anywhere
print(g)
# but we can only access the local scope from within the function