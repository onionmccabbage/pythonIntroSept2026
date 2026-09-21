# every python file is a module
from basics import details
from basics import person   

# We may write loops like this
for i in range(10): # range(start=0:stop-before)
    print(i)

# we may loop over a collection
for i in details:
    print(type(i))
    print(i)

# we may iterate over a dict like this
for (key, value ) in person.items():
    print(key, value)