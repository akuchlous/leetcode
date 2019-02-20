from itertools import permutations as pm
from itertools import combinations as cm 
from collections import defaultdict
import pdb

def BA(n):
	n = 5
	sum2 = defaultdict(list)
	nums = [x for x in range(1, n+1)]
	allC = cm(nums, 2)
	for c in allC:
		sum2[sum(c)].append(c)
	
	allP = pm (nums, n)
	for p in allP:
		status = True
		for k in range(1, len(p)-1):
			if (p[k]*2 in sum2):
				for s in sum2[p[k]*2]:
					i = p.index(s[0])
					j = p.index(s[1])
					if (i < k and k< j):
						status = False
		if (status == True):
			return (p)
	
print (BA(4))
