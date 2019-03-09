class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        addB = {
            #(in0, in1) : (carryover, result)
            ("0", "0","0"): ("0","0"),
            ("0", "1","0"): ("0","1"),
            ("0", "0","1"): ("0","1"),
            ("0", "1","1"): ("1","0"),
            ("1", "0","0"): ("0","1"),
            ("1", "1","0"): ("1","0"),
            ("1", "0","1"): ("1","0"),
            ("1", "1","1"): ("1","1"),
        }
            
        #pad the number with zeros to shorter number
        if (len(b) < len(a)):
            a,b = b,a
            
        if (len(a) < len(b)): 
            a=(len(b)-(len(a)))*"0"+a
        
        #print (a,b)
        
        carry="0"
        result = ""
        l = len(a)
        a = a[::-1]
        b = b[::-1]
        for i in range(l):
            carry, bit = addB[(carry, a[i], b[i])]
            result += bit
            # print (result, carry)
        if (carry == "1"): result += carry
        
        return result[::-1]

