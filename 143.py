# Definition for singly-linked list.
import pdb

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        newL = []
        if (not head): return head
        n = head
        while (n.next):
            newL.append(n.next)
            n = n.next
        currentNode = head
        front = False 
        while newL:
            if front:
                nxtNode = newL.pop(0)
                front = False 
            else:
                front = True
                nxtNode = newL.pop()
            currentNode.next = nxtNode
            currentNode = nxtNode
        currentNode.next = None
        return head
                

def P(node):
	while (node):
		print (node.val)
		node = node.next
	print ("\n\n")
head = currNode = None
for i in range(5):
	l = ListNode(i)
	if (not head): head = l
	if (not currNode): currNode = l
	else: currNode.next = l; currNode= l

P(head)
Solution().reorderList(head)
P(head)
