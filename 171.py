import string
import pdb
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapS = dict(zip(list(string.ascii_uppercase), range(1,27)))
        retVal = 0
        i = 0 
	pdb.set_trace()
        for c in s[::-1]:
            retVal += mapS[c]* pow(26, i)
	    i+=1
        return retVal
        

print (Solution().titleToNumber("A"))
print (Solution().titleToNumber("AA"))
