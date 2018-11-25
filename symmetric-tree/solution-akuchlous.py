class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if (root == None): return True
        return self.mirror (root.left, root.right)

    def mirror(self, lM, rM):
        if (lM == None) & (rM == None) : return True
        if (lM == None) & (rM != None) : return False
        if (lM != None) & (rM == None) : return False
        if (lM.val != rM.val) : return False
        return mirror(lM.right, rM.left) & mirror(lM.left, rM.right)

