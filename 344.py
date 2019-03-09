class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l = len(s)
        for i in range(l/2):
            print (i, l-i-1)
            s[i], s[l-i-1] = s[l-i-1], s[i]
            print (s)


Solution().reverseString(["h","e","l","l","o"])

