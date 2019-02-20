import pdb

import  inputs
def findAll(inStr, w):
        ret = []
        index = 0
        while (index > -1):
                i = inStr[index:].find (w)
                if (i == -1) :
                        index = -1
                else:
                        ret.append( index+i)
                        index=index+1
                if (index > len(inStr)):
                        index = -1
        return ret

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
	if (s == "") or (words == []): return []
	if (len (words) > len(s)): return []	
	pdb.set_trace()
	posWordMap = {}
	wordDict = {}
	allPos =  []
	wlen = len(words[0])
	totalCount = len(words)
	for w in words:
		if (w not in wordDict):
			wordDict[w] = 0
		wordDict[w]+=1
	c = s[0]
	allSame = True
	for i in range(0, len(s)):
		if (c != s[i]):
			allSame = False 
			break
		
	if (allSame and len(wordDict.keys()[0]) == 1 and len(wordDict) == 1 and c == wordDict.keys()[0] and (wordDict[wordDict.keys()[0]] <= len(s))):
		return range(0, len(s)-wordDict[wordDict.keys()[0]])
		
			
	for i in range(0, len(s)):
		if (s[i:i+wlen] in wordDict):
			posWordMap[i] = s[i:i+wlen]
			allPos.append(i)
	allPos.sort()
	allLoc  = []
	for p in posWordMap.iterkeys():
		nWords = dict(wordDict)
		count  = 0
		for i in range(0, len(words)):
			pos = p+(i*wlen)
			if (pos in posWordMap):
				if (nWords[posWordMap[pos]]>0):
					nWords[posWordMap[pos]]-=1
					count +=1 
				else:
					#duplicate
					break
			else:
				break
		if (count == totalCount):
			allLoc.append(p)
	return allLoc

# s =""
# words = []
# s ="aaaaaaaa"
# words = ["a","a","a", "a"]
# # s = "barfoothefoobarman"
# words = ["foo","bar"]
ret = Solution().findSubstring(inputs.str, inputs.words)
print ret
