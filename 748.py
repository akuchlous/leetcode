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

from collections import Counter 
import string

# Solution II 
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        lC = Counter()
        for l in licensePlate.lower():
            if l in string.ascii_lowercase:
                lC[l] +=1 
                
        small = None
        
        for w in words:
            wC = Counter(w)
            if (not (lC - wC)):
                if not small or (len(small) > len(w)): 
                    small = w

                    
        return small


print (Solution().shortestCompletingWord("1s3 PSt", ["step","steps","stripe","stepple"]))

