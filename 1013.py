import collections 

class Solution:
    def numPairsDivisibleBy60(self, time):
     
        lenMap = collections.defaultdict(int)
        total = 0
        for t in time:
            if (60 - (t%60)  in lenMap): total+= lenMap[60 - (t%60)]
            print (lenMap)
            lenMap[t%60] = lenMap[t%60] +1
	    print (total)
        return total


print (Solution().numPairsDivisibleBy60([60,60,60]))
