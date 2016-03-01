import urllib
from BeautifulSoup import *
 
url = raw_input('Enter URL: ')
count = int(raw_input('Enter count: '))
ctr = 0
position = raw_input('Enter position: ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
 
# Retrieve all of the anchor tags
tags = soup('a')
#print 'Retrieve', tags[1].get('href',None)	
while (ctr < count):
	ctr += 1
	tag = tags[int(position)-1]
	url = tag.get('href',None)
	print 'Retrieve',url
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	