#!/usr/bin/env python

def f(nA):
	currA = prevA = 0
	for i in range (0, len(nA)):
		t = prevA
		prevA = max(currA, prevA)
		currA = max(nA[i], t+nA[i])
	print (max(currA, prevA))

f([2, 4, 6, 2, 5])
f([-5,-1,-1,5])
f([-5,-1,-1,-5])
f([5,1,1,5])
f([5,1,7,1,1,2,6])
