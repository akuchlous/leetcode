import pdb
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        results = []
        self.recurse ([], candidates, target, results)
	sResults = [sorted(x) for x in results]
	newList = []
	for s in sResults :
	   if s not  in newList:
	       newList.append(s)
        return newList
    
    def recurse (self, partial,  candidates, target, results):
        for c in candidates:
            newPartial = partial + [c]
            newTarget = target - c 
            if (newTarget == 0):
                results.append(newPartial)
            elif (newTarget > 0):
                self.recurse (newPartial, candidates, newTarget, results)


print (Solution().combinationSum([2,3,6,7], 7))
