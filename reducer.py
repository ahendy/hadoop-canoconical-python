#!/usr/bin/env python

from operator import itemgetter
import sys

current_word 	= None
current_count 	= 0
word 			= None
delim			= '\t'
readwords 		= []

for line in sys.stdin:
	line = line.strip()

 	word, count = line.split(delim, 1)
 	#print word, count	

	try:
		count = int(count)
	except ValueError:
		continue

	if current_word == word:
		current_count += count
	else:
		if current_word:
			print '%s\t%s' % (current_word, current_count)
			readwords.append( (current_word, current_count) )
		current_count = count
		current_word  = word

readwords.sort(key = lambda x: x[1])
#print readwords.reverse()
if current_word == word:
	print '%s\t%s' % (current_word, current_count)
