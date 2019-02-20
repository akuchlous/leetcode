import pdb

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        neg = (n < 1)
        p = 2
        product = 1 
        #print("{0:b}".format(abs(n)))
        #pdb.set_trace()
        for y in reversed("{0:b}".format(abs(n))):
            if (y == "1"):
                product = product * p
            p = p*p 
                
        if (neg):
            product = 1/product
            
        return product

#print(Solution().myPow(2.0,10))
print(Solution().myPow(2.0,1))
print(Solution().myPow(2.0,2))
print(Solution().myPow(2.0,4))
print(Solution().myPow(2.0,5))
print(Solution().myPow(2.0,10))


