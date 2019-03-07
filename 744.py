class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        retVal = None
        for t in letters[::-1]:
	    if (t > target): retVal = t
        if (not retVal):
            retVal = letters[0]
        return retVal


print (Solution().nextGreatestLetter(["c","f","j"], "c"))
