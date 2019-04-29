class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        i = iter(set(pattern))
        newStr = ""
        sDict = {}
        for w in str.split(" "):
            if (w not in sDict):
                try:
                    sDict[w] = i.next()
                except StopIteration:
                    return False
            newStr+=sDict[w]
        print (newStr)
        return (newStr == pattern)


#print(Solution().wordPattern("abba", "dog cat cat fish"))
print(Solution().wordPattern("abc", "b c a"))
