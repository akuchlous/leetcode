class Solution(object):
    def consecutiveNumbersSum(self, N): 
        """ 
        :type N: int
        :rtype: int
        """
        if (N == 1) : return 1
        cSum = {}
        for i in range(N+1):
            cSum[(i*(i+1))/2] = 1 
        total = 0
        for x in cSum:
	    if (x-N) in cSum and x-N < x: total+=1
	print (total)
	return (total)


Solution().consecutiveNumbersSum(5)
Solution().consecutiveNumbersSum(9)
Solution().consecutiveNumbersSum(15)
Solution().consecutiveNumbersSum(3654859)
