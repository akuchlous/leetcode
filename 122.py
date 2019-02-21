class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if (not prices): return 0
        prevPrice = prices.pop(0)
        while (prices):
            newPrice = prices.pop(0)
            if (newPrice > prevPrice):
                profit += newPrice-prevPrice
            prevPrice = newPrice 
        return profit
