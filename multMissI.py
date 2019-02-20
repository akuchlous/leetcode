#!/usr/bin/env python


def mult(arr):
	forA = [1 for a in arr]
	revA = [1 for a in arr]
	aA = [1 for a in arr]
	for i in range(0, len(arr)):
		if (i ==0): forA[i] = arr[i]
		else: forA[i]=forA[i-1]*arr[i]
	for i in range(0, len(arr)):
		j = len(arr)-i-1
		if (j ==len(arr)-1): revA[j] = arr[j]
		else: revA[j]=revA[j+1]*arr[j]
	for i in range(0, len(arr)):
		if (i==0): aA[i] = revA[1]
		elif (i==len(arr)-1): aA[i] = forA[len(arr)-2]
		else:  aA[i] = forA[i-1] * revA[i+1]
		
	print (forA, revA, aA)

mult([1,2,3,4,5])
