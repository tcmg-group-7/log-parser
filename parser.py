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
totalrequests = 0

print('Loading...\n')

# days dictionary

days = {
    'Sun': 0,
    'Mon': 0,
    'Tue': 0,
    'Wed': 0,
    'Thu': 0,
    'Fri': 0,
    'Sat': 0,
}

# the individual days of the week for the week-by-week portion
days_by_week = {
    'Sun': 0,
    'Mon': 0,
    'Tue': 0,
    'Wed': 0,
    'Thu': 0,
    'Fri': 0,
    'Sat': 0
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

# empty list that the days_by_week dict will append to
week = []
date_conversion = -1


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
    last_date = date_conversion

# this variable converts the day digit portion from the original datestamp
    date_conversion = datestamp.strftime('%d')

# converting the date object to the month full name
    month_conversion = datestamp.strftime('%B')

# if the date_conversion variable is not equal to the last_date and the day is Sun append to the empty week list
    if date_conversion != last_date and day_conversion == "Sun":
        week.append(days_by_week)
        days_by_week = {
            'Sun': 0,
            'Mon': 0,
            'Tue': 0,
            'Wed': 0,
            'Thu': 0,
            'Fri': 0,
            'Sat': 0
        }

# when the conversions match the dictionary values, add to the counters
    days[day_conversion] += 1
    days_by_week[day_conversion] += 1
    months[month_conversion] += 1

# These were test statements to make sure the sums matched
# day_values = days.values()
# month_values = months.values()
# print(sum(day_values))
# print(sum(month_values))

# print out the totals per day from the days dictionary
for key, value in days.items():
    print(f'{key}: {value}\n')
print()

# printing the week-by-week totals from the week variable
i = 0

for weeks in week:
    print(f'Week {i+1} total is: {week[i]}\n')
    i += 1
print()

# print out the totals per month from the months dictionary
for key, value in months.items():
    print(f'{key}: {value}\n')
print()

# looks through the log file 
for line in filelines:
    if "[" in line:
        totalrequests += 1
        if re.search("\".*\" 4..", line) is not None:
            error += 1
        
        # 3xx codes = redirected requests
        if re.search("\".*\" 3..", line) is not None:
           redirect += 1
errorpercent= round((error * 100) / totalrequests, 2)  
redirectpercent= round((redirect * 100) / totalrequests, 2)

print("Total number of requests:", totalrequests)
print("Percentage of Unsuccessful Requests: ",str(errorpercent), "%")
print("Percentage of Requests Redirected: ",str(redirectpercent), "%\n")

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
print()
