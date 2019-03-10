class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        revD = digits[::-1]
        carry = 1
        results = []
        for d in revD:
            nd = d + carry 
            carry = nd//10
            results.append(nd%10)
        if (carry): results.append(1)
        return results[::-1]
