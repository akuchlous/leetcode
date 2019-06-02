import pdb
from collections import Counter
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        tLen = len(S)
        cntr = Counter(S)
        newStr = [" " for s in S]
        filled = 0
	l = sorted(cntr.keys(), key=lambda x: (-1*cntr[x], x))
        for s in l:
                pos = filled 
		while (newStr[pos] != " "): pos+=1
                for x in range(cntr[s]):
                        newStr[pos] = s
			pos += 2
                filled+=1
        return "".join(newStr)


print Solution().reorganizeString("aba")
# Solution().reorganizeString("vvvlo")
print Solution().reorganizeString("bfrbs")
