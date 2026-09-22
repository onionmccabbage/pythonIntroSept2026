# we may need to be a bit more in control of the file output

def writeToFile(b):
    '''Persist the entire contents of b into a text file'''
    fout = open('my_log.txt', 'a') # the default is 't' for text
    fout.write(b)
    fout.close()

# there is an alternative syntax which is more performant
def writeWith(n):
    '''use the 'with' operator to persist in a text file'''
    with( open('log.txt', 'a') as fout ):
        fout.write(n)
        fout.write('\n')
    # the 'with' operator will close the asset as soon as no longer used

if __name__ == '__main__':
    l = ['report', 'analysis', 'outcome', 'debrief']
    # for _ in l:
    #     writeToFile(_)
    #     writeToFile(', ') # here we opt to write a comma separator
    # writeToFile('\n') # we may choose to add a new line character
    writeWith( str(l) )
