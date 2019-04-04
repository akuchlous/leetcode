# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs (root, nodes, totalS):
            nodes.append(str(root.val))
            if (root.left): 
                totalS = dfs(root.left, nodes, totalS)
            if (root.right):
                totalS = dfs(root.right, nodes, totalS)
            if (not root.left and not root.right):
                # print int("".join(nodes))
                totalS+= int("".join(nodes))
            nodes.pop()
            return totalS
            
        if (not root) : return 0
        totalS = 0
        nodes = []
        return dfs (root, nodes, totalS)
        
        
