import pdb
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        nb = [[board[x][y] for y in range(len(board[0]))] for x in range(len(board))]
        for x in range (len(board)):
            for y in range (len(board[0])):
                n = [(x,y)]
                c = 0
                for nx,ny in ((x-1, y-1), (x,y-1), (x+1,y-1), (x-1,y), (x+1,y), (x-1, y+1), (x, y+1), (x+1, y+1)):
                    if (0<=nx<len(board) and 0<=ny<len(board[0])):
                        c+=board[nx][ny]
                        n.append((nx,ny))
                if board[x][y] == 1  :
                    if (3<c or c<2): 
                        nb[x][y] = 0
                elif board[x][y] == 0 and c == 3 : 
                        nb[x][y] = 1 
        board = nb 
        return board

def printM(m):
	for r in m:
		print r

m = [ [0,1,0], [0,0,1], [1,1,1], [0,0,0] ]
m = [ [0,1,0],[0,0,1],[1,1,1],[0,0,0]]

n = Solution().gameOfLife(m)
printM(m)
print
printM(n)


