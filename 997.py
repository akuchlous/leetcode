from collections import defaultdict 
import pdb

class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trustMap = {}
        allP = set()
        for l in trust:
	    pdb.set_trace()
            [person, ptrust] = l
            if (ptrust not in trustMap):
                # trust self 
                trustMap[ptrust] = set(ptrust)
            # list of ppl who trust him
            ptrust.add(person)
            allP.add(person)
        
        for p in trust:
            if (trustMap[p] == allP):
                return p
        return -1 


print (Solution().findJudge(2, [[1,2]]))
