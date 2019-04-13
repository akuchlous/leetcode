#!/usr/bin/env python

from collections import defaultdict

def countU(L):
    c = defaultdict(int)
    for d in L:
        c[d] += 1
        lenS = len(d)
        i = lenS-1
        while (i > 0):
            if (d[i] == "."):
                c[d[i+1:]]+=1 
            i-=1 
    print (c) 

if __name__ == "__main__":
    l = [ "a.b.com",
          "b.com",
          "c.com",
          "d.c.com"]
    countU(l)


