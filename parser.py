from datetime import datetime
import re

# this is the requests that were made each month
# opening the file and using the local log
url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local = 'http_access_log.txt'
openfile = open(local, 'r')
file = openfile.read()
filelines = file.split('\n')
error = 0
redirect = 0

print('Loading...')

# days dictionary

days = {
    'Sun': 0,
    'Mon': 0,
    'Tue': 0,
    'Wed': 0,
    'Thu': 0,
    'Fri': 0,
    'Sat': 0,
    'Sun': 0
}

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

# for loop to find the number of requests for each month
for line in filelines:

# regex pattern to use
    regex = re.compile('(.*)\[(.*?):(.*)')

# parts

    parts = regex.split(line)
    # print(len(day_parts))
    # print(parts)
    if len(parts) != 5:
        continue

# convert date string to a date object
    datestamp = datetime.strptime(parts[2], '%d/%b/%Y')
# converting the date object to the date abbreviation
    day_conversion = datestamp.strftime('%a')
# converting the date object to the month full name
    month_conversion = datestamp.strftime('%B')
# when the conversions match the dictionary values, add to the counters
    days[day_conversion] += 1
    months[month_conversion] += 1

day_values = days.values()
month_values = months.values()
print(sum(day_values))
print(sum(month_values))

# print out the dictionary totals
print(days)
print(months)

#looks through the log file 
for line in filelines:
    if "[" in line:
        totalrequests += 1
        if re.search("\".*\" 4..", line) is not None:
            error += 1
        
        # 3xx codes = redirected requests
        if re.search("\".*\" 3..", line) is not None:
           redirect += 1
           
print("Total number of requests:", totalrequests, "\n")
print("Percentage of Unsuccessful Requests: ", round((error * 100) / totalrequests, 2), "%")
print("Percentage of Requests Redirected: ", round((redirect * 100) / totalrequests, 2), "%")
