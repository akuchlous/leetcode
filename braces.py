#!/usr/bin/env python

import pdb

def dfs (lQ, rQ, buf, allC):
    # print "choices: " , lQ, rQ
    # pdb.set_trace()
    if lQ:
       newBuf = buf + lQ[0]
       rrQ = rQ + [")"]
       dfs (lQ[1:], rrQ, newBuf, allC)
    if rQ:
       newBuf = buf + rQ[0]
       dfs (lQ, rQ[1:], newBuf, allC)
    if not lQ and not rQ: 
       allC.append(buf)


def sol(n):
   lQ = ["(" for i in range(n)]
   rQ = []
   allC = []
   dfs (lQ, rQ, "", allC)
   return allC

print sol(1)
print sol(2)
print sol(3)
print sol(4)
