import pdb
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.recurseS(nums, target, 0)
    
    def recurseS(self, nums, target, start):
        print (nums, target)
        pdb.set_trace()
        if (len(nums) == 1):
            if (nums[0] == target):
                return start
            else:
                return -1 
         
        mid = len(nums)//2
        if nums[mid] == target: return start + mid
        if (target > nums[mid] and target < nums[0] and nums[0] > nums[mid]):
            return self.recurseS(nums[:mid], target, mid)
        else:
            return self.recurseS(nums[mid:], target, mid)



print (Solution().search([4,5,6,7,0,1,2], 0))
