import pdb
class Solution:
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        print (points)
        for i in range(-3, len(points)-1):
            pdb.set_trace()
            [x0, y0] = points[i]
            [x1, y1]= points[i+1]
            print (x1, y1)
            [x2, y2] = points[i+2]
            print (x0, y0, x1, y1, x2, y2)
            if (x0<x1) and (x2<x1) : return False 
            if (x0>x1) and (x2>x1): return False 
            if (y0<y1) and (y2<y1) : return False 
            if (y0>y1) and (y2>y1) : return False
        return True
        

#print (Solution().isConvex([[0,0],[0,10],[5,5],[10,10],[10,0]]
print (Solution().isConvex([[0,0],[0,1],[1,1]] ))
