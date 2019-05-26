#!/usr/bin/env python

import pdb

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def dfs(numbers, res):
            if (not numbers): 
		return res
            res = dfs(numbers[1:], res)
            r1 = [[numbers[0]] + x for x in res]
            r2 = [[numbers[0]]]
            res = r1+r2 + res
            return res
        res =  dfs(nums, [])
        res.append([])
        res.sort()
        return res 
        

print (Solution().subsets([ i for i in range(1, 4)]))
