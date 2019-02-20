#!/usr/bin/env

def foo (x,y, bound):
   maxX = maxY = 0
   while (x**maxX <= bound): maxX+=1
   while (y**maxY <= bound): maxY+=1
   print (maxX, maxY)
   #l = list(filter(lambda x: x<bound, [x^i+y^j for i in range (maxX) for j in range(maxY)]))
   l = [x^i+y^j for i in range (0, maxX) for j in range(0, maxY)]
   l.sort()
   print (list(set(l)))

foo(2,3, 10)
