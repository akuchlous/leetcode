import pdb
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [[1], [1,1]]
        count = 1
        while (count < rowIndex):
            count += 1 
            row.append([1])
            for i in range(1,count):
                row[count].append(row[count-1][i-1] + row[count-1][i])
            row[count].append(1)

        return row[rowIndex]

print (Solution().getRow(5))
