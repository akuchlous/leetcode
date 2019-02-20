import pdb 
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        startPos = 0
        endPos = len(s) - 1 
        removed=False
        pdb.set_trace()
        while (True):
            print (s[startPos], s[endPos])
            if (startPos >= endPos): return True
            if (s[startPos] == s[endPos]):
                startPos+=1
                endPos-=1
            elif ((removed==False)  and (s[startPos+1] == s[endPos])):
                    startPos +=2
                    endPos   -= 1
                    removed = True
            elif ((removed == False) and (s[startPos] == s[endPos-1])):
                    startPos += 1
                    endPos   -= 2 
                    removed = True
            else:
                return False
        return True

# print (Solution().validPalindrome("aba"))
# print (Solution().validPalindrome("abc"))
# print (Solution().validPalindrome("abca"))
# print (Solution().validPalindrome("abcdcbba"))
# print (Solution().validPalindrome("atbbga"))
#print (Solution().validPalindrome("eddboebddcaacddkbebdde"))
print (Solution().validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
