# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import pdb

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if (not nums): return None
        mid = len(nums)//2
        node = TreeNode(nums[mid])
        self.sortedA(node, nums[:mid], nums[mid+1:])
        return node
    
    
    def sortedA(self, root, leftArr, rightArr):
        pdb.set_trace()
        if (len(leftArr)>2):
            leftNodeIdx = len(leftArr) // 2
            root.left = TreeNode(leftArr[leftArrIdx])
            self.sortedA(root.left, leftArr[:leftArrIdx], leftArr[leftArrIdx+1:])
        elif (len(leftArr) == 2):
            root.left = TreeNode(leftArr[1])
            root.left.left = TreeNode(leftArr[0])
        elif (len(leftArr) == 1):
            root.left = TreeNode(leftArr[0])
            
            
        if (len(rightArr)>2):
            leftNodeIdx = len(rightArr) // 2
            root.right = TreeNode(rightArr[leftArrIdx])
            self.sortedA(root.right, rightArr[:leftArrIdx], rightArr[leftArrIdx+1:])
        elif (len(rightArr) == 2):
            root.right = TreeNode(rightArr[1])
            root.right.left = TreeNode(rightArr[0])
        elif (len(rightArr) == 1):
            root.right = TreeNode(rightArr[0])


Solution().sortedArrayToBST([-10,-3,0,5,9])
