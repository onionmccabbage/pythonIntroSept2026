# We may retrieve text from a file using a file access object

def readWith():
    '''retrieve and return the entire contents of a text file'''
    try:
        with open('my_log.txt', 'rt') as fin: # 'rt' will read text
            r = fin.read()
            return r
    except FileNotFoundError as fnf:
        print(f'Cannot locate file: {fnf}')
    except Exception as err: # we always handle generic exceptions after specific exceptions
        print(err)
    finally:
        print('This optional block will always run')

def readAsList():
    '''retrieve the entire contents of a file as a list of text lines'''
    try:
        with open('my_log.txt', 'rt') as fin:
            r_l = fin.readlines() # retrieve each line as a string in a list
            return r_l
    except FileNotFoundError as fnf:
        print(f'Cannot locate file: {fnf}')
    except Exception as err:
        print(err)

if __name__ == '__main__':
    print( readWith() )
    print( readAsList() )