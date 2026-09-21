# we may import from the Python Standard Library
import datetime # this imports the entire datetime library
# alternative
from datetime import datetime # this imports only the datetime class from the datetime library

# now = datetime.datetime.now() # here we use datetime.datetime
now = datetime.now() # here we use datetime

print(now)