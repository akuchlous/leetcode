import pdb
from collections import defaultdict 
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        allN = [x for x in range(numCourses)]
        preReqForMe   = defaultdict(list)
        canFullFill = defaultdict(list)
        for l in prerequisites:
            a,b = l
            # print a,b
            preReqForMe[a].append(b)
            canFullFill[b].append(a)
            if (a) in allN: allN.remove(a)
            if (b) in allN : allN.remove(b)
            
        #can be taken first
        
        covered =  list(set(canFullFill.keys()) - set(preReqForMe.keys()))
        allC = set([x for x in range(0, numCourses)])
	print (covered)
        canTake = list(set(covered).union(allN))
        while (covered):
            c = covered.pop()
            for nxtC in canFullFill[c]:
                if nxtC in canTake: continue
                preR = preReqForMe[nxtC]
                if not (set(preR) - set(canTake)):
                    canTake.append(nxtC)
                    covered.append(nxtC)

                    
        if (not allC - set(canTake)): return canTake
        return []


print Solution().findOrder(2, [[1,0]])




