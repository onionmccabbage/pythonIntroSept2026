# A class may take default values
# We may use name mangling and property decorators

class Person: # by convention we use InitialCap names
    '''Person will have name (string) age (int) and admin (boolean)'''
    __slots__ = ['__name', '__age', 'admin'] # here we explicitly restrict the permitted mangled property names
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
    # write get/set methods for the age
    @property
    def age(self): # every class function MUST start with 'self'
        return self.__age # the getter function just returns the value
    @age.setter
    def age(self, new_age):
        if type(new_age) in (int, float) and new_age >=0:
            self.__age = new_age
        else:
            # we could set a default or raise an exception
            raise TypeError('Age must be a positive integer')
    # classes may have their own class methods (things the class can do)
    def birthday(self):
        '''when this method is called, the age property will be incremented by one'''
        self.__age += 1 # here we refer directly to the the mangled name (inside this class)
        # or 
        # self.age = self.age+1 # here we use the getter and setter methods
    # if we choose we may write our own print function
    # this will override the default print for objects
    def __str__(self):
        return f'{self.name} is {self.age} years old. Administrator: {self.admin}'
    def __repr__(self): # this is used in immediate python to represent the class instance
        return f'{self.age} year old {self.name}'

if __name__ == '__main__':
    o = Person('Orla', 32) # defaults to admin=False
    o.name = 'Betty' # this will change the name
    # o.name = False # this will raise an exception
    p = Person('Peony', 42, True) # here we override the default admin
    print( o.name, o.age, o.admin )
    # we CANNOT directly acces the name-mangled property
    # print( o.__name ) # fail
    # we may mutate instance properties via the setter methods
    p.name = 'Penny' # p['name'] will not work!!!
    p.age  = 43
    p.birthday() # calls the class method
    print(o) # print will use the default for objects
    print(p.name, p.age) # calls the getter methods

    # docstring access
    print( o.__doc__ )
    print('_______________________________________________________')
    help(Person)