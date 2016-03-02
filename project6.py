import json
import urllib


address = raw_input('Enter json: ')
url = urllib.urlopen(address)
input = url.read()
info = json.loads(input)
print 'Retrieved ',len(info),' characters'
print (info)
sum = 0
count = 0 
for item in info['comments']:
	count +=1
	sum += item['count']
print 'Count: ',count
print 'Sum: ', sum