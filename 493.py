import pdb
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute force is easy 
        nA, nc = self.mergeSort(nums)
    
    def mergeSort(self, nums):
        if (len(nums) == 1):
            return nums, 0
        mid = len(nums)//2
        nA = []
        pdb.set_trace()
        lA, lc = self.mergeSort(nums[:mid])
        rA, rc = self.mergeSort(nums[mid:])
        count = lc + rc
        while (len(lA) >0 or len(rA)>0):
            if (len(lA) >0 and len(rA) >0):
                if (lA[0] > rA[0] ):
                    if (lA[0] > 2*rA[0]): count+=1 
                    nA.append(rA.pop())
                else:
                    nA.append(rA.pop())
        return (nA, count)


Solution().reversePairs([2,4,3,5,1])
