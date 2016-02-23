import re

hand = open('regex_sum_242649.txt')
numlist = list()
for line in hand:
	line = line.rstrip()
	stuff = re.findall("[0-9]+",line)
        for num in stuff:
                numlist.append(int(num))
print 'Sum:', sum(numlist)

