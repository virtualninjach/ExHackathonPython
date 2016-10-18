import urllib
url= "http://lwaldtech.com/oopsapi/API/oopsAPI/GetAllOops"
response = urllib.urlopen(url).read()
print (response)

