#!/usr/bin/env python
import pdb

def rev(nums):
	if (nums==[]): return nums
	lenN = len(nums)
	pdb.set_trace()
	done = False
	for x in range(1,lenN):
	        if (nums[lenN-x]> nums[lenN-x-1]):
	                tmp  = nums[lenN-x]
	                nums[lenN-x] = nums[lenN-x-1]
	                nums[lenN-x-1] = tmp
	                done = True
	                break
	        
	if (done == False): nums.sort(reverse=True)
	return nums


print (rev ([1,3,2]))
