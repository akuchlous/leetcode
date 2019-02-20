
class Solution(object):
    def maxDepth(self, a,b):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.goDown (a,b)

    def goDown(self, a,b):
        return max(a,b)


s = Solution()
s.maxDepth(1,3)
