from datetime import datetime

# Python has built in generators
# g = (float(i/3) for i  in range(0,10))
# for _ in g:
#     print(_)

# we may create our own custom generator
def makeDT():
    '''This custom generator will yiled a date-time value every time we ask for one'''
    while True: # careful - this is an endless loop (only cease when Python stops running)
        now = datetime.now() # retrieve the computer clock time stamp
        dt_str = now.strftime('%d-%m-%y %H:%M:%S') # this is a date-time picture
        # the keyword 'yield' makes this function into a generator
        yield dt_str

if __name__ == '__main__':
    # we need an instance of our generator
    dt = makeDT()
    print(dt, type(dt)) # we have a generator
    # we can use it like this:
    t1 = dt.__next__() # this will grab the next available member from our generator
    print(t1)

