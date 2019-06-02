import pdb
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
	pdb.set_trace()
        if N <2: return 0
        
        while N%2 == 0:
            N//=2 
        arr = [0]
        N//=2 
        cnt = 1 
        while (N):
            if (N %2 == 1) : 
                arr.append(cnt) 
                cnt=1
            else:
                cnt+=1
            N//=2
        return max(arr)


print(Solution().binaryGap(8))
