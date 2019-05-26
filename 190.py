#/usr/bin/env python

import pdb

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
	pdb.set_trace()
        val = 0
        for i in range(30):
            bit = n&1
            val<<=1 
            val|=bit
            n>>=1 # shift right 
            
        return n


Solution().reverseBits(2)
