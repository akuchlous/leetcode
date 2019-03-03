from collections import *
class P(object):
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def __repr__(self):
    	return "P repr print %d %d"%(self.a, self.b)
    def __str__(self):
    	return "P str print %d %d"%(self.b, self.a)


class OrderedCounter(Counter, OrderedDict):
     'Counter that remembers the order elements are first encountered'

     def __repr__(self):
         return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

     def __reduce__(self):
         return self.__class__, (OrderedDict(self),)



p = P(1,2)
print repr(p)
print str(p)

o = OrderedDict()
print repr(o)
print str(o)
O = OrderedCounter()
print repr(O)
