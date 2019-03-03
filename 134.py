class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
	pass
	
gas  = [4,5,1,2,3]
cost = [1,2,3,4,5]
t = 0
for (g,c) in zip(gas,cost):
    t += g-c
    print (t)

print (t)

