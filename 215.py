import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        r = heapq.nlargest(k, nums)   
        return r[-1]
