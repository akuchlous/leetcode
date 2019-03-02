from collections import OrderedDict

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        uniq = OrderedDict()
        for i in range(len(s)):
            if s[i] not in uniq:
                uniq[s[i]] = 1 
            else:
                uniq[s[i]] += 1 
                
        i = 0 
	print (uniq)
        for k in uniq.keys():
            if (uniq[k] == 1 ): return i
            i+=uniq[k]
            
        return -1


print (Solution().firstUniqChar("dddccdbba"))

