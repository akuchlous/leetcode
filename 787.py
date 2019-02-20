from collections import deque
from collections import defaultdict
import sys


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        cost = {}
        steps = {}
        fPaths = defaultdict(list)
        for f in flights:
            fPaths[f[0]].append(f)
            cost[f[1]] = -1
            steps[f[1]] = 0
        cost[src] = 0
        print (cost)
        paths = deque()
        paths.append(src)
        while (not not paths):
            p = paths.pop()
            for localP in fPaths[p]:
                if ((cost[localP[1]] == -1) or (cost[localP[1]] > cost[localP[0]] + localP[2])):
                    if (steps[localP[1]] <= K):
                        steps[localP[1]] = steps[localP[1]] +1 
                        cost[localP[1]] = cost[localP[0]] + localP[2]
                        paths.append(localP[1])
        if (dst not in cost): return -1
        return cost[dst]



# print (Solution().findCheapestPrice( 3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))
print (Solution().findCheapestPrice( 2, [[1,0,5]], 0, 1, 1))

