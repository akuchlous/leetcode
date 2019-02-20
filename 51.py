import pdb
import copy
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [["." for x in range(n)]for y in range(n)]
        allB = []
        self.recursive(board, 0, allB)
        # for b in allB:
        #     self.printBoard(b)
        return allB
    
    def checkValidPos(self, board, row, p):
        #self.printBoard(board)
        if (row == 0): return True
        # vertical up
        for x in range (0, row):
            if (board[x][p] == 'Q'): return False 
        
        # horizontal not needed

        # up left
        r,c = row-1, p-1
        while (r>=0 and c>=0):
            if (board[r][c] == 'Q'): return False 
            r, c = r-1, c-1 
        
        # up right
        r,c = row-1, p+1
        while (r>=0 and c<len(board)):
            if (board[r][c] == 'Q'): return False 
            r, c = r-1, c+1 

        return True
 
    def printBoard(self, b):
        for r in b:
            print (r)
        print ("\n\n")

    def recursive(self, board, row, allB):
        if (row > len(board)-1): return 
        for p in range(len(board[0])):
            board[row][p] = "Q"
            if (self.checkValidPos(board, row, p)):
                if (row == len(board)-1):
                    n = [ "".join(board[i]) for i in range(len(board))]
                    allB.append(n)
                else:
                    self.recursive(board, row+1, allB)
            board[row][p] = "."
           
print(Solution().solveNQueens(5))
