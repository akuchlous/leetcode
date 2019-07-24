import pdb
from collections import Counter
from guppy import hpy
class Solution(object):
    #@profile
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        h = hpy()
        def isSubset(small, big):
           for k in small.keys():
              if (small[k] > big[k]): return False
           return True

        if (len(s) < len(t)): return ""
        allValues = ""
        c = Counter(t)
	cs = Counter (s)
	if (not isSubset(c, cs)): return False 
        start = end = 0 
	bigS = s[start:end]
	bigC = Counter(bigS)
        while (end<len(s)):
	   end+=1 
	   bigC [s[end-1]]+=1
	   bigS = s[start:end]
	   while (isSubset(c, bigC)):
	      bigS = s[start:end]
	      if (len(allValues) >end-start+1):
	         allValues = s[start:end]
	      # allValues.append(bigS)
	      bigC [s[start]]-=1
	      start+=1 
        print h.heap()
	return allValues


#print (Solution().minWindow("ADOBECODEBANC", "ABC"))
#print (Solution().minWindow("a", "aa"))
#print (Solution().minWindow("a", "b"))
