# we may access data from the internet using the requests library
import requests
import sys

# Problem: if there is an additional sys.argv, 
# use it as the parameter in our request

def getData(param=''):
    '''Make a call to a remote API to retrieve JSON data'''
    api_url = "https://jsonplaceholder.typicode.com/photos"
    # use the requests library to access this url
    # maybe we only need one part of the data. We pass parameters to the URL
    # param = 19
    # whenever we access remote data we should wrap in try-except
    try:
        response = requests.get(f'{api_url}/{param}') # this will return a response object
        # we then grab the JSON data from the respinse object
        # (we would know beforehand if we are working with JSON, xml etc)
        photos = response.json() # this will return a list of dictionaries
        return photos
    except Exception as err:
        return f'An error occurred {err}'

def checkSysArgs():
    '''Look for additional system arguments'''
    p=''
    if len(sys.argv) > 1:
        p = sys.argv[1]
    return p


if __name__ == "__main__":
    # we may iterate over a series of values to retireve each in turn
    l = [12, 19, 2, 33]
    for _ in l:
        result = getData(_)
        print(result) # we could combine these lines print( getData() )
    # use any sys.argv values
    print( getData( checkSysArgs() ) ) # could be separate lines

    # we may see just part of the data
    # print( result[0] ) # we only want member 0 of the list
    # print( result[0]['title'] ) # we can access members of the dict 


