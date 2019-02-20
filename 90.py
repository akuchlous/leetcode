import pdb
from collections import deque

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # add single items 
        return self.dfs(nums, [[]])
    
    def dfs (self, nums, prevList):
        if (nums == []):
            return prevList
        newList = []
        #pdb.set_trace()
        #for n in nums:
        for p in prevList:
            newL = p+[nums[0]]
            newL.sort()
            if (newL not in newList):
                newList.append(newL)
        for p in prevList:
            if p not in newList:
               newList.append(p)
        return self.dfs(nums[1:], newList)

#print (Solution().subsetsWithDup([1,2,2]))
print (Solution().subsetsWithDup([4,4,4,1,4]))
