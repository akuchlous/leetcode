import pdb
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
	pdb.set_trace()
        pow10  = 0
        if (n > 9 * (10**pow10)):
            n= n - (9 *(pow10+1)* (10**pow10))
            pow10+=1 
        
        c = 10**pow10
        print "1", n,c 
        charSize = pow10+1 
        n-=pow10+1
        print n,c 
        while (n>0):
            c+=1 
            n-=charSize
            print "loop",n,c 
        
        print str(c)[n-1]


#Solution().findNthDigit(13)
Solution().findNthDigit(11)
