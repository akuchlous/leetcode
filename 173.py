# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = []
        self.addLeftSubTree(root)

    def addLeftSubTree(self, current):
        while (current):
           self.nodes.append(current)
           current = current.left
   
    def next(self, current):
        """
        @return the next smallest number
        :rtype: int
        """
        last = self.nodex[-1]
        v = last.val
        del self.nodes[-1]
        self.addSelfSubTree(last)
           
        return v

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.nodes)>0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
