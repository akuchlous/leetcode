class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        comp = set()
        p = set()
        for i in range(2, n):
            if (i in comp): continue
            x = 1 
            if (i not in comp): p.add(i)
            while (i*x < n):
                comp.add(i*x)
                x+=1 
        return p


print (Solution().countPrimes(100))
