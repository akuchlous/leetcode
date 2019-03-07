import pdb
import string 
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        allChars = set(licensePlate.lower()).intersection(set(string.ascii_lowercase))
        retVal = None
	pdb.set_trace()
        for w in words:
            if set(w).issuperset(set(allChars)): 
                if (not retVal) or (len(retVal) > w):
                    retVal = w
            
        return retVal

print (Solution().shortestCompletingWord("1s3 PSt", ["step","steps","stripe","stepple"]))

