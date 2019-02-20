import pdb

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i ,j =  0, m
        print (nums1)
        nums1[m:] = nums2
        print (nums1)
        while (i<m):
	    pdb.set_trace()
	    print (nums1, i, j)
            if (nums1[i] >= nums1[j]):
                nums1[i], nums1[j] = nums1[j], nums1[i]
            i+=1

        print (nums1)

Solution().merge([4,5,6,0,0,0] ,3 ,[1,2,3] ,3 )

#Solution().merge([1,2,3,0,0,0] ,3 ,[2,5,6] ,3 )


