import pdb

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def dfs (root, count):
            if (root.next):
                head, tail, count = dfs(root.next, count)
            else:
                return root, root, count-1
            
            if (count>0):
                tail.next = root
                tail = root
                tail.next = None
            elif (count==0):
                root.next = None

                
            return (head, tail, count -1 )
        
        newHead, tail, _ = dfs(head, k)
        tail.next = head
        
        return newHead

def P(n):
	while (n):
		print (n.val)
		n = n.next

head = None
for i in range (10):
	l  = ListNode(i)
	if (not head):
		head = l
		tail = l
	else:
		tail.next =l
		tail = l

P( Solution().rotateRight(head, 1))
P( Solution().rotateRight(head, 3))
P( Solution().rotateRight(head, 7))



