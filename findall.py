import pdb

def findAll(str, w):
	ret = []
	inStr = "abcdabcdabcd"
	index = 0
	while (index > -1):
		# pdb.set_trace()
		i = inStr[index:].find (w)
		if (i == -1) :
			index = -1
		else:
			ret.append( index+i)
			index=index+i+len(w)
		if (index > len(inStr)):
			index = -1
	return ret
