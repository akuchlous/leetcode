import pdb
from collections import defaultdict 
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        mapping = defaultdict(list)
        for e in edges:
            mapping[e[0]].append(e[1])
            mapping[e[1]].append(e[0])
        
        minDist , minDNodes = n, []
	minHeight = n
        for p in xrange(n):
            height = 0
            visited = []
            queue = []
            newQueue = [p]
            while (len (visited) < n):
                queue = newQueue
                newQueue = []
                while (queue):
                    node = queue.pop()
                    visited.append(node)
                    for nn in mapping[node]:
                        if nn not in visited:
                            newQueue.append(nn)
                height+=1
            if height < minDist:
		minDist = height
		minDNodes = [p]
            elif height == minDist:
		minDNodes.append(p)
	

            
        print minDNodes 

Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]);
Solution().findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
