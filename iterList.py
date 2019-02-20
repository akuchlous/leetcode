class listIter:
	def __init__(self, inL):
		self.list = inL
	def __iter__(self):
		self.listP = 0
		self.pos = 0
		return self

	def next(self):
		if (self.pos < len(self.list[self.listP])):
			retV = self.list[self.listP][self.pos]
			self.pos+=1
			return retV
		self.listP+=1
		self.pos=0
		if (self.listP < len(self.list)) :
			retV = self.list[self.listP][self.pos]
			self.pos+=1
			return retV
		raise StopIteration

in1 = [[], [3,4,5]]

iter1 = iter(listIter(in1))
while (True):
	try :
		print next(iter1)
	except StopIteration:
		print "done"
		break
