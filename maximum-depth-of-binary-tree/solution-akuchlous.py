# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def goDown(root, lvl):
        if (root==None): return lvl
        lvl += 1 
        return max(goDown(root.left, lvl), goDown(root.right, lvl))

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return goDown (root, 0)
