# We may override any built in feature of Python
# for example + means add things together
# also == means compare if things are the same

class Asset():
    '''An asset includes a name and a serial number'''
    def __init__(self, n, s):
        self.name   = n
        self.serial = s
    # we may declare our own definition of equality
    def __eq__(self, comparator): # override the built in equality operator
        '''if the name and serial match, consider the assets to be equal
        Here we will ignore case'''
        isEqual = True
        if self.serial != comparator.serial:
            isEqual = False
        if self.name.lower() != comparator.name.lower():
            isEqual = False
        return isEqual

if __name__ == '__main__':
    mast    = Asset('5g mast', 234626)
    cabinet = Asset('thermal cabinet', 56324)
    other   = Asset('5G mast', 234626)
    # are these assets the same?
    print( mast == other ) # True
    print( mast == cabinet ) # False