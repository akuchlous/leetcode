import pdb
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.l = []
        self.populate(nestedList)
	print (self.l)
        self.c = len(self.l)
        self.idx = 0 
        self.i = iter(self.l)

    def populate(self, curList):
        for c in curList:
            #pdb.set_trace()
            if (type(c) is not list):
                #print (c)
                self.l.append(c)
            else:
                self.populate(c)
         
        
    def next(self):
        """
        :rtype: int
        """
        self.idx+=1 
        return self.i.next()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx <self.c


n = NestedIterator([[1,1],2,[1,1]])
n = NestedIterator([1,[4,[6]]])
n = NestedIterator([1,[4,[6]],5])
n = NestedIterator([1,[4,[6],3],5])

