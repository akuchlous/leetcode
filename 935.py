class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        mapping = {
            1 : [6,8],
            2 : [7,9],
            3 : [4,8],
            4 : [3,9,0],
            5 : [],
            6 : [1,7,0],
            7 : [2,6],
            8 : [1,3],
            9 : [4,2],
            0 : [4,6],
        }
        
        if N==0 : return 0
        q = [1,2,3,4,5,6,7,8,9,0]
        for i in range(1,N):
            newQ =  []
            for p in q:
                newQ+=mapping[p]
            q = newQ
            
        # print q
        return len (q)

print Solution().knightDialer(1)
print Solution().knightDialer(2)
print Solution().knightDialer(3)
print Solution().knightDialer(4)
print Solution().knightDialer(24)
