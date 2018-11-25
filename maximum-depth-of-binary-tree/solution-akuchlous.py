# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        lvl = 0
        if (root==None): return 0
        return self.goDown (root, 0)

    def goDown(self, root, lvl):
        llvl = rlvl = lvl+1
        if (root.left) : llvl = goDown(root.left, lvl)
        if (root.right): rlvl = goDown(root.right, lvl)
        return max(llvl, rlvl)
