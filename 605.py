class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        p = 0 
        while p < len(flowerbed):
            if (flowerbed[p]): 
                    p+=1
                    continue
            if p > 0 and p <len(flowerbed)-1:
                if (not flowerbed[p-1] and not flowerbed[p+1]):
                    n-=1
                    flowerbed[p]=1
            
            elif (p == len(flowerbed)-1): # last element 
                if (not flowerbed[p-1]):
                    n-=1
                    flowerbed[p]=1
            elif (p == 0): # start 
                if (not flowerbed[p+1]):
                    n-=1 
                    flowerbed[p]=1
                    
            p+=1
        return n<=0
