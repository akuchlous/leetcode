# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import pdb

class Solution(object):
	def rev(self, head):
		if (head.next):
			first, ret = self.rev(head.next)
			ret.next = head
			return first, head
		else:
			return head, head

	def reverseKGroup(self, head, k):
		if (head == None): return None
		multList = []
		count = 0 
		multList.append(head)
		prev = None
		while (head):
			if (count <k):
				count+=1
				prev = head
				head=head.next
			else:
				multList.append(head)
				prev.next = None
				count = 0
				prev = None

	# check
		for l in multList:
			count = 0
			while (l):
				l = l.next
				count += 1
			# if (count != k):
				# print "error : count:", count
			count = 0 
		
		revMultList = []
		def p(l):
			buf = ""
			while (l):
				buf += str(l.val) + " "
				l = l.next
			print buf
	
		newList = []
		for l in multList:
			first, last = self.rev(l)
			count = 0 
			last.next = None
			c = first
			while (c ):
				c = c.next
				count+=1 
	
			if (count < k):
				first, last = self.rev(first)
				last.next = None
			newList.append(first)
			
		newNode = newList[0]
		prevNode = None
		for l in newList:
			if (prevNode):
				prevNode.next = l
			while (l):
				prevNode = l
				l = l.next
		p(newNode)
		return newNode

first = ListNode(1)
curr = first
for i in range (2,6):
	n = ListNode(i)
	curr.next = n
	curr  = n

buf = ""
l = first
while (l):
	buf += " "+str(l.val)
	l  = l.next
print buf

r = Solution().reverseKGroup(first, 2)
# buf = ""
# while (r):
# 	buf += " "+str(r.val)
# 	r  = r.next
# 
# print buf
# 
