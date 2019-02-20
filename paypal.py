import pdb
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        matrix = []
        matrix = [[0 for x in range(numRows)]  for y in range(len(s))]
        for x in range(0,numRows):
            matrix[x] = []
            for y in range(0,len(s)):
                matrix[x].append(0)
			
        i =j = 0   # currentPos
        goVertical = True
        for c in s:
            matrix[i][j] = c
            if (goVertical): 
                    if (i== numRows-1 ): 
                            goVertical = False
                            i = i-1 
                            j = j+1 
                    else:
                            i+=1 
            else:
                    if (i != 0):
                            goVertical = True
                            i=i-1
                            j=j+1 
                    
        retStr = ""
        for x in range(0,numRows):
            for y in range(0,len(s)):
                if (matrix[x][y]!= 0):
                        retStr += matrix[x][y]
                matrix[x].append(0)
        return retStr

s = Solution().convert("PAYPALISHIRING",3) 
