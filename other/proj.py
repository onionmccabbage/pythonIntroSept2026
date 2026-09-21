# make use of our utility
# NB relative import here is from the SAME package (folder)
# CAREFUL - when we import, Python executes the entire module
from util import validateNumeric
from util import askForNumber

# ask the user for a value
# make sure we cast as numeric
# use our utility to validate the value
user_input = askForNumber()
validated_input = validateNumeric(user_input)
print(f'validated_input: {validated_input}')

# we may have other sources of data
data = (3, 5, 2.2, 'oops')
for i in data:
    print(f'checking {i}...')
    validated = validateNumeric(i)
    print(f'validated: {validated}')    