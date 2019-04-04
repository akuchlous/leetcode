# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        smallS = smallE = bigS = bigE = None

        if (not head) : return head
            
        while (head):
            if (head.val >= x ):
                if (not bigS) : 
                    bigS = bigE = head 
                else:
                    bigE.next = head 
                    bigE = head 
            else:
                if (not smallS):
                    smallS = smallE = head 
                else:
                    smallE.next = head 
                    smallE = head 
                
            head = head.next
        if (bigE): bigE.next = None
            
        if (smallE): smallE.next = bigS
        if (bigE): bigE.next = None 
    
        if (smallS): return smallS
        if (bigS): return bigS

