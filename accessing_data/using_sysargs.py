# Python may access the system via the sys library (also the os library)

import sys
import os

if __name__ == "__main__":
    print( sys.platform ) # this will return the platform we are running on
    print( sys.version_info )
    print( os.cpu_count() )
    # every time we run a python module, it will have system argument variables
    # the sys.argv members are always in a list
    # sys.argv[0] is ALWAYS the name of the current module
    for arg in sys.argv:
        print(arg, type(arg))
    # We often act conditonally based upon optional sys.argv
    # NB every sys.argv is always a string value
    # we may need to check if we have additional sys.argv
    # and if so, act upon them
    if len(sys.argv) > 1:
        new_args = sys.argv[1:] # start from member 1 (ignore member 0)
        print( new_args )
    