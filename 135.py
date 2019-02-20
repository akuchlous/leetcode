class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        rT = [1 for x in range(len(ratings))]
        lT = [1 for x in range(len(ratings))]
        for r in range(1, len(ratings)):
            if (ratings[r-1] < ratings[r]): rT[r] = rT[r-1]+1
        print (rT)
        for l in list(range(len(ratings)-2,-1)):
            print(l)
            if (ratings[l] > ratings[l+1]): lT[l] = lT[l+1]+1
        
        print (lT)
        for r in range(0, len(ratings)):
            rT[r] = max(rT[r], lT[r]) 
            
        print (rT)
        return sum(rT)


print (Solution().candy([1,0,2]))
