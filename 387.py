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
                
        for i in range(len(s)):
            if (uniq[s[i]] == 1 ): return i

	return -1

print (Solution().firstUniqChar("dddccdbba"))
print (Solution().firstUniqChar("loveleetcode"))

