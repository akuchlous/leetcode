class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word : return True
        
        def dfs (x,y, board, visited, word):
            if word == "": 
                print visited
                return True
            
            for nx, ny in [(x-1, y), (x+1, y), (x,y-1), (x,y+1)]:
                if (nx, ny) not in visited :
                    if 0<=nx and nx<len(board) and 0 <=ny and ny<len(board[0]):
                        if (board[nx][ny] == word[0]):
                            ret = dfs (nx, ny, board , visited+[(nx,ny)], word[1:])
                            if ret == True : 
                                return True
            return False
            
            
        for x in range (len(board)):
            for y in range(len(board[0])):
                if (board[x][y] == word[0]):
                    if  dfs (x,y, board , [(x,y)], word[1:]): return True

	return False


print Solution().exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB")

