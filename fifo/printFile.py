# We may choose to use the print function to write to a text file

l = [1,2,3,4,5,6,7]

# for _ in l:
#     print(_, end=', ') # we may choose the ending character

def printToFile(b):
    '''Send the text contained in b to a text file'''
    # we need a file access object
    # the file is created if it does not exist
    fout = open('my_file.txt', 'at') # the 't' means text (default)
    # 'at' means append text 
    # 'wt' (over)write
    # 'xt' means exclusive access (fails if file already exists)
    print( b, file=fout ) # NB this adds a default new line character
    fout.close() 
    # it is a really good idea to 
    # clean up resources when no longer needed

if __name__ == '__main__':
    words = 'here is some info to be stored in a file'
    printToFile( words ) 