from collections import defaultdict
import re

def substring_indexes(substring, string):
    """ 
    Generate indices of where substring begins in string

    >>> list(find_substring('me', "The cat says meow, meow"))
    [13, 19]
    """
    last_found = -1  # Begin at -1 so the next position to search from is 0
    while True:
        # Find next index of substring, by starting after its last known position
        last_found = string.find(substring, last_found + 1)
        if last_found == -1:  
            break  # All occurrences have been found
        yield last_found

class Solution:
   def wordBreak(self, s, wordDict):
      """
      :type s: str
      :type wordDict: List[str]
      :rtype: bool
      """
      # find all occurences of words in string and make a map
      posMap = defaultdict(list)
      for w in wordDict:
              allP = substring_indexes(w, s)
              for p in allP:
                      posMap[p].append(len(w)) 
      return (self.bk (0,posMap,s))

   def bk(self, pos, posMap, s):
      
      for e in posMap[pos]:
         if (pos + e == len(s)) : return True
         elif (pos +e > len(s)): return False
         else: 
              if (self.bk(pos+e, posMap, s) == True):
                  return True 
      return False


# c = Solution().wordBreak("applepenapple", ["apple", "pen"])
# c = Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
print(Solution().wordBreak("aaaaaaa", ["aaaa", "aaa"]))
