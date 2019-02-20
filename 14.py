import pdb
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (strs == []): return ""
        i = 0 
        pdb.set_trace()
        while (True):
            if (i >= len(strs[0])):
                return strs[0][:i]
            c = strs[0][i]
            
            for r in range(0, len(strs)-1):
                if ((i > len(strs[r])-1) or c != strs[r][i]):
                    if (i == 0): return ""
                    
                    return strs[0][:i-2]
            i+=1
            
        return strs[0][:i-1]
        

print (Solution().longestCommonPrefix(["a", "b"]))
