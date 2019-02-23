class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def isValid( board, i, j, setVal):
            val = board[i][j]
            if ( val == "."): return True
            if ( val in setVal): 
                # print (i,j, setVal, val)
                return False
            return True

        for i in range(9):
            vals = set([0])
            # print ("row", i)
            for j in range(9):
                if (not isValid(board, i, j, vals)): return False
                vals.add(board[i][j])
                
        for j in range(9):
            # print ("col", j)
            vals = set([0])
            for i in range(9):
                if (not isValid(board, i, j, vals)): return False
                vals.add(board[i][j])

        rows = [0, 3, 6]
        cols = [0, 3, 6]
        for r in rows:
            for c in cols:
                vals = set([0])
                # print ("row col", r,c)
                for i in range(0,3):
                    for j in range(0,3):
                        if (not isValid(board, r+i, c+j, vals)): return False
                        vals.add(board[r+i][c+j])
                        
        return True
