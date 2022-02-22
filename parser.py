from urllib.request import urlretrieve

url='https://s3.amazonaws.com/tcmg476/http_access_log'
local='localcopy.log'

local, headers=urlretrieve(url, local)
file=open(local,'r')
