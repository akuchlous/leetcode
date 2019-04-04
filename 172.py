import pdb
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        retVal = 0 
        for i in range(1,n):
            if (i%5 == 0) : 
	        retVal +=1 
        return retVal

#print (Solution().trailingZeroes(3))
print (Solution().trailingZeroes(1808548329))
