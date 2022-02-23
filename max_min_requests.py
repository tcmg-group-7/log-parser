import re

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local = 'http_access_log.txt'
openfile = open(local, 'r')
file = openfile.read()
filelines = file.split('\n')
error = 0
redirect = 0
totalrequests = 0

def find_most_least_requested_file():
    log_line= 'local - - [24/Oct/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 200 150'
    pattern= r'\[([^:]*):(.*) .*\] \"([A-Z]*) (.*) HTTP.*\" ([2345]\d\d)'
    collection_dict={}
    # searches for matching pattern 
    for line in filelines:
        match= re.search(pattern,line)
        try:
            filename = match.groups()[3]
        except AttributeError:
            filename = match
        if filename in collection_dict:
            collection_dict[filename] += 1
        else:
            collection_dict[filename] = 1
    
    # if the pattern is found, it is added to the dictionary 
    values = list(collection_dict.values())
    keys = list(collection_dict.keys())

    # calculates the max and the minimum number of files 
    m = max (values)
    n = min (values)
   
    # finding the values 
    i = values.index(m)
    z = values.index(n)

    # gets the count of the keys which is the total number of times a file is requested
    most_requested_file= keys[i]
    least_requested_file= keys[z]

    return "Most Requested",most_requested_file, "Least Requested",least_requested_file


if __name__ == "__main__":
    file_request= find_most_least_requested_file()
    print(file_request)