class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
	start = 0
	uniqC = set(s[0])
	largest = s[0]
	current = s[0]
	# get next element
	#pdb.set_trace()
	for i in range(1, len(s)):
		current+=s[i]
		if (s[i] not in uniqC):
			uniqC.add(s[i])
		else:
			#pdb.set_trace()
			for j in range(0, len(current)-1):
				#print current , j
				if (current[j] == s[i]):
					current = current[j+1:]
					break
				else:
					uniqC.remove(current[j])
		if len(largest) < len(current):
			largest = current
	return largest




s  = Solution()

print s.lengthOfLongestSubstring("abcd")
print s.lengthOfLongestSubstring("abcdabce")
print s.lengthOfLongestSubstring("abcdeadc")
print s.lengthOfLongestSubstring("bbbbbb")
