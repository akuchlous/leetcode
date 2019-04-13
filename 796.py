class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if not A and not B  : return True
        allF = [i for i in range(len(A)) if A[i] == B[0]]
        for l in allF:
            if (B == A[l:]+A[:l]): return True
            
        return False 
