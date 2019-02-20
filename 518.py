import pdb

class Solution:
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        ways = [0 for x in range (amount+1)]
        ways[0] = 1
        print(ways)
        for coin in coins:
            for c in range(coin, amount+1):
               ways[c] += ways[c-coin]
        print(ways)
        return ways[amount]

#print(Solution().change(4, [4]))
#print(Solution().change(3, [1,2]))
print(Solution().change(5, [1,2,3]))
