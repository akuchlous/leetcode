class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        newList = d.copy()
        l = len(newList)
        words = ["",""]
        for c in s :
            for i in range(0,l):
                if ((newList[i]!= "") and (newList[i][0] == c)):
                    newList[i] = newList[i][1:]
                    if (newList[i] == ""): 
                        if (len(words[0]) < len(d[i])):
                            words = [d[i]]
                        elif (len(words[0]) == len(d[i])):
                            words.append(d[i])
                    print (words)
        return min(words)

print (Solution().findLongestWord("abpcplea",["ale","apple","monkey","plea"]))
print (Solution().findLongestWord("bab", ["ba","ab","a","b"]))

