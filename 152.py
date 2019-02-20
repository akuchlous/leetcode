import pdb
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #pdb.set_trace()
        negM = [1]  # negMarkers
        maxP = max(nums)
        for n in nums: 
            added = False
            l = len(negM)
            for i in range(0,l):
                    negM[i] = negM[i]*n
                    maxP = max(maxP, negM[i])
            print(negM)
            if (n<0):
                negM.append(1)
                added = True
        if (added == True): negM.pop()
        return max(max(negM), maxP)

#print (Solution().maxProduct([2,3,-2,4]))
print (Solution().maxProduct([-2,0,-1]))


