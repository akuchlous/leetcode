class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        ret = False
        while (i<len(bits)):
            if (bits[i] == 1):
                ret = False 
                i+=2
            else:
                ret = True 
                i+=1
        
        return ret


print (Solution().isOneBitCharacter([1, 1, 1, 0]))
print (Solution().isOneBitCharacter([1, 0,0 ]))
