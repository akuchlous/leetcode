import pdb
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l , r =  0, len(nums)-1
        while (l<=r):
            mid = (l+r)//2
            print (l, r, mid)
            if (nums[mid] == target):
                return mid
            elif (nums[mid] > target):
                r = mid -1
            else:
                l = mid +1
        return -1 

#print(Solution().search(nums = [-1,0,3,5,9,12], target = 9))
print(Solution().search([-1,0,3,5,9,12] ,13))

