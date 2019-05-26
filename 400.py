class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        tens = 1 
        maxTen = 10 ** tens
        count = 0
        index = 0 
        while (count < n):
            index+=1 
            if index < maxTen :
                count += tens
            else:
                tens+=1 
                maxTen = 10** tens 
                count+=tens
            print (index, count)

	index -= 1 
	count -= tens
        diff = n - count -1
        print (index,count, diff)
        return int(str(index)[diff])
            

print (Solution().findNthDigit(1))
print (Solution().findNthDigit(3))
# print (Solution().findNthDigit(11))
