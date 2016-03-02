
import urllib
import xml.etree.ElementTree as ET

output = 0
address = raw_input('Enter location: ')
xml = urllib.urlopen(address)
print 'Retrieved: ',xml
data = xml.read()
print data
tree = ET.fromstring(data)
counts = tree.findall('.//count')
#values = int(counts[0].text)
for val in counts:
	output += int(val.text)
print output	
