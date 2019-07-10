class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        s = 0
        i = 0
	target = abs(target)
        while (s <target):
            i+=1
            s = s+i
        return i

print Solution().reachNumber(2)
print Solution().reachNumber(-2)
print Solution().reachNumber(4)
print Solution().reachNumber(10)
print Solution().reachNumber(1000)
