class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def findNeighbors(x,y, X, Y, grid):
            result = []
            if (x-1>=0):
                # if (y-1 >= 0 and grid[x-1][y-1] == 1): 
                #     result.append((x-1,y-1))
                #     grid[x-1][y-1] = 0
                if (grid[x-1][y] == 1) : 
                    result.append((x-1,y))
                    grid[x-1][y]=0
                # if (y+1 < Y and grid[x-1][y+1] == 1): 
                #     result.append((x-1, y+1))
                #     grid[x-1][y+1] = 0
            
            if (y-1 >= 0 and grid[x][y-1] == 1):
                result.append((x, y-1))
                grid[x][y-1]=0
                
            if (y+1 < Y and grid[x][y+1] == 1):
                result.append((x, y+1))
                grid[x][y+1]=0
                
            if (x+1 < X):
                # if (y-1 >= 0 and grid[x+1][y-1] == 1): 
                #     result.append((x+1,y-1))
                #     grid[x+1][y-1] = 0
                if (grid[x+1][y] == 1) : 
                    result.append((x+1,y))
                    grid[x+1][y]=0
                # if (y+1 < Y and grid[x+1][y+1] == 1): 
                #     result.append((x+1, y+1))
                #     grid[x+1][y+1] = 0
            
            return result
        
        maxArea = 0
        X , Y = len(grid), len(grid[0])
        for x in range(X):
            for y in range(Y):
                area = 0
                if (grid[x][y]):
                    grid[x][y] = 0
                    connected1s = [(x,y)]
                    while connected1s:
                        area+=1
                        (x,y) = connected1s.pop(0)
                        connected1s.extend(findNeighbors(x,y,X, Y, grid))
                maxArea = max(area, maxArea)
            
            
        return maxArea
