class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if (not numbers): return numbers
        i = 0 
        j = len(numbers) -1 
        while (i != j):
            s2n = numbers[i] + numbers[j]
            if (s2n == target):
                return [i+1,j+1]
            elif (s2n<target):
                i+=1 
            else: 
                j-=1 
        return []
