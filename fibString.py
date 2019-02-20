#!/usr/bin/env python

'''
Problem statement : The Fibonacci strings are a series of recursively­defined strings. F(0) is the string a, F(1) is
the string bc, and F(n+2) is the concatenation of F(n) and F(n+1). For example, F(2) is abc, F(3) is
bcabc, F(4) is abcbcabc, etc. 
Given a number n and an index k, return the kth character of
the string F(n)

'''

import pdb
N = 18
fibA = [1,1]
newV = 1
while fibA[-1] < N:
	fibA.append(fibA[-2] + fibA[-1])
fibS = ["a", "bc"]

pos = N
startPoint = len(fibA)


while (pos > 2):
    print (pos, startPoint)
    pdb.set_trace()
    lA, RA = fibA[startPoint - 3],  fibA[startPoint - 2]
    if (pos > lA):
       pos = pos-lA
       startPount = 
    else:
