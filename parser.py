
## this is an attempt at some of the code that we talked about in class. It will more than likely have to be cleaned up to work, but it should be a good start for the project 


import re
from datetime import datetime

from urllib.request import urlretrieve

url='https://s3.amazonaws.com/tcmg476/http_access_log'
local='localcopy.log'

local, headers=urlretrieve(url, local)
file=open(local,'r')


# How many requests were made on a week-by-week basis? Per month?

# months = {
#  Jan: 0,
#  Feb: 0,
#  Mar: 0,
#  Apr: 0,
#  May: 0,
#  Jun: 0,
#  Jul: 0,
#  Aug: 0,
#  Sep: 0,
#  Oct: 0,
#  Nov: 0,
#  Dec: 0
#}


awk 'BEGIN {
    split("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec ", months, " ")
    for (a = 1; a <= 12; a++)
        m[months[a]] = a
}
{
    split($4,array,"[:/]");
    year = array[3]
    month = sprintf("%02d", m[array[2]])

    print > FILENAME"-"year"_"month".txt"
}' incendiary.ws-2009




















