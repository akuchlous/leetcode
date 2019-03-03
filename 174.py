class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
	def printM(dungeon):
            rows = len(dungeon)
            cols = len(dungeon[0])
            for i in range (rows):
	        buf = ""
                for j in range(cols):
		    buf += str(dungeon[i][j]) + " " 
		print (buf)
            print ("\n")

	printM(dungeon)  
        rows = len(dungeon)
        cols = len(dungeon[0])
        for i in range (rows):
            for j in range(cols):
                if (i == 0):
                    if (j == 0): continue
                    else: dungeon[i][j] += dungeon[i][j-1]
                else:
                    if (j == 0): dungeon[i][j] += dungeon[i-1][j]
                    else: dungeon[i][j] += max(dungeon[i][j-1], dungeon[i-1][j])
		print (i,j)
	        printM(dungeon)  

        return dungeon[rows-1][cols-1]

Solution().calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]])
