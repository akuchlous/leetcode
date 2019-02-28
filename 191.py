import pdb
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
	b = 1 
	#pdb.set_trace()
	total =0 
        for i in range(32):
            if (n & b) != 0  : total +=1
	    b = b << 1 

        return total


print (3, Solution().hammingWeight(3))
for x in range(10):
 	print (x, Solution().hammingWeight(x))
