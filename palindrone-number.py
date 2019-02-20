#!/usr/bin/env python

def isPalindrome(x):
	"""
	:type x: int
	:rtype: bool
	"""
	if (x < 0):
	        return False
	digits = []
	while (x >0):
                # get last digit 
		# 123 % 10 = 3
		d = x%10
		# remove last digit 
		# 123 - (123/10 [=3]) / 10 = 12
		x = int((x - (x %10 )) / 10)
		digits.append(d)
	print (digits)
	while (len (digits) > 1) :
		if (digits.pop(0) != digits.pop()):
			return False
	return True


# print (isPalindrome(1239))
# print (isPalindrome(-1239))
# print (isPalindrome(1221))
# print (isPalindrome(12221))
print (isPalindrome(1000021))
