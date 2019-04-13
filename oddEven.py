#!/usr/bin/env python


def sortOddEven(N):
    return [x for x in N if (x%2 == 0)] + [x for x in N if (x%2 == 1)]
    
   #  evenL = []
   #  oddL = []
   #  for n in N : 
   #      if (n%2 == 0): 
   #          evenL.append(n)
   #      else: 
   #          oddL.append(n)
   #  return evenL + oddL

if __name__ == "__main__":
	print (sortOddEven([2,1]))
	print (sortOddEven([1]))
	print (sortOddEven([]))
	print (sortOddEven([1,3,5]))
	print (sortOddEven([1,3,5]))
	print (sortOddEven([1,2,-5]))
