import pdb
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seq = set()
        while (True):
            def sum2(num):
                #pdb.set_trace()
                s = 0
                while (num != 0):
                    s += pow((num% 10),2)
                    num = num/10
                return s
        
            retVal = sum2(n)
            if (retVal == 1): return True
            if (retVal in seq): return False 
            n = retVal
            seq.add(retVal)


print (Solution().isHappy(19))
