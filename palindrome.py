#!/usr/bin/env python
import pdb

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
	if (s == "") : return s
	max = len(s)
	largest = s[0]
	# pdb.set_trace()
	for i in range(1,max):
		currentLargest =  s[0]
		if (s[i] == s[i-1]):
			currentLargest = s[i-1:i+1]
			l = i - 2 
			r = i +1
			while ( l>=0 and r <max and (s[l] ==  s[r]) ):
				currentLargest =  s[l:r+1]
				l-=1
				r+=1
			if (len(currentLargest)  > len(largest)):
				largest = currentLargest
		if (i < max-1 and s[i-1] == s[i+1]):
			currentLargest = s[i-1:i+2]
			l = i-2 
			r = i+2
			while ( l>=0 and r <max and (s[l] ==  s[r]) ):
				currentLargest =  s[l:r+1]
				l-=1
				r+=1
			if (len(currentLargest)  >= len(largest)):
				largest = currentLargest
		
	return largest
        


s = Solution()
print "P:" , s.longestPalindrome("")
print "P:" , s.longestPalindrome("x")
print "P:" , s.longestPalindrome("bb")
print "P:" , s.longestPalindrome("ccc")
print "P:" , s.longestPalindrome("cbbc")
print "P:" , s.longestPalindrome("babad")
print "P:" , s.longestPalindrome("aaaaaacbbc")
print "P:" , s.longestPalindrome("abcddcba")
print "P:" , s.longestPalindrome("aba")
print "P:" , s.longestPalindrome("aaabaaa")
print "P:" , s.longestPalindrome("aaabaca")
