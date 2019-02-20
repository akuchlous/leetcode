import pdb
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxA = 0
        pdb.set_trace()
        for currI in range(0, len(heights)):
            minH = heights[currI]
            areaT = heights[currI]
            i = 1
            indx = currI-1
            while (indx >= 0):
                i+=1
                minH = min(minH, heights[indx])
                areaT = max(areaT, i*minH)
                indx = indx -1
            maxA = max(maxA, areaT)
        return maxA

print (Solution().largestRectangleArea([1,1]))
