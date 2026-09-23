# A class may take default values
# We may use name mangling and property decorators

class Person: # by convention we use InitialCap names
    '''Person will have name (string) age (int) and admin (boolean)'''
    def __init__(self, n, a, admin=False): # default admin is False
        self.name = n # here we call the setter function for name
        self.age  = a
        self.admin = admin
    @property # this is a property decorator
    def name(self):
        return self.__name # this is name-mangled
    @name.setter
    def name(self, new_name):
        # here we validate the name
        if type(new_name) == str and len(new_name)>0:
            self.__name = new_name # here we set the name-mangled property
        else:
            raise TypeError('Name must be a non empty string')

if __name__ == '__main__':
    o = Person('Orla', 32) # defaults to admin=False
    o.name = 'Betty' # this will change the name
    # o.name = False # this will raise an exception
    p = Person('Peony', 42, True) # here we override the default admin
    print( o.name, o.age, o.admin )
    # we CANNOT directly acces the name-mangled property
    print( o.__name ) # fail