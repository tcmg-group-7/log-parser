
## this is an attempt at some of the code that we talked about in class. It will more than likely have to be cleaned up to work, but it should be a good start for the project 

from urllib.request import urlretrieve

url='https://s3.amazonaws.com/tcmg476/http_access_log'
local='localcopy.log'

local, headers=urlretrieve(url, local)
file=open(local,'r')


import re
from datetime import datetime

total_count = 0

# How many requests were made on a week-by-week basis? Per month?

months = {
1: 0,
2: 0,
3: 0,
4: 0,
5: 0,
6: 0,
7: 0,
8: 0,
9: 0,
10: 0,
11: 0,
12: 0
}

entire_log= [open('http_access_log.txt')]

# the rejex pattern
regex = re.compile("(.*?) - - \[(.*?):(.*).*\]\"[A_Z]{3,6}(.*?)HTTP.*\" (\d{3}) (.+)")

for line in entire_log:
    
    total_count +=1
    
    parts = regex.split(line)
    
    datestamp = datetime.strptime(parts[2], '%d/%b/%Y')
    
    months[datestamp.month} +=1
              
    print(datestamp.month) 
    
print(months)


















