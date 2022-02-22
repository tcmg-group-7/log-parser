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
    'January': 0,
    'February': 0,
    'March': 0,
    'April': 0,
    'May': 0,
    'June': 0,
    'July': 0,
    'August': 0,
    'September': 0,
    'October': 0,
    'November': 0,
    'December': 0
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
    datestamp_conversion = datestamp.strftime('%B')
    # print(datestamp)
    months[datestamp_conversion] += 1

print(months)
