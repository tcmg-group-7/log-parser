from datetime import datetime
import re

# opening the file and using the local log
url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local = 'http_access_log.txt'
openfile = open(local, 'r')
file = openfile.read()
filelines = file.split('\n')

print('Loading...')

# months dictionary

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

for line in filelines:

# regex pattern to use
    regex = re.compile('(.*)\[(.*?):(.*)')

# parts

    parts = regex.split(line)
    # print(parts)
    if len(parts) != 5:
        continue

# convert date string to a date object
    datestamp = datetime.strptime(parts[2], '%d/%b/%Y')
    # print(datestamp)
    months[datestamp.month] += 1

values = months.values()
print(sum(values))
print(months)
