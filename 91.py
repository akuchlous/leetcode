class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (s == ""): return 0
        c = 1
        for i in range (1, len(s)):
            if (s[i]<"7") and (s[i-1] <"3"): 
                c = c+1 
        return c

print (Solution().numDecodings("12"))
print (Solution().numDecodings("226"))
