import pdb
class Po2:
	def __init__(self,maxN):
		self.max = maxN

	def __iter__(self):
		self.n = 0
		return self

	def next(self):
		if self.n <= self.max:
			result = 2** self.n
			self.n+=1 
			return result
		raise StopIteration


v = Po2(10)
i = iter(v)

print next(i)
while True:
	try:
		print i.next()
	except StopIteration:
		print "iterator end"
		break
			

