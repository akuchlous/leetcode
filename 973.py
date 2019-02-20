from math import sqrt

class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        l = [(pow(x,2)+pow(y,2), [x,y]) for [x,y] in points]
        l.sort()
        print (l)
        minD = l[0][0]
        ret = []
        for d in l:
            if d[0] == minD : ret.append(d[1])
        return ret


print (Solution().kClosest([[3,3],[5,-1],[-2,4]], 2))

