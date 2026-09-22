# we may access data from the internet using the requests library
import requests

def getData():
    '''Make a call to a remote API to retrieve JSON data'''
    api_url = "https://jsonplaceholder.typicode.com/photos"
    # use the requests library to access this url
    response = requests.get(api_url) # this will return a response object
    # we then grab the JSON data from the respinse object
    photos = response.json() # this will return a list of dictionaries
    return photos

if __name__ == "__main__":
    result = getData()
    print(result)


