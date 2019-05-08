import pdb
class MyLinkedList(object):

    class Node (object):
        def __init__(self, val):
            self.next = None
            self.val = val
            
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = self.tail = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        # could keep an array for fast lookup, but will have to update each time for add / delete 
        i = 0 
        n = self.head
        while (n):
            if i == index: 
                return n.val
            i+=1 
        return -1 
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        n = self.Node (val)
        n.next = self.head 
        self.head = n 
        if (not self.tail) :
            self.tail = self.head 

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if (not self.tail): 
            self.addAtHead(val)
        else:
            n = self.Node(val)
            self.tail.next = n
            self.tail = n

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
	pdb.set_trace()
	if (index == 0): return self.addAtHead(val)
        i = 1
        prevNode = self.head 
        currNode = prevNode.next
        while (currNode):
            if i == index:
                n = self.Node(val)
                n.next = currNode
                prevNode.next = n
                return
            currNode = currNode.next
            prevNode = prevNode.next
            i+=1 
        if (i == index):
            n = self.Node(val)
            self.tail.next = n
            self.tail = n
                    

    def Print(self):
	h = self.head
	while (h):
		print (h.val)
		h = h.next
		
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        i = 0
        currNode = self.head 
        if ((index == 0) and self.head):
            self.head = self.head.next
            return 
        i+=1
        prevNode = self.head 
        currNode = prevNode.next
        while (currNode):
            if i == index:
                prevNode.next = currNode.next
                if currNode == self.tail:
                    self.tail = prevNode
                break
            currNode = currNode.next
            i+=1 
        

linkedList = MyLinkedList()
print(linkedList.addAtHead(1))
linkedList.Print()
print(linkedList.addAtTail(3))
linkedList.Print()
print(linkedList.addAtIndex(1, 2))
linkedList.Print()
print(linkedList.get(1))
linkedList.Print()
print(linkedList.deleteAtIndex(1))
print(linkedList.get(1))
