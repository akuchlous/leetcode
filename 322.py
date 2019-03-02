class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
    
        def recurse(coins, amount, coinsAdded, results):
            for c in coins:
                remain = amount - c
                newComb = coinsAdded + [c]
                if (remain == 0): 
                    results.append(newComb)
                elif (remain >0):
                    recurse (coins, remain, newComb, results)
                    
        results = []
        recurse(coins, amount, [], results)
        if (not results) : return -1
        return len(min(results, key=len))
