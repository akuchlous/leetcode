import sys
import pdb
class Solution:
	def mySqrt(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		do = True
		start = 0 
		end = x
		mid = 0 
		while (do):
			mid = (start+end)/2
			val = mid*mid
			if ((mid*mid - x) > 0.01 ):
				end = mid
			elif ((mid*mid - x) < -0.01):
				start =  mid
			else:
				do = False
			#print (val, start, end, mid)
			if (int(start) == int(end) ):
				return (int(mid))
		return( int(mid))

print(Solution().mySqrt(2147483647))



