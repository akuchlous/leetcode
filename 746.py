class Solution:
   def minCostClimbingStairs(self, cost):
       """
       :type cost: List[int]
       :rtype: int
       """
       L = len(cost)
       newA = [0 for x in range (L)]
       newA[0:2] = cost[0:2]
       for s in range (2, L):
               newA[s] = min(cost[s]+ newA[s-1], cost[s]+newA[s-2])
       print (min(newA[-1], newA[-2]))


Solution().minCostClimbingStairs([10, 15, 20])
Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
               
