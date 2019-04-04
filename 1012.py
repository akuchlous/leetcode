class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        bits = []
        while (N > 0):
            if (N & 1) :
                bits.append(0)
            else :
                bits.append(1)
            N = N>>1
	    # print (N,  bits)
        retVal = 0
        # print (bits)
        while (bits):
            b = bits.pop()
            retVal = retVal << 1
            retVal = retVal | b
	print (retVal)
	


Solution().bitwiseComplement(10) # 1010 , 101 
Solution().bitwiseComplement(5) # 101 , 10
