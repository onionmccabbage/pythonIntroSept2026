# Python classes let us combine properties and methods into a single entity
# the following is demo code
f_name = 'fuschia'
f_colour = 'red'
num_f   = 120
height_f = 300
hardy = True
# we often collect related data into a collection
f = [f_name, f_colour, num_f, height_f, hardy] # or a tuple or a dict...
# None of the built in structures let us enforce data sanity
# no way to ensure facets like min/max
# no data type clarity 

# here we write code together
class Flower:
    '''This class takes colour and height arguments'''
    # the __init__ method is called once, when we make an instance
    def __init__(self, colour, height): # we may choose to pass properties to the instance 
        # We are only able to write a SINGLE __init__ function
        # we may wish to validate the incoming properties
        if type(colour)== str and colour != '':
            self.colour = colour # self must be the first argument in the function
        else:
            raise TypeError('Colour must be a non empty string')
        if type(height) in (int, float) and height >= 0:
            self.height = height # self will refer to the instance
        else:
            self.height = 12 # we may choose to set a sensible default value

if __name__ == '__main__':
    # here we create instances of our class
    fuschia     = Flower('red', 120) 
    honeysuckle = Flower('yellow', 300)
    example     = Flower(False, 'tall')
    print(fuschia.colour) # we may use dot notation to access properties
    print(honeysuckle.height)
    print(example.height)
    