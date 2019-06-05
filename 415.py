import pdb
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i,j = len(num1)-1, len(num2)-1
        s,c = [] ,0
        while (i>=0 or j>=0):
            x = int(num1[i]) if i>=0 else 0
            y = int(num2[j]) if j>=0 else 0
            s.insert(0, (x+y+c)%10)
            c = 1 if x+y+c > 9 else 0
            i,j = i-1, j-1 
        if (c) : s.insert(0, "1")
	print ''.join(str(x) for x in s)


Solution().addStrings("2", "3")
Solution().addStrings("9", "99")
Solution().addStrings("22", "33")
Solution().addStrings("229", "331")
Solution().addStrings("229", "31")
Solution().addStrings("229", "931")
