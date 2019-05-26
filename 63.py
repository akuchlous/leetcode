import pdb
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        grid = obstacleGrid
        ways = [[0 for x in range(len(grid[0]))] for y in range (len(grid))]
        if grid[0][0] == 1 : return 0
        else: ways[0][0] = 1
        print (ways)
        for i in range (len(grid)):
            for j in range(len(grid[0])):
		pdb.set_trace()
                if (i == 0 and j == 0) : continue
                up = ways[i-1][j] if ((i > 0) and (grid[i-1][j] == 0)) else 0
                left = ways[i][j-1] if ((j>0) and (grid[i][j-1] == 0)) else 0
                ways[i][j] = up + left 
                # print (i, j , ways)
                
        return ways[i][j]


print (Solution().uniquePathsWithObstacles([[0,0]]))

