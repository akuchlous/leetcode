import pdb 
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        def neighbors(x, y, board, covered):
            nList = []
            maxX = len(board)
            maxY = len(board[0])
            if (x >0): # Left
                nList.append((x-1, y))
            if (x<maxX-1): # Right
                nList.append((x+1, y))
            if (y>0): # Up 
                nList.append((x, y-1))
            if (y<maxY-1): # Up 
                nList.append((x, y+1))
            #print (nList)
            return nList
            
        def backtrack(x,y, board, word, covered):
            #pdb.set_trace()
            if (word == "") : return True
            nbs = neighbors(x,y,board, covered)
            for n in nbs:
                if (n in covered):
                    continue
                else:
                    x,y = n
                    if board[x][y] != word[0]:
                        continue
                    else:
                        covered.append(n)
                        retVal = backtrack(x,y, board, word[1:], covered)
                        if not retVal :
                            covered.remove(n)
                        else:
                            return retVal
            return False
            
            
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] == word[0]):
                    retVal =  backtrack (i, j, board, word[1:], [(i,j)])
                    if (retVal): return True
                    else: continue


        return False


print(Solution().exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))


