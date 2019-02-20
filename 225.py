from queue import Queue
import pdb
import copy

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = Queue()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q.put(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        size = self.q.qsize()
        nq = Queue()
        pdb.set_trace()
        while (size>1):
            nq.put(self.q.get())
            size = size - 1 
        last = self.q.get()
        self.q = nq
        return last
        
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        size = self.q.qsize()
        nq = Queue()
        while (size>0):
            last = self.q.get()
            nq.put(last)
            size = size - 1
        self.q = nq
        return last
        
    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q.empty()
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
print(obj.push(3))
print(obj.push(4))
print(obj.top())
print(obj.pop())
print(obj.empty())
