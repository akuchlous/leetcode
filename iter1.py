import pdb
class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def next(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

pdb.set_trace()
a = PowTwo(4)
i = iter(a)
while (True):
	try:
		print next(i)
	except StopIteration:
		print "done"
		break
