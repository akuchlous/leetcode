import pdb
class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        # 3 1 1 2
        # 3 1 4 2
        # 1 1 2 2
        minL = [nums[0]]
        for i in range(1, len(nums)):
           minL.append( minL[i-1])
           if (nums[i] < minL[i-1]):
              minL[i] = nums[i]

        nums.reverse()
        minR = [nums[0]]
        for i in range(1, len(nums)):
           minR.append( minR[i-1])
           if (nums[i] < minR[i-1]):
              minR[i] = nums[i]

        nums.reverse()
        minR.reverse()
        print (nums)
        print (minL)           
        print (minR)           
        for i in range(1,len(nums)-1):
           if (nums[i] > minL[i]) and (nums[i] > minR[i]):
              print (i , nums[i], minL[i], minR[i])
              return True
        return False 


print (Solution().find132pattern([1,0,1,-4,-3])
)
