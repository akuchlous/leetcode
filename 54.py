import pdb
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        dA = [(0,1), (1,0), (0,-1), (-1,0)]
        d = 0
        posx, posy = 0,0
        
        for i in range(1, (len(matrix) * len(matrix[0]))+1):
            print "p", posx, posy
            matrix[posx][posy] = i

            npx, npy = posx + dA[d][0], posy + dA[d][1]
            if len(matrix)-1<npx or npx<0  or len(matrix[0])-1<npy or npy <0 or  matrix[npx][npy] != 0 :
                d = (d+1) % 4 
                npx, npy = posx + dA[d][0], posy + dA[d][1]
            posx, posy = npx, npy
        print matrix


m = [[0 for y in range(3)] for x in range(3)]
print m
Solution().spiralOrder(m)
