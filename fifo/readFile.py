# We may retrieve text from a file using a file access object

def readWith():
    '''retrieve and return the entire contents of a text file'''
    with open('my_log.txt', 'rt') as fin: # 'rt' will read text
        r = fin.read()
        return r

def readAsList():
    '''retrieve the entire contents of a file as a list of text lines'''
    with open('my_log.txt', 'rt') as fin:
        r_l = fin.readlines() # retrieve each line as a string in a list
        return r_l

if __name__ == '__main__':
    print( readWith() )
    print( readAsList() )