#!/usr/bin/env python

def match(inS):
   match = {"(":")","[":"]", "{":"}"}
   l = []
   for s in inS:
      if ((not l) or (l[-1] not in match )or  (match[l[-1] ] != s)): 
         l.append(s)
      else: 
         del l[-1]
   return (not l)



print (match("([])[]({})"))
print (match("(])[]({})"))
