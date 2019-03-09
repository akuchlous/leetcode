import pdb
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        currPos = 0
        zeroPos = -1
        # find firstzero
	pdb.set_trace()
        for i in range(len(nums)):
            if (nums[i] == 0): zeroPos = i;break

        if (zeroPos == -1): return 
        
        for idx in range(zeroPos, len(nums)):
            print (idx)
            if nums[idx] != 0 :
                nums[zeroPos], nums[idx] = nums[idx], nums[zeroPos]
                print (nums)
                zeroPos+=1

	print (nums)

#Solution().moveZeroes([0,1,0,3,12])
Solution().moveZeroes([1,0,1])
