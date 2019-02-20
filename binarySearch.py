#!/usr/bin/env python

import random
import pdb

def binarySearch(numbers, key):
	# print (numbers, "..", key)
	l = len(numbers)
	if (l == 1):
		# pdb.set_trace()
		if (numbers[0] == key):
			return 0
		else:
			return -1
	mid = len(numbers)/2
	left = numbers[:mid]
	right = numbers[mid:]
	if (key == numbers[mid]):
		return 0
	elif (key <numbers[mid]):
		return binarySearch(left, key)
	else:
		return binarySearch(right, key)

def main():
	numbers = []
	for x in range(1,10):
		numbers.append(random.randint(1,100000))
	print numbers
	numbers.sort()
	print numbers
	search = random.randint(1,100000)
	print search
	print binarySearch(numbers, search)
	print binarySearch(numbers, numbers[0])

if __name__ == "__main__":
	main()

