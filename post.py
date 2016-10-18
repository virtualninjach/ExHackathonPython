import urllib
import urllib2
query_args = {'EventType':"motion detected in the dining room",
              'Action':"turn on the lights",
              'TimeStamp':"10/1/2016"}

url = 'http://lwaldtech.com/API/oopsAPI/InsertOops'
              
data = urllib.urlencode(query_args)
request = urllib2.Request(url, data)
response = urllib2.urlopen(request).read
print 'posted'
