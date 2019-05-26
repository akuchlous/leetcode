import pdb

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1 
        ptr = 0
        pdb.set_trace()
        for i in range(1, len(nums)):
            if (nums[i] != nums[i-1]):
                for r in range(min(2, count)):
                    nums[ptr] = nums[i-1]
                    ptr+=1
                count = 1
            else: 
                count+=1 

        for r in range(min(2, count)):
            nums[ptr] = nums[-1]
            ptr+=1

	return nums


print (Solution().removeDuplicates([1,1,1,2,2,3]))


