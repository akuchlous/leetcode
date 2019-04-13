#!/usr/bin/env python

def doors(N):
   doors = [0]* (N+1)
   for p in range(1,N+1):
      for d in range (1,N+1):
         if (d%p == 0): 
            doors[d] ^=1 
      #print (doors)
   print sum(doors)


if __name__ == "__main__":
    doors(100)
