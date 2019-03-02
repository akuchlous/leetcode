 class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        total = 0
        for i in range(rows): # rows 
            for j in range(cols): # cols 
                if not grid[i][j] : continue
                total+=4
                if (i != 0 ) and (grid[i-1][j] == 1): total -=1  
                if (i != rows -1 ) and (grid[i+1][j] == 1): total -=1  
                if (j != 0 ) and (grid[i][j-1] == 1): total -=1  # left
                if (j != cols -1) and  (grid[i][j+1] == 1): total -=1  # right
                        
        return total
