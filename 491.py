#!/usr/bin/env 


import pdb
def recurse(s):
	if (len(s) == 1): return s
	retList = []
	for c in s[1:]:
		if (c >= s[0]):
			retList.extend([s[0]]+ recurse(s[1:]))
	print (retList)


recurse([1,2,3])
