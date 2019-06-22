#!/usr/bin/env python

import random
import pdb

def binSearch(nums, key):
	pdb.set_trace()
	start = 0
	end = len(nums) -1 
	while (start <= end):
		print (start, end)
		mid = start + (end-start)//2
		if nums[mid] == key:
			return mid
		elif nums[mid] > key:
			end = mid-1 
		else:
			start = mid +1 
	return -1 

def main():
	numbers = []
	for x in range(1,10):
		numbers.append(random.randint(1,100000))
	print numbers
	numbers.sort()
	print numbers
	search = numbers[3]
	print binSearch(numbers, search)

if __name__ == "__main__":
	main()

