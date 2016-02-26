import re
import socket
#import urlib

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com',80))

#TELNET CONNECTION
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
	data = mysock.recv(512)
	if(len(data) < 1):
		break
	print data
mysock.close()


print "using urlib"
##urlib
#fhand = urlib.urlopen("http://www.pythonlearn.com/code/intro-short.txt")

#for line in fhand:
#	words = line.strip()
#	for word in words:
#		counts[word] = counts.get(word,0) + 1
#print counts