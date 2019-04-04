from collections import Counter 

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        lenP = len(p)
        pC = Counter(p)
        sC = Counter(s[:lenP])
        retVal = []
        if pC == sC  : retVal.append(0)
        for i in range(lenP, len(s)):
            sC[s[i-lenP]] = sC[s[i-lenP]] - 1 
            if (sC[s[i-lenP]] == 0) : del sC[s[i-lenP]] 
            sC[s[i]] = sC[s[i]] +1 
            if (pC == sC) : 
                retVal.append(i-lenP +1)        
        return retVal
    
