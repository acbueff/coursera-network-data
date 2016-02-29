import urllib
from BeautifulSoup import *
 
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
 
soup = BeautifulSoup(html)
 
# Retrieve all of the anchor tags
tags = soup('span')
count = 0
sum = 0
for tag in tags:
	count = count + 1
	sum = sum + int(tag.contents[0])
    
	
print "Count ", count
print "Sum ", sum