import pdb
import string 

import string
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        allS = string.ascii_uppercase
        # base 26
        buf = ""
        remainders = []
	#pdb.set_trace()
        while (n >0):
	    print ( " ", n)
            remainders.insert(0, (n-1)%26)
            n = (n-1)/26
	print (remainders)
        for r in remainders :
            buf+=allS[r]
        return buf

# for x in range(28):
#           print (x,Solution().convertToTitle(x))
print (Solution().convertToTitle(26))
print (Solution().convertToTitle(27))
print (Solution().convertToTitle(500))
