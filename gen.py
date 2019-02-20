import pdb
def countdown(num):
	print("Starting")
	while (num >0):
		yield num
		num -= 1

pdb.set_trace()
val = countdown(1)
print val
print next(val)
print next(val)
print next(val)
print next(val)
print next(val)
