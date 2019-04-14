class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        # print (A, K)
        AK = []
        while (K):
            AK.insert(0, K%10)
            K //=10
            
        ret = []
        c = 0
        # print (A, AK)
        while (A or AK):
            k = AK.pop() if AK else 0
            a = A.pop() if A else 0
            s = k+ a + c
            c = s//10
            ret.insert(0, s%10)
            # print (A, AK)
        if (c) :
            ret.insert(0, c)
            
        return ret
