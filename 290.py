import pdb
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strL = str.split(" ")
        print(strL)
        i = 0
        dict = {}
        for p in pattern:
            if (p in dict):
                #print(dict[p], strL[i])
                if (dict[p] != strL[i]): 
                    return False
            dict[p] = strL[i]
            i+=1 
            if (i >= len(strL)): break
        return True

# print(Solution().wordPattern("abba", "dog cat cat dog"))
# print(Solution().wordPattern("abba", "dog cat cat fish"))
# print(Solution().wordPattern("e", "eureka"))
## print(Solution().wordPattern("jquery", "jquery"))
print(Solution().wordPattern("abba", "dog dog dog dog"))
