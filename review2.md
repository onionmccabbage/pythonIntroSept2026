## Python Review 2 

Ask the user for a category (and also for an id)
Use these to make a call to an API and show the results

This is a chance to explore Python 
- Alter these instructions to suit your thinking
- Think about architecture (maybe use separate functions, modules and imports, although it can be one single file if you like)
- Look online, talk to each other, ask me etc.
There will be an opportunity to share your code at the end

#### Details:

- Write a new module which asks the user for a 'category' 
(remember to use input() which always returns a string)
Validate the user input as follows:
- The category may only be one of 'users', 'posts', 'todos' or 'photos'
- Maybe use the 'in' operator to see if the value is in a tuple of permitted values
- Also ask the user to enter an id
- The id must be a positive integer in the range 1-8 (or suitable range per category)
- After you ask the user for category value, build a string something like this: 
  url = f'https://jsonplaceholder.typicode.com/{cat}/{id}'
- Inject the 'category' and 'id' into the curly brackets as shown
- Use the 'requests' library to make a 'get' call to this API
- Show the user what was returned by printing a nicely formatted string
- Remember to handle potential exceptions with try...except

#### Optional

We need to ensure the two parameters are in the required form:
Write a module containing a function called 'cleanup' which receives arguments

The cleanup function should ensure:
- there is a value for the 'category' and it is a non-empty string 
  containing one of the permitted categories
- there is a value for the 'id' and it is a positive integer within range

If category or id is missing or unacceptable, you should provide sensible defaults

For example, if id is a floating point number or a string, try to cast it as an int()

Import and use your 'cleanup' function to sanitize the user-provided data

#### If Time

Check to see if there are additional system arguments, and if so, use them for the category and id