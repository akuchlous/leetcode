import string 
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newS = ""
        for c in s:
	    print (c)
            if (c.isalnum()):
                newS+=c.lower()
	print (newS)
        return newS==newS[::-1]


print (Solution().isPalindrome("0P"))

