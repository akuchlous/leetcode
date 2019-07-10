import pdb
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        def dp (stack, count):
            if count == 0  or not stack: return 0
            s0 = 0
            if len (stack)>1:
                if (stack[-1][1] > stack[-2][1]):
                    s0 = dp (stack[:-2] + [(stack[-2][0], stack[-1][1])], count)
            s1 = stack[-1][1]-stack[-1][0] + dp (stack[:-1], count-1) 
            s2 = dp (stack[:-1], count) 
            return max(s0, s1,s2)
        
        if not prices: return 0
        start  = end = prices[0]
        stack = []    # end val, 
        for p in prices[1:]:
            if (p < end):
                if (start != end): stack.append((start, end))
                start = p
                end = p
            else:
                end = p
        if (end > start): stack.append((start, end))
            
        return dp (stack, 2)

print Solution().maxProfit([3,3,5,0,0,3,1,4])

