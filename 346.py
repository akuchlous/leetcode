class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.count = 0
        self.last = 0
        self.avg = 0 
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if (self.count <self.size):
            sumP = (self.avg*self.count) + val 
            print ("S=>", sumP)
            self.count+=1 
            self.avg = float(sumP/self.count)
            self.last = val
        else:
            sumP = (self.avg*self.size) - self.last + val
            print ("Last, S=>", (self.avg*self.size), sumP)
            self.avg = float(sumP/ self.size )
            self.last = val
            
        return self.avg

m = MovingAverage(3)
print (m.next(1))
print (m.next(10))
print (m.next(3))
print (m.next(5))
    
