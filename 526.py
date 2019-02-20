import pdb
class Solution:
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        ''' backtracking '''
        nums = [i for i in range(1,N+1)]
        fillArray = [ 0 for i in range(N)]
        return self.recurse(nums, fillArray, 0)
        
    def recurse(self, nums, fillArray, total):
        #pdb.set_trace()
        if (0 not in fillArray or nums == None):
            #print (fillArray)
            return total+1

        for i in nums:
            numsT = nums.copy()
            fillArrayT = fillArray.copy()
            index = fillArrayT.index(0) +1
            if (i%index == 0 ) or (index%i == 0):
                fillArrayT[index-1] = i
                numsT.remove(i)
                total = self.recurse(numsT, fillArrayT, total)
        return total

for i in range(1,16):
   print (Solution().countArrangement(i))
