class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        i = 0
        prev = A[i]
        i+=1 
        nextI = A[i]
        while (nextI > prev):
            i+=1
            prev, nextI = nextI, A[i]
        i-=1
        return i
