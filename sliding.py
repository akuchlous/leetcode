import pdb
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        retVal = []
        m = 0
        for x in range(0, len(nums)-k):
            retVal.append(max(nums[x:x+k]))
        return retVal

print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))

