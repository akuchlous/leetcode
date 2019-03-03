import pdb
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        index = 0
        prev = None
        count = 0
        for c in chars:
	    print (c)
            if not prev:
                prev, count = c , 1
	        continue
	    elif (prev == c):
	        count+=1
            else:
                chars[index] = prev
                index +=1 
                if (count) >1 :
                    numS = str(count)
                    for n in numS:
                        chars[index] = n
                        index+=1
                prev, count = c, 1
        chars[index] = prev
        index +=1 
        if (count) >1 :
            numS = str(count)
            for n in numS:
                chars[index] = n
                index+=1
        return index-1
        print (chars)


print (Solution().compress(["b", "a","a"]))
print (Solution().compress(["a","a","b","b","c","c","c"]))
